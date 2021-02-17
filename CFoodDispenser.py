#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:26:18 2021

@author: ravindu
"""

import Eye
import TestTray
import time

INTERVAL_BETWEEN_DISPENSING = 10

try:
    Eye.open()
    while True:
        if(Eye.see()):
            Eye.close()
            TestTray.openTray()
            time.sleep(INTERVAL_BETWEEN_DISPENSING)
            Eye.open()
except KeyboardInterrupt:
    print('Closing on keyboard interrupt')
finally:    
    Eye.close()
    print('Bye!')