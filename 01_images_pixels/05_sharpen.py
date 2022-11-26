import cv2
import numpy as np
from utils.load_image import load_image

image_path = load_image('unsharp_bird.jpg')
original_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Sharpen kernel
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpen_image = cv2.filter2D(original_image, -1, kernel)

cv2.imshow('Original Image', original_image)
cv2.imshow('Sharpen Image', sharpen_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
