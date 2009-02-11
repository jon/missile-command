#!/sw/bin/python2.5
# Copyright (C) 2009 Ballistic Pigeon, LLC

import usb
from dream_cheeky import DreamCheekyLauncher

# Supported launchers represnted as a dictionary mapping device identifiers
# (as a tuple containing the vendor and device id) to driving classes
launcher_definitions = { (0x0a81, 0x0701) : DreamCheekyLauncher }

def find_launcher_devices():
    """Searches connected USB busses for any known rocket launcher variants"""
    devices_list = [ list(bus.devices) for bus in usb.busses() ]
    devices = sum(devices_list, [])
    return [ d for d in devices if (d.idVendor, d.idProduct) in launcher_definitions ]
    
def find_launchers():
    """Instantiates controllers for all launchers found on the system and returns a list"""
    devices = find_launcher_devices()
    drivers = [ launcher_definitions[(d.idVendor, d.idProduct)] for d in devices ]
    return [ driver(device) for device, driver in zip(devices, drivers) ]
    
def main():
    """Tests launchers.py"""
    launchers = find_launchers()
    if len(launchers) == 0:
        print "Found no launchers."
    else:
        print "Found the following launchers:"
        for launcher in launchers:
            print launcher            


if __name__ == '__main__':
    main()