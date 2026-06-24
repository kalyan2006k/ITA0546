import cv2
image=cv2.imread("C:/Users/aadhy/Desktop/images.jpg")
rotated=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Original image',image)
cv2.imshow('Rotated image',rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
