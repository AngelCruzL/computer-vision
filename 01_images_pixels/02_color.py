import cv2

image = cv2.imread('01_images_pixels/bird.jpg', cv2.IMREAD_COLOR)

print(image.shape)
print(image)

cv2.imshow('Computer Vision', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
