import cv2
import numpy as np

original_image = cv2.imread('01_images_pixels/bird.jpg', cv2.IMREAD_COLOR)

# To normalize the array we need to divide the 25 items by themselves
kernel = np.ones((5, 5)) / 25

# -1 "destination depth"
blur_image = cv2.filter2D(original_image, -1, kernel)


# Gaussian blur is used to reduce noise
cv2.imshow('Original Image', original_image)
cv2.imshow('Blurred Image', blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
