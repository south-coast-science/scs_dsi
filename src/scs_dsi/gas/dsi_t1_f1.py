"""
Created on 27 May 2019

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://github.com/south-coast-science/scs_dsi_t1_f1
"""

import struct
import time

from scs_host.bus.i2c import I2C
from scs_host.lock.lock import Lock


# --------------------------------------------------------------------------------------------------------------------

class DSIt1f1(object):
    """
    South Coast Science DSI t1 f1 microcontroller
    """
    ADDR_AUX =          0x48


    # ----------------------------------------------------------------------------------------------------------------


    # ----------------------------------------------------------------------------------------------------------------

    __LOCK_TIMEOUT =    2.0


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, addr):
        """
        Constructor
        """
        self.__addr = addr


    # ----------------------------------------------------------------------------------------------------------------

    def start_conversion(self):
        pass


    def read_conversion(self):
        pass


    # ----------------------------------------------------------------------------------------------------------------

    def test(self, cmd):
        try:
            self.obtain_lock()
            I2C.start_tx(self.__addr)

            return I2C.read_cmd(cmd, 2)

        finally:
            I2C.end_tx()
            self.release_lock()


    # ----------------------------------------------------------------------------------------------------------------

    def obtain_lock(self):
        Lock.acquire(self.__lock_name, DSIt1f1.__LOCK_TIMEOUT)


    def release_lock(self):
        Lock.release(self.__lock_name)


    @property
    def __lock_name(self):
        return self.__class__.__name__ + "-" + ("0x%02x" % self.__addr)


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def addr(self):
        return self.__addr


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "DSIt1f1:{addr:0x%0.2x}" % self.addr
