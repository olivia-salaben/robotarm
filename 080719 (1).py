"""Code for locations of 2 magnets, order in which the magnets are placed"""
import numpy as np
from astropy.table import Table
import matplotlib.pyplot as plt
import pandas as pd 

"""r is from the center of the imaginary circle, given by (x,y)"""
circ_magnet_imaginary_radius = r = 6 mm 
dist(circular, rectangular) = g = 23 mm
length_of_rectangular_magnet = L = 20 mm
width_of_arm = w = 5 mm
point_robot = f = .5 * w = .200 mm

#CIRCLE CENTER COORDINATES 
for probe in textfile
#These coordinates are absolute coordinates
circ_coordinates = (x, y)
(x, y) = (columns['x'], columns['y'])
"""Need to convert (x, y) from degrees into mm such that 1 degree = 260 mm"""
mm_cordinates = (x * 260, y * 260) = circ_coordinates * 260
"""plate goes from -260<x<260 and -260<y<260"""
"""Turns plate into a grid in mm rather than degrees. It is confusing working in degrees and radians"""
theta = angs_azAngs*(180/pi) - 90
center_circ = mm_cordinates

#CODE FOR ROTATION MATRIX
i = (a, b)
def(rot_angle):
    for i in center_circ
        if a, b > 0:
           return math.atan(b/a)
        if a < 0, b > 0:
           return 180 - math.atan(b/a)
        if a < 0, b < 0:
            return 180 + math.atan(b/a)
        if a > 0, b < 0:
            return 360 - math.atan(b/a)
angle = np.radians(rot_angle)
RotMatrix = np.array([[np.cos(angle), -np.sin(angle)],
                      [np.sin(angle), np.cos(angle)]])
"For the code above, using math.atan2(y,x) will take into account the sign of the inputs so it can compute the correct quadrant for the angle"

#RECTANGULAR CENTER COORDINATES
"Here I am using the Rotation Matrix to find the absolute coordinates of the center of the rectangular magnets"
"I am rotating the coordinates with respect to the angle/quadrant they are at on the plate to"

def(center_rectangle):
    x1 = sin(theta) * ((.5 * L) + g + r)
    y1 = cos(theta) * ((.5 * L) + g + r)
    k = (x + x1, y + y1)
return: RotMatrix * np.array([k])

"Now that we have the location of the center of the rectangular magnetes, we are going to use the kernel density of a given orientation of probes"
"Using this method to determine an order because we need more densities than just the peak"
"Can solve using n nearest neighbors"
"Want to assign each magnet with their respective density, find peak density, and go to next densest region until all the magnets are cleared or placed"

#GAUSSIAN KERNEL DENSITY ESTIMATE
"one or two columns of all magnet centers in a given probe configuration called magnet centers"
"magnet centers can also be turned into a list"
pb = np.array(magnet_centers)
X = pb.random_sample((54, 2))
#27 probes in the cluster field, 54 magnets, 2 for 2D field plate and x,y coordinates 
tree = KDTree(X, k= 'some number where after that it switches to brute force')
tree.kernel_density(X[:1], h = , kernel = 'gaussian')
#h is band width 

"Once we have the densities, we are going to intergrate that with whether the magnet is being blocked or blocking another magnet"
"Check distances from n nearest neighbors, flag distances less than 5 mm (the pickup arm width)"
###It may be useful to have the available pick up axes of a magnet in the final code
#CIRCULAR MAGNET CAN BE PICKED UP RADIALLY
i = (x3, y3)
j = (x4, y4)
for i,j in circ_magnet_centers:
    leg_1 = (x4 -x3) - 7    #7mm is half the length of the pickup arm
    leg_2 = math.sqrt(r**2 - (leg_1)**2)
    center_circ of j = (s1, t1)
    point_magnet = (s1 + leg_1, t1 + leg_2)
    center_circ of i = (s2, t2)
    point_arm = (s2 + 7, t2 - .5*w)     # .5*w = 2.5 mm
    if point_arm(2) - point_magnet(2) > 0:
        "boolean flag: can be picked up along radial axis"
