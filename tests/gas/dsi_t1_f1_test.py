#!/usr/bin/env python3

"""
Created on 27 May 2019

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import time

from scs_dsi.gas.dsi_t1_f1 import DSIt1f1

from scs_host.bus.i2c import I2C
from scs_host.sys.host import Host


# --------------------------------------------------------------------------------------------------------------------

controller = DSIt1f1(0x30)
print(controller)


# --------------------------------------------------------------------------------------------------------------------

try:
    I2C.open(Host.I2C_SENSORS)

    result = controller.test(6)
    print("result: %s" % str(result))

finally:
    I2C.close()
