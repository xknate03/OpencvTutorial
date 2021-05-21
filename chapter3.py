import cv2
import numpy as np

import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")
print(img.shape)

# resizing image ( width, height ) format
imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)

# cropping an image
# [height, width] format, where given a range
imgCropped = img[125:250, 0: 500]

cv2.imshow("Image", img)
# cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)

