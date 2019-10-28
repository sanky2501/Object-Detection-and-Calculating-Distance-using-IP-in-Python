import cv2
import numpy as np

cap = cv2.VideoCapture(0)#put the value as 0 if you are using webcam else put 1 for any external camera and put location if you are using video

while True:
    ret, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    lower = np.array([90, 120, 76]) #put the low values of hsv of the color of object you wanna detect
    upper = np.array([154, 255, 255]) #put the high values of hsv of the color of object you wanna detect
    mask = cv2.inRange(hsv, lower, upper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    ans=0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area>2000: #adjust area according to threshold
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 2)
            ans=55+(abs(12150-area)/212.3)#blue bottle
            #ans=40+(abs(2550-area)/61.11)#pink ball
            #ans=30+(abs(25350-area)/940)#yellow wall
            print(area)
    cv2.putText(frame,'%.2fcm' % ans, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2, cv2.LINE_AA)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
