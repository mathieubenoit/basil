
Basil modules
===============

.. begin-include

Modules use simple bus single master interconnection bus.
Every module has same/similar set of parameters and pins that allow to properly connect to bus.

List of modules can be found in `device/modules folder <https://github.com/SiLab-Bonn/basil/tree/master/device/modules>`_.

Software drivers for modules can be found in `host/basil/HL folder <https://github.com/SiLab-Bonn/basil/tree/master/host/basil/HL>`_.

Parameters
    +--------------+---------------------+--------------------------------------------------------------------+ 
    | Name         | Default             | Description                                                        | 
    +==============+=====================+====================================================================+ 
    | BASEADDR     | 0                   | Defines base address of module (start address) in memory map space | 
    +--------------+---------------------+--------------------------------------------------------------------+ 
    | HIGHADDR     | 0                   | Defines last module address in memory map space                    |
    +--------------+---------------------+--------------------------------------------------------------------+ 
    | ABUSWIDTH    | 16                  | Define address bus with                                            |
    +--------------+---------------------+--------------------------------------------------------------------+ 
    | DBUSWIDTH    | 8                   | Define data bus with                                               |
    +--------------+---------------------+--------------------------------------------------------------------+ 

Pins
    +--------------+-------------------------+-----------+------------------------------------------------------+ 
    | Name         | Size                    | Direction | Description                                          | 
    +==============+=========================+===========+======================================================+ 
    | BUS_RST      | 1                       | input     | Synchronous Reset - Active High                      | 
    +--------------+-------------------------+-----------+------------------------------------------------------+ 
    | BUS_CLK      | 1                       | input     | Clock                                                | 
    +--------------+-------------------------+-----------+------------------------------------------------------+ 
    | BUS_WR       | 1                       | input     | Write strobe - Active High                           | 
    +--------------+-------------------------+-----------+------------------------------------------------------+ 
    | BUS_RD       | 1                       | input     | Read strobe - Active High                            | 
    +--------------+-------------------------+-----------+------------------------------------------------------+ 
    | BUS_ADD      | ABUSWIDTH               | input     | Address bus`                                         | 
    +--------------+-------------------------+-----------+------------------------------------------------------+ 
    | BUS_DATA     | DBUSWIDTH (typically 8) | inout     | Data Bus                                             | 
    +--------------+-------------------------+-----------+------------------------------------------------------+
