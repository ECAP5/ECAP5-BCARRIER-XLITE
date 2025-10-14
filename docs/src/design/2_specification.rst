Specification
=============

.. requirement:: U_POWER_01
   :rationale: The board will be powered by a lab bench power supply.

   The board shall include a 2x1 terminal block connector for power input with a voltage range of 9V to 15V.

.. requirement:: U_POWER_02

   The board shall include reverse polarity and ESD protection after the power input connector.

.. requirement:: U_POWER_03

   The board shall include a 9-15V to 3.3V voltage regulator.

.. requirement:: U_POWER_04

   An LED shall be connected to the 3.3V regulator output.

.. requirement:: U_SOM_01

   The board shall include two DDR4-SODIMM connectors.

.. requirement:: U_SOM_02

   Any routing of the DDR4-SODIMM connector pins shall comply with the following pinout.

.. image:: ../assets/io-pinout.svg
   :align: center
   :width: 50%

.. list-table:: SO-DIMM IO Connector Signal Description
   :header-rows: 1
   :width: 100%

   * - Name
     - Type
     - Description

   * - JTAG_TCK
     - I
     - JTAG clock input
   * - JTAG_TDI
     - I
     - JTAG data input
   * - JTAG_TDO
     - O
     - JTAG data output
   * - JTAG_TMS
     - I
     - JTAG test mode select input
   * - SE[0-67]
     - I/O
     - Single-Ended general purpose 3v3 input/output
   * - RTD[0-64][P/N]
     - I
     - General purpose input/output LVDS2V5
   * - RESET_I
     - I
     - Reset input
   * - VIN9_15
     - 
     - Main power input 9~20V
   * - unused
     - 
     - 
   * - GND
     - 
     - 

.. note:: Unused pins are left unconnected but reserved on the connector for future use.

.. requirement:: U_SOM_03

   The VIN9_15 pins of the DDR4-SODIMM connectors shall be connected to the protected 9-15V board power.

.. requirement:: U_SOM_04

   The JTAG pins of the DDR4-SODIMM connectors shall be routed to separate pin headers for each SOM.

.. requirement:: U_SOM_05

  The RESET_IN pins of the DDR4-SODIMM connectors shall be routed to separate tactile switches for each SOM.

.. requirement:: U_BUS_01

  8 differential pairs shall be routed between the two SOMs.

.. requirement:: U_BUS_02

  16 single-ended signals shall be routed between the two SOMs.

.. requirement:: U_UART_01

  The board shall include a USB-to-UART converter.

.. requirement:: U_UART_02

  Pin headers shall be used with jumpers to allow the user to select which of the SOM's UART pins are connected to the USB-to-UART converter.

.. requirement:: U_USER_01

   Two tactile switches shall be connected to one of the SOMs, supplying 3.3V when activated.

.. requirement:: U_USER_02

   Two LEDs shall be connected to one of the SOMs in an open drain configuration.

.. requirement:: U_TEST_01

   One single-ended signal of one of the SOMs shall be routed to a coaxial connector.

.. requirement:: U_TEST_02

   One differencial pair of one of the SOMs shall be routed to two coaxial connectors, one for the true signal and one for the complement..

.. requirement:: U_MECHANICAL_01

   The board shall include M2 mounting holes.