#CIRCULAR MAGNET CAN BE PICKED UP TANGENTIALLY 
    tan_leg = (x4 -x3) - r  #r = 6 mm
    if tan_leg > .5*w:      #.5*w = 2.5 mm 
        "boolean flag: can be picked up along tangential axis"
    if tan_leg > .5*w and (point_arm(2) - point_magnet(2) > 0):
        "boolean flag: can be picked up both radially and tangentially"
    if tan_leg < .5*w and (point_arm(2) - point_magnet(2) < 0):
        "boolean flag: can not be picked up radially nor tangentialy"
        #IF MAGNET CAN NOT BE PICKED UP TANGENTIALLY OR RADIALLY-> BLOCKED

#IF A CIRCULAR MAGNET IS BEING BLOCKED BY A CIRCULAR MAGNET
"pull two magnet centers from list/columns magnet_centers and find the distance between them"
for i,j in circ_magnet_centers
    if dist(i,j) - 2*r < 1 and  #set minimum distance to 13 mm, so 1 mm minimum between magnets
    #boolean flag
    if 

#IF A CIRCULAR MAGNET IS BLOCKING ANOTHER CIRCULAR MAGNET
"Same distances and equations for radial vs tangental pick up"
"BUT blocking magnet can still be picked up radially, tangentially, both, or neither"
"In the case of neither, the blocking magnet is also being blocked"
"To find blocking magnets, look at nearest neighbors, with in.5*w = 2.5 mm"
"If ONE of the n nearest neighbors with in 2.5 mm are BLOCKED, then the corresponding magnet is blocking"
"If there are multiple (1+) magnets in 2.5 mm that are BLOCKED, ????"


#THE ORDER
"Go to the magnet 1. in the list of magnets that are blocking other magnets and 2. with the highest kernel denstiy"
"clear all the magnets in that radius, then go to the blocking magnet with next high kernel density"
"repeat until all blocking magnets are cleared, then go in order of descending kernel density, clearing with in the set radius"
"repeat until all magnets are places/removed"
#Kernel density 

#COUNT BLOCKED
"if a magnet is blocked, how many magnets is it being blocked by. Count number of magnets in set radius"
"use center + 6"

#RECTANGULAR AND RECTANGULAR
i = (x1, y1) 
j = (x2, y2)
if dist(rect_center(i), rect_center(j)) is in [ 2*r, ((.5*L)^2 + (2*r +1)^2)^.5]
2*r = 12 mm 
((.5*L)^2 + (2*r +1)^2)^.5 = distance_limit = 16.40121947 mm
    print 'rectangular magnets are blocking eachother'
#WHEN RECTANGULAR MAGNETS ARE IN A 'T' FORMATION
if dist(rect_center(i), rect_center(j)) is in [16, 17] with either x1 = x2 or y1 = y2
    print 'T formation'
16 = (.5* L) + r 
17 = (.5* L) + r + 1 mm 
#IN THIS ARRANGEMENT, ONLY ONE MAGNET IS BLOCKED. THIS IS THE ONLY SCENARIO WHERE ONLY ONE RECTANGULAR MAGNET IS BLOCKED BUT NOT THE OTHER
"Need too add code to recognize which magnet is being blocked when in T formation"
if x1 = x2 ...
if y1 = y2 ...
#RECTANGULAR AND CIRCULAR 
"A rectangular magnet CAN be blocked by a single circular magnet but a circular magnet can NEVER be blocked by a single rectangular magnet"
"A circle magnet can only be blocked by a rectangular magnet if there are other magnets (circular or rectangular) with in exclusion radius"
#RECTANGULAR MAGNET IS BEING BLOCKED BY CIRCULAR
if dist(center_circ, rect_center) is in [12, 14.31782106]
    print 'rectangular magnet is blocked'
2*r = 12 mm
((2*r + 1)^2 + r^2)^.5 = 14.31782106

"Out of RECT-RECT, RECT-CIRC, and CIRC-CIRC, make on list that had all of the blocked magnets"
"From this list, take the kernel density and have pickup arm start with magnet with the highest kernel. Clearing all magnets with in a set radius and then moving to next highest kernel"
"Once all blocked magnets are cleared/placed, take kernel of remaining magnets OR go to magnets with the shortest distance from the origin to their center out, spiraling out from the plate"