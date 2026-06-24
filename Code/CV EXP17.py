import cv2
import numpy as np

image = cv2.imread("C:/Users/aadhy/Desktop/images.jpg")

if image is None:
    print("Error: Image not found.")
else:
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_x = np.absolute(sobel_x)
    sobel_x = np.uint8(sobel_x)

    cv2.imshow('Original Image', image)
    cv2.imshow('Sobel X Edge Detection', sobel_x)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
