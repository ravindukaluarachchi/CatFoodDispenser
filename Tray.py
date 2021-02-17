#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 16:23:13 2021

@author: ravindu
"""

import RPi.GPIO as GPIO
import time


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    global pwm
    pwm = GPIO.PWM(11,50)
    pwm.start(0)

def clean():
    pwm.stop()
    GPIO.cleanup()
    
def openTray():
    setup()
    pwm.ChangeDutyCycle(1)
    time.sleep(10)
    pwm.ChangeDutyCycle(3)
    clean()

