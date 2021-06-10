# python getting_pixels.py --image obama.jpg

# import the necessary packages
import argparse
from collections import defaultdict
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the image, grab its spatial dimensions (width and height),
# and then display the original image to our screen
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)



# images are simply NumPy arrays -- with the origin (0, 0) located at
# the top-left of the image
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# access the pixel located at x=100, y=5
(b, g, r) = image[5, 100]
print("Pixel at (100, 5) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# access the pixel at x= 100, y =50 and set it to blue
(b, g, r) = image[50, 100]
(b, g, r) = (255, 0, 0)
print("Pixel at (100, 50) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# compute the center of the image, which is simply the width and height
# divided by two
(cX, cY) = (w // 2, h // 2)
print ("the centre of the image is cX: {}, cY: {}".format(cX, cY))


cv2.waitKey(0)