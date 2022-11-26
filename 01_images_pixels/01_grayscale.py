import cv2
from utils.load_image import load_image

image_path = load_image('camus.jpg')
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# On grayscale values close to 0 are black, values close to 255 are white
print(image)

cv2.imshow('Computer Vision', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
