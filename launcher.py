# Copyright (C) 2009 Ballistic Pigeon, LLC

from time import time
from time import sleep
from simple_math import *

class Launcher(object):
    """Basic missile launcher definition featuring simple calibration"""
    _DOWN = 0
    _UP = 1
    _LEFT = 2
    _RIGHT = 3
    
    def calibrate(self):
        """Calibrates this launcher by going finding transit time between extents in each dimension"""
        self.moveUp()
        self.waitForExtent(self._UP)
        start_down = time()
        self.moveDown()
        self.waitForExtent(self._DOWN)
        stop_down = time()
        self.vertical_transit = stop_down - start_down
        self.moveLeft()
        self.waitForExtent(self._LEFT)
        start_right = time()
        self.moveRight()
        self.waitForExtent(self._RIGHT)
        stop_right = time()
        self.horizontal_transit = stop_right - start_right
        
        # We're at the bottom right, so minimum elevation, maximum azimuth
        self.azimuth = self.azimuthRange[1]
        self.elevation = self.elevationRange[0]
        
        # Calculate the total range (in radians) for each dimension
        scalarAzimuthRange = self.azimuthRange[1] - self.azimuthRange[0]
        scalarElevationRange = self.elevationRange[1] - self.elevationRange[0]
        
        # Use transit times to calculate angular velocities in rads/sec
        self.azimuthRate = scalarAzimuthRange / self.horizontal_transit
        self.elevationRate = scalarElevationRange / self.vertical_transit
        
        # Center the launcher at (0, 0)
        self.center()
    
    def center(self):
        """Centers the launcher by traveling to nearest extents and returning to center"""
        if self.azimuth < 0:
            self.moveLeft()
            self.waitForExtent(self._LEFT)
        else:
            self.moveRight()
            self.waitForExtent(self._RIGHT)
            
        if self.elevation < 0:
            self.moveDown()
            self.waitForExtent(self._DOWN)
        else:
            self.moveUp()
            self.waitForExtent(self._UP)
            
        self.aim(0, 0)
    
    def waitForExtent(self, extent):
        """Waits for the launcher to read a given extent"""
        extents = self.checkExtents()
        while not extents[extent]:
            extents = self.checkExtents()
    
    def updatePositionWithExtents(self, extents):
        """Updates the current heading of the launcher based on any extents that have been hit"""
        bottom, top, left, right = extents
        if bottom or top:
            self.elevation = self.elevationRange[0] if top else self.elevationRange[1]
        if left or right:
            self.azimuth = self.azimuthRange[0] if left else self.azimuthRange[1]
    
    def aim(self, azimuth, elevation):
        """Positions the launcher at a given azimuth and elevation given its current position. 
        Returns the elapsed time for azimuth and elevation movement as a tuple (azimuthTime, elevationTime)"""
        
        # Calculate desired movement times
        dtAzimuth = (azimuth - self.azimuth) / self.azimuthRate
        dtElevation = (elevation - self.elevation) / self.elevationRate
        
        # Move azimuth
        self.moveRight() if dtAzimuth > 0 else self.moveLeft()
        startAzimuth = time()
        sleep(abs(dtAzimuth))
        self.stop()
        stopAzimuth = time()
        azimuthTransit = stopAzimuth - startAzimuth
        self.azimuth += azimuthTransit*self.azimuthRate * sign(dtAzimuth)
        
        self.moveUp() if dtElevation > 0 else self.moveDown()
        startElevation = time()
        sleep(abs(dtElevation))
        self.stop()
        stopElevation = time()
        elevationTransit = stopElevation - startElevation
        self.elevation += elevationTransit*self.elevationRate * sign(dtElevation)
        
        return (self.azimuth, self.elevation)
    

