import cv2
cap = cv2.VideoCapture(r"C:/Users/aadhy/Desktop/video.mp4")
delay = 30  
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Video Player", frame)
    key = cv2.waitKey(delay) & 0xFF
    if key == ord('+'):
        delay = max(1, delay - 5)  
        print("Playback Speed Increased")
    elif key == ord('-'):
        delay = delay + 5  
        print("Playback Speed Decreased")
    elif key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
