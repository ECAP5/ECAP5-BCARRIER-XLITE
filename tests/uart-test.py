#!/usr/bin/env python3

#           __        _
#  ________/ /  ___ _(_)__  ___
# / __/ __/ _ \/ _ `/ / _ \/ -_)
# \__/\__/_//_/\_,_/_/_//_/\__/
# 
# Copyright (C) Clément Chaine
# This file is part of ECAP5-BCARRIER-XLITE <https://github.com/ecap5/ECAP5-BCARRIER-XLITE>
# 
# ECAP5-BCARRIER-XLITE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# ECAP5-BCARRIER-XLITE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with ECAP5-BCARRIER-XLITE.  If not, see <http://www.gnu.org/licenses/>.

import pyftdi.serialext
import pyftdi.ftdi
import threading
import argparse
import textwrap
import sys
import random
import string
import time

BAUDRATES = [
    9600, 115200, 460800, 921600, 2000000, 3000000, 4000000, 5000000, 6000000, 12000000
]

def list_devices() -> int:
    pyftdi.ftdi.Ftdi.show_devices()
    return 0

def receive_thread(port : str, baudrate : int, num_bytes : int, read_data : list[bytes]) -> None:
    try:
        reader = pyftdi.serialext.serial_for_url(port, baudrate=baudrate, timeout=0.1)

        done = False
        while not done:
            read_data[0] = reader.read(num_bytes)
            if(len(read_data[0]) > 0):
                done = True

        reader.flushInput()
        reader.flushOutput()
        reader.close()

        read_data[0] = read_data[0].decode("utf-8")
        read_data[1] = 0
    except ValueError:
        read_data[1] = 1
    return

def test_helloworld(write_device: str, read_device: str) -> int:
    print("Running helloworld test...")
    data = "Hello World!"

    # Read data will be written in this mutable table
    read_data = [[]]
    # Start the reading thread first
    rt = threading.Thread(target=receive_thread, args=(read_device, BAUDRATES[0], len(data), read_data))
    rt.start()
    
    # Write the data
    writer = pyftdi.serialext.serial_for_url(write_device, baudrate=BAUDRATES[0])
    writer.write(data)

    # Wait for the data to be read
    rt.join()
    writer.close()

    read_data = read_data[0]

    print("Written: {} -> {}".format(write_device, data))
    print("Read:    {} -> {}".format(read_device, read_data))

    return data != read_data

def test_bandwidth(write_device : str, read_device: str) -> int:
    print("Running bandwidth test : ", end="")
    print("{} -> {}".format(write_device, read_device))

    # Test each baudrate
    for baudrate in BAUDRATES:
        data = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(baudrate))

        print("{} baud ".format(baudrate), end="", flush=True)

        # Read data will be written in this mutable table
        read_data = [[], 0]
        # Start the reading thread first
        rt = threading.Thread(target=receive_thread, args=(read_device, baudrate, len(data), read_data))
        rt.start()

        # Write the data
        try:
            writer = pyftdi.serialext.serial_for_url(write_device, baudrate=baudrate)

            start_time = time.time()
            writer.write(data)
            end_time = time.time()

            bitrate = (len(data)*8) / (end_time - start_time)

            # Wait for the data to be read
            rt.join()
            writer.close()

            # If the baudrate on the reading port is not supported
            if read_data[1] != 0:
                print("not supported")
                continue

            read_data = read_data[0]

            if len(data) != len(read_data):
                print("KO - expected {} bytes, read {} bytes".format(len(data), len(read_data)))
                continue

            # Compare the read data with the expected data
            num_errors = 0
            for i in range(len(data)):
                if data[i] != read_data[i]:
                    num_errors += 1

            if num_errors > 0:
                print("KO - {} erroneous bytes".format(num_errors))
            else:
                print("OK - {} bytes at {:.0f}kbps".format(len(data), bitrate / 1000.0))
        except ValueError:
            print("not implemented")
            continue

    return num_errors

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                prog='ecap5-bcarrier-xlite-uart-test',
                formatter_class=argparse.RawDescriptionHelpFormatter,
                description=textwrap.dedent('''\
                This program tests the UART to USB link of the ECAP5-BCARRIER-XLITE board by 
                injecting UART through an FT232H IC connected to the selector header and reading 
                back the data on the USB link.
            '''))

    parser.add_argument('mode', choices=['list', 'helloworld', 'bandwidth'])
    parser.add_argument('-d1', '--device1')
    parser.add_argument('-d2', '--device2')

    args = parser.parse_args()

    if args.mode in ['helloworld', 'bandwidth'] and ((args.device1 is None) or (args.device2 is None)):
        parser.error("--device1 and --device2 are required")

    if args.mode == 'list':
        err = list_devices()
        sys.exit(err)
    if args.mode == 'helloworld':
        err  = test_helloworld(args.device1, args.device2)
        err |= test_helloworld(args.device2, args.device1)
        sys.exit(err)
    elif args.mode == 'bandwidth':
        err = test_bandwidth(args.device1, args.device2)
        err = test_bandwidth(args.device2, args.device1)
        sys.exit(err)
    else:
        print("Unimplemented mode : {}".format(args.mode))
        sys.exit(-1)
