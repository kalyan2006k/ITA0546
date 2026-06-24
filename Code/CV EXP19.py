import cv2
import numpy as np

image = cv2.imread("C:/Users/aadhy/Desktop/images.jpg")

if image is None:
    print("Error: Image not found.")
else:
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    abs_sobel_x = np.abs(sobel_x)
    sobel_x = np.uint8(abs_sobel_x)

    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    abs_sobel_y = np.abs(sobel_y)
    sobel_y = np.uint8(abs_sobel_y)

    edge_image = cv2.bitwise_or(sobel_x, sobel_y)

    cv2.imshow('Original Image', image)
    cv2.imshow('Edge-Detected Image', edge_image)

    cv2.imwrite('edge_detected_image.jpg', edge_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
