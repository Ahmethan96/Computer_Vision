import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    test = cap.read()
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    cv2.imshow("Frame", frame)
    ch = cv2.waitKey(1)
    # if ch & 0xFF == ord('q'):
    #     break
    print("the ret is ", type(ret))
    print("the frame is ", type(frame))


cap.release()
cv2.destroyAllWindows()
