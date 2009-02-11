# Copyright (C) 2009 Ballistic Pigeon, LLC

from time import time
from time import sleep

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
        vertical_transit = stop_down - start_down
        self.moveLeft()
        self.waitForExtent(self._LEFT)
        start_right = time()
        self.moveRight()
        self.waitForExtent(self._RIGHT)
        stop_right = time()
        horizontal_transit = stop_right - start_right
        self.setTransitTimes(horizontal_transit, vertical_transit)
    
    def waitForExtent(self, extent):
        """Waits for the launcher to read a given extent"""
        extents = self.checkExtents()
        while not extents[extent]:
            extents = self.checkExtents()
    
    def aim(self, azimuth, elevation):
        """Positions the launcher at a given azimuth and elevation given its current position. 
        Returns the elapsed time for azimuth and elevation movement as a tuple (azimuthTime, elevationTime)"""
        dtAzimuth = (azimuth - self.azimuth) / self.azimuthRate
        dtElevation = elevation - self.elevation / self.elevationRate
        self.moveRight() if dtAzimuth > 0 else self.moveLeft()
        startAzimuth = time()
        sleep(abs(dtAzimuth))
        self.stop()
        stopAzimuth = time()
        self.moveUp() if dtElevation > 0 else self.moveDown()
        startElevation = time()
        sleep(abs(dtElevation))
        self.stop()
        stopElevation = time()
        return ((stopAzimuth - startAzimuth), (stopElevation - startElevation))
    

