# -*- coding: utf-8 -*-
# by Leon Sering


import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np


##### Create a Repeating Image ####
print("1) Creating a Repeating Image")
# use a 80x80 image as tile image
xrepeats = 15 # number of dublications of the tile image in x-direction
yrepeats = 10 # number of dublications of the tile image in y-direction 

tile = imageio.imread('tile.png')
print("  tile image size:", tile.shape)
print("  repeats:", xrepeats, yrepeats)

eyedist = tile.shape[1] # = 80

# create one column by dublicating tile image in y-direction:
largeCol = tile

for i in range(1, yrepeats):
  largeCol = np.concatenate((largeCol,tile))

# create whole picture by dublicationg column in x-direction: 
large = largeCol
for j in range(1, xrepeats):
  large = np.concatenate((large, largeCol), axis = 1)
# large is now 1200x800

print("  large image size:", large.shape)



######## Load Hologram Image ########
print("2) Loading Hologram Image")
holo = imageio.imread('holo.png') # insert grey hologram image size as 'large', but one eyedist less in y-direction, 1120x600. (black = background, white = front)

maxshift = eyedist/4   # the value a pixil is shifted if a white pixil (nearest) appears: 20

holo = holo /255 * maxshift
holo = holo.astype(int) # there are know values between 0 (black) and 20 (white)

print("  maximal left shift (if hologram is white):", maxshift)



######## Insert Distraction ########
## Shift the initial image to achieve a straight line in the middle (not on the left side) (not working but not needed)
print("3) Inserting Distraction")
shifts = np.zeros(large.shape[0:2])

for i in range(0, holo.shape[0]):
  for j in range(0, holo.shape[1]):
    shifts[i,j+eyedist - holo[i,j,0]] = shifts[i,j]+holo[i,j,0]
middle = 600 #x value where the straight line appears
print("  shifting image at the shift values with column at x =", middle)

ultralarge = np.concatenate((large, largeCol, largeCol), axis = 1)
for i in range(0,holo.shape[0]):
  for j in range(0,holo.shape[1]):
      large[i,j] = ultralarge[i,j-int(shifts[i,middle+2*eyedist])]

print(" holo:", holo.shape)


######## Insert 3D Effect ########
print("4) Inserting 3D Effect")
for i in range(0, holo.shape[0]):
  for j in range(0, holo.shape[1]):
    large[i,j+eyedist - holo[i,j,0]] = large[i,j]


####### Save Image ########
print("5) Saving Image as 'large.png'")
imageio.imsave('magic_eye.png', large)

