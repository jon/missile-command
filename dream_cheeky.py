#!/usr/bin/env python
# encoding: utf-8
"""
dream_cheeky.py

Created by Erik Hollembeak on 2009-02-10.
Copyright (c) 2009 Future Perfect Software. All rights reserved.
"""

import sys
import os

azimuthRate = 2  # degrees per second
elevationRate = 4 # degrees per second

class DreamCheekyLauncher(Launcher):
    """docstring for DreamCheekyLauncher"""
    def __init__(self, arg):
        super(DreamCheekyLauncher, self).__init__()
        self.arg = arg
    
    def moveLeft(self):
        """Starts turret moving counterclockwise"""
        pass
    
    def moveRight(self):
        """Starts turret moving clockwise"""
        pass
    
    def moveUp(self):
        """Starts turret moving towards higher elevation"""
        pass
    
    def moveDown(self):
        """Starts turret moving towards lower elevation"""
        pass
    
    def stop(self):
        """Stops turrent movement"""
        pass
    
    def primeRocket(self):
        """Primes rocket for firing"""
        pass
    
    def fireRocket(self):
        """Fires rocket"""
        pass
    

