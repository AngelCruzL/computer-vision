import cv2
import numpy as np

original_image = cv2.imread('01_images_pixels/bird.jpg', cv2.IMREAD_COLOR)

# We have to transform the image into grayscale
# OpenCV handles BGR instead RGB
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Laplacian kernel
kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
result_image = cv2.filter2D(gray_image, -1, kernel)

# Also we can use the function cv2.Laplacian
result_image2 = cv2.Laplacian(gray_image, -1)

# Gaussian blur is used to reduce noise
cv2.imshow('Original Image', gray_image)
cv2.imshow('Result Image', result_image)
cv2.imshow('Result Image 2', result_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
