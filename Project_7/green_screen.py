#%matplotlib inline

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import cv2


# Read in the image
image = mpimg.imread('images/car_green_screen.jpg')

# Print out the image dimensions (height, width, and depth (color))
print('Image dimensions:', image.shape)

# Display the image
plt.imshow(image)

# Define our color selection boundaries in RGB values
lower_green = np.array([0,180,0]) 
upper_green = np.array([100,255,100])

# Define the masked area
mask = cv2.inRange(image, lower_green, upper_green)

# Vizualize the mask
plt.imshow(mask, cmap='gray')

# Mask the image to let the car show through
masked_image = np.copy(image)

masked_image[mask != 0] = [0, 0, 0]

# Display it!
plt.imshow(masked_image)
plt.show()

# Load in a background image, and convert it to RGB 
background_image = mpimg.imread('images/sky.jpg')

## TODO: Crop it or resize the background to be the right size (450x660)
# Hint: Make sure the dimensions are in the correct order!
# Make a copy of the image to manipulate
image_crop = np.copy(background_image)

# Define how many pixels to slice off the sides of the original image
row_crop_top = 65
row_crop_bot = 60
col_crop = 182

# Using image slicing, subtract the row_crop from top/bottom and col_crop from left/right
image_crop = background_image[row_crop_top:-row_crop_bot, col_crop:-col_crop, :]

print('Image dimensions: ',image_crop.shape)
## TODO: Mask the cropped background so that the car area is blocked
# Hint: mask the opposite area of the previous image

crop_background = np.copy(image_crop)

crop_background[mask == 0] = [0, 0, 0]

## TODO: Display the background and make sure 
plt.imshow(crop_background)
plt.show()

## TODO: Add the two images together to create a complete image!
# complete_image = masked_image + crop_background
new_image = cv2.add(masked_image, crop_background)
plt.imshow(new_image)
plt.show()