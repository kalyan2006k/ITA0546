import cv2
import numpy as np
image = cv2.imread("C:/Users/aadhy/Desktop/images.jpg")
rows, cols = image.shape[:2]
tx = 100   
ty = 35    
M = np.float32([[1, 0, tx],
                [0, 1, ty]])
translated = cv2.warpAffine(image, M, (cols, rows))
cv2.imshow("Original Image", image)
cv2.imshow("Translated Image", translated)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
