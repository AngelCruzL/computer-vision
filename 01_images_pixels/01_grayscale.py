import cv2

image = cv2.imread('01_images_pixels/camus.jpg', cv2.IMREAD_GRAYSCALE)

# On grayscale values close to 0 are black, values close to 255 are white
print(image)

cv2.imshow('Computer Vision', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
