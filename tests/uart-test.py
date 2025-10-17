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

#import pyftdi.serialext
import argparse
import textwrap
import sys

def test_helloworld(write_port : str, read_port : str) -> int:
    return 0

def test_bandwidth(write_port : str, read_port : str) -> int:
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                prog='ecap5-bcarrier-xlite-uart-test',
                formatter_class=argparse.RawDescriptionHelpFormatter,
                description=textwrap.dedent('''\
                This program tests the UART to USB link of the ECAP5-BCARRIER-XLITE board by 
                injecting UART through an FT232H IC connected to the selector header and reading 
                back the data on the USB link.
            '''))

    parser.add_argument('mode', choices=['helloworld', 'bandwidth'])
    parser.add_argument('-i', '--injecting-port', required=True)
    parser.add_argument('-u', '--usb-port', required=True)

    args = parser.parse_args()
    if args.mode == 'helloworld':
        err = test_helloworld(args.injecting_port, args.usb_port)
        sys.exit(err)
    elif args.mode == 'bandwidth':
        err = test_bandwidth(args.injecting_port, args.usb_port)
        sys.exit(err)
    else:
        print("Unimplemented mode : {}".format(args.mode))
        sys.exit(-1)
