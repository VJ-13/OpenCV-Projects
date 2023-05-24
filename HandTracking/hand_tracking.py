import cv2 as cv
import numpy as np
import mediapipe as mp
import time 


capture = cv.VideoCapture(0)
capture.set(3, 640)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Frame Rate
pTime = 0
cTime = 0


while True:
    isTrue, frame = capture.read()
    
    imgRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                # Convert to pixel values
                h,w,c = frame.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id==0:
                    cv.circle(frame, (cx,cy), 25, (255,0,255), cv.FILLED)
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)


    # Frame Rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(frame, "FPS " + str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (255,255,255), 3)

    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break




capture.release()
cv.destroyAllWindows()

