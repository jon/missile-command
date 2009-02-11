#!/usr/bin/env python
# encoding: utf-8
"""
dream_cheeky.py

Created by Erik Hollembeak on 2009-02-10.
Copyright (c) 2009 Future Perfect Software. All rights reserved.
"""

import sys
import os
from launcher import Launcher

azimuthRate = 2  # degrees per second
elevationRate = 4 # degrees per second

class DreamCheekyLauncher(Launcher):
    """Driver for DreamCheeky USB dart launcher"""
    def __init__(self, device):
        super(DreamCheekyLauncher, self).__init__()
        self.device = device
    
    def start(self):
        """Opens the launcher and takes control of it"""
        self.handle = handle = self.device.open()
        try:
            handle.reset()
            handle.claimInterface(0)
        except:
            handle.detachKernelDriver(0)
            handle.reset()
            handle.claimInteface(0)
    
    def sendCommand(self, command):
        """Sends a command to the robot"""
        self.handle.controlMsg(0x21, 0x09, [command], 0x0200)
    
    def moveLeft(self):
        """Starts turret moving counterclockwise"""
        self.sendCommand(4)
    
    def moveRight(self):
        """Starts turret moving clockwise"""
        self.sendCommand(8)
    
    def moveUp(self):
        """Starts turret moving towards higher elevation"""
        self.sendCommand(2)
    
    def moveDown(self):
        """Starts turret moving towards lower elevation"""
        self.sendCommand(1)
    
    def stop(self):
        """Stops turrent movement"""
        self.sendCommand(0x20)
    
    def primeRocket(self):
        """Primes rocket for firing"""
        pass
    
    def fireRocket(self):
        """Fires rocket"""
        self.sendCommand(0x10)
    

