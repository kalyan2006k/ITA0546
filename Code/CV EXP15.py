import cv2
import numpy as np

img=cv2.imread("C:/Users/aadhy/Desktop/images.jpg")

pts1=np.float32([[50,50],[200,50],[50,200],[200,200]])
pts2=np.float32([[100,100],[300,100],[100,300],[300,300]])

H=cv2.getPerspectiveTransform(pts1,pts2)

dst=cv2.warpPerspective(img,H,(500,500))

cv2.imshow("Original",img)
cv2.imshow("Transformed",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
