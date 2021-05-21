import cv2
import numpy as np

# creating a matrix of 512 x 512 image, zeros means black
img = np.zeros((512, 512, 3), np.uint8)
print(img)
# makes the img  mustard color with format BGR
# img[] is similar to giving range in cropping

# img[:] = 86, 220, 254
# making lines format is line(src, (startX, startY), (untilX, untilY), lineColor, thickness)
# channel 1 = width, channel 2 = height
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
# creating rectangle almost similar to line, cv2.FILLED for solid color rectangle, else thickness of sides can be chosen
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)
# circle, need to pass img source, position, radius, color, and thickness
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
# putting text on images, scale is for size of font
cv2.putText(img, "OPENCV", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)

