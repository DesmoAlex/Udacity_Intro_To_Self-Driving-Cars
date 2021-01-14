import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import cv2

# Read in the image
image = mpimg.imread('images/car_green_screen2.jpg')

# Define our color selection boundaries in RGB values
lower_green = np.array([0,180,0]) 
upper_green = np.array([100,255,100])

# Define the masked area
mask = cv2.inRange(image, lower_green, upper_green)

# Mask the image to let the car show through
masked_image = np.copy(image)

masked_image[mask != 0] = [0, 0, 0]

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# HSV channels
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

# Visualize the individual color channels
f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20,10))
ax1.set_title('H channel')
ax1.imshow(h, cmap='gray')
ax2.set_title('S channel')
ax2.imshow(s, cmap='gray')
ax3.set_title('V channel')
ax3.imshow(v, cmap='gray')
plt.show()

## TODO: Define the color selection boundaries in HSV values
lower_h = np.array([10, 0, 0])
upper_h = np.array([100,255,255])

mask = cv2.inRange(image, lower_h, upper_h)

## TODO: Define the masked area and mask the image
# Don't forget to make a copy of the original image to manipulate
masked_image = np.copy(image)

masked_image[mask != 0] = [0, 0, 0]

f1, (hsv1, hsv2) = plt.subplots(1, 2, figsize=(20,10))
hsv1.set_title('Original')
hsv1.imshow(image)
hsv2.set_title('H-Channel')
hsv2.imshow(masked_image)
plt.show()
