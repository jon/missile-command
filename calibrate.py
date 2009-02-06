#!/sw/bin/python2.5

from rocket_backend import *
from time import time
from time import sleep

points = []

manager = RocketManager()
manager.acquire_devices()

try:
   rocket = manager.launchers[0]
except: IndexError:
   print "No rocket launchers"
   exit(1)

DOWN = 0
UP = 1
LEFT = 2
RIGHT = 3

def wait_for(direction):
   """docstring for wait_for"""
   limits = (False,)*4
   while not limits[direction]:
      limits = rocket.check_limits()

def mean(collection):
   """docstring for mean"""
   return float(sum(collection)) / len(collection)


for x in range(1):
   rocket.start_movement(DOWN)
   wait_for(DOWN)

   start_vert = time()
   rocket.start_movement(UP)
   wait_for(UP)
   stop_vert = time()

   rocket.start_movement(LEFT)
   wait_for(LEFT)

   start_horiz = time()
   rocket.start_movement(RIGHT)
   wait_for(RIGHT)
   stop_horiz = time()

   points.append((stop_vert - start_vert, stop_horiz - start_horiz))

mean_vert = mean([vert for vert, horiz in points])
mean_horiz = mean([horiz for vert, horiz in points])

print (mean_vert, mean_horiz)

rocket.start_movement(UP)
wait_for(UP)
rocket.start_movement(DOWN)
sleep(mean_vert / 2.0)
rocket.stop_movement()

rocket.start_movement(LEFT)
wait_for(LEFT)
rocket.start_movement(RIGHT)
sleep(mean_horiz / 2.0)
rocket.stop_movement()

for p in points:
   print p
