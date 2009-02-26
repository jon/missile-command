#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2009 Ballistic Pigeon, LLC

import sys
import os
from launcher import Launcher

class DreamCheekyLauncher(Launcher):
    """Driver for DreamCheeky USB dart launcher"""
    def __init__(self, device):
        super(DreamCheekyLauncher, self).__init__()
        self._device = device
        self._started = False
        self.azimuthRange = (-2.76383645932, 2.76383645932) # Range of rotation in radians
        self.elevationRange = (-0.120671968473228, 0.432407775570538)
    
    def start(self):
        """Opens the launcher and takes control of it"""
        self._handle = handle = self._device.open()
        try:
            handle.reset()
            handle.claimInterface(0)
        except:
            handle.detachKernelDriver(0)
            handle.reset()
            handle.claimInterface(0)
        self._started = True
    
    def sendCommand(self, command):
        """Sends a command to the robot"""
        if not self._started:
            self.start()
        self._handle.controlMsg(0x21, 0x09, [command], 0x0200)
    
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
    
    def checkExtents(self):
        """Checks to see if the rocket is at any of its extents"""
        self.sendCommand(0x40)
        byte, = self._handle.bulkRead(1, 1)
        bottom = (byte & 0x1) <> 0
        top = (byte & 0x2) <> 0
        left = (byte & 0x4) <> 0
        right = (byte & 0x8) <> 0
        extents = (bottom, top, left, right)
        self.updatePositionWithExtents(extents)
        return extents
        

