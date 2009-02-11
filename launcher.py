
from time import time
from time import sleep

class Launcher:
    """Basic missile launcher definition featuring simple calibration"""
    DOWN = 0
    UP = 1
    LEFT = 2
    RIGHT = 3
    
    def calibrate(self):
        """Calibrates this launcher by going finding transit time between extents in each dimension"""
        self.moveUp()
        self.waitForExtent(self.UP)
        start_down = time()
        self.moveDown()
        self.waitForExtent(self.DOWN)
        stop_down = time()
        vertical_transit = stop_down - start_down
        self.moveLeft()
        self.waitForExtent(self.LEFT)
        start_right = time()
        self.moveRight()
        self.waitForExtent(self.RIGHT)
        stop_right = time()
        horizontal_transit = stop_right - start_right
        self.setTransitTimes(horizontal_transit, vertical_transit)
    
    def waitForExtent(self, extent):
        """Waits for the launcher to read a given extent"""
        extents = self.checkExtents()
        while not extents[extent]:
            extents = self.checkExtents()
    
    def aim(self, azimuth, elevation):
        """Positions the launcher at a given azimuth and elevation given its current position"""
        pass
    

