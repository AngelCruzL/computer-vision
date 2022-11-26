import cv2
from utils.load_image import load_image

image_path = load_image('bird.jpg')
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

print(image.shape)
print(image)

cv2.imshow('Computer Vision', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
