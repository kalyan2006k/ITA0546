import cv2
import numpy as np
image = cv2.imread("C:/Users/aadhy/Desktop/images.jpg")
image = cv2.resize(image, (100, 100))
frame_width = 800
frame_height = 600
x = 100
y = 100
dx = 5
dy = 3
while True:
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    h, w = image.shape[:2]
    x += dx
    y += dy
    if x <= 0 or x + w >= frame_width:
        dx = -dx
    if y <= 0 or y + h >= frame_height:
        dy = -dy
    frame[y:y+h, x:x+w] = image
    cv2.imshow("Moving Image", frame)
    if cv2.waitKey(30) == 27:
        break
cv2.destroyAllWindows()
