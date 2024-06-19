import cv2 as cv

cam = 0
mirror = False

cap = cv.VideoCapture(cam)
while True:
    ret, frame = cap.read()
    if mirror:
        frame = cv.flip(frame, 1)
    cv.namedWindow('Webcam', cv.WINDOW_NORMAL)
    cv.setWindowProperty('Webcam', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    cv.imshow('Webcam', frame)
    if cv.waitKey(1) == 27:
        break

cv.destroyAllWindows('Webcam')