# USAGE
# python load_image_opencv.py --image obama.jpg --output car.jpg

# import the necessary packages
import argparse
from collections import defaultdict

import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("--image", required=True,
	help="path to input image")
ap.add_argument("--output", required=True,
	help="path to output image")
args = vars(ap.parse_args())

# load the image from disk via "cv2.imread" and then grab the spatial
# dimensions, including width, height, and number of channels
image = cv2.imread(args["image"])
output_image = cv2.imread(args["output"])
(h, w, c) = image.shape[:3]

# display the image width, height, and number of channels to our
# terminal
print("width: {} pixels".format(w))
print("height: {}  pixels".format(h))
print("channels: {}".format(c))

# show the image and wait for a keypress
cv2.imshow("Image", image)
# save the image back to disk (OpenCV handles converting image
# filetypes automatically)
cv2.imwrite("newimage1.jpg", output_image)

cv2.waitKey(0)

