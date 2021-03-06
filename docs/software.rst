############
Software
############

The software framework has a modular structure that reflects the firmware and adds extra layers to make hardware interface user friendly. It loosely follows Register Abstract Layer (RAL) concepts. All the layers are automatically created based on yaml configuration file. 

.. image:: _static/basil_layers.png

Yaml configuration file
====================

TBD

Transfer Layer (TL)
====================

Implements communication interface like UART, USB, Ethernet or Simulation.
Every TL interface implements 2 functions:

.. code-block:: python

    def write(self, addr, data):

and

.. code-block:: python

    def read(self, addr, size):

Hardware Layer (HL)
====================

Implements drivers for basil modules and external devices.

User Layer (UL)
===============

Implements drivers which make use of HL. Example ADC control with spi module.


Register Layer (RL)
===================

Implements Register Level Abstraction. Allow to user/control software to work on DUT registers without taking thinking about underlying levels.

