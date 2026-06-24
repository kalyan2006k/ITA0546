import cv2
import numpy as np

img=cv2.imread("C:/Users/aadhy/Desktop/images.jpg")

pts_src=np.float32([[141,131],[480,159],[493,630],[64,601]])

pts_dst=np.float32([[0,0],[500,0],[500,700],[0,700]])

matrix=cv2.getPerspectiveTransform(pts_src,pts_dst)

result=cv2.warpPerspective(img,matrix,(500,700))

cv2.imshow("Original",img)
cv2.imshow("Perspective Corrected",result)

cv2.waitKey(0)
cv2.destroyAllWindows()
