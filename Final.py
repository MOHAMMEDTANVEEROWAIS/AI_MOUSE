import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy
import pyautogui


###################
wCam, hCam = 640, 480
frameR = 80  # Frame Reduction
smoothening = 7
###################

plocX, plocY = 0, 0
clocX, clocY = 0, 0

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
pTime = 0
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
# print(wScr, hScr)



while  True:

    # 1.Find the hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    # print(lmList)


    # 2.Get the tip of the index and Middle Fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        x4, y4 = lmList[4][1:]
        # print(x1,y1,x2,y2,x4,y4)

        # 3.Check Which fingers are up
        fingers = detector.fingersUp()
        # print(fingers)
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        # 4. Only Index Finger : Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:

            # 5.Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            # 6.Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # 7.Move Mouse
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY



        # 8.Both Index and Middle fingers are up : Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1:
            # 9. Find distance between Fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            print(length)
            # 10.Click mouse if distance is Short
            if length < 40 :
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()

        # 8.1.Both Index and Thumb fingers are up : Right Clicking Mode
        if fingers[0] == 1 and fingers[1] == 1:
            # 9. Find distance between Fingers
            length, img, lineInfo  = detector.findDistance(4, 8, img)
            print(length)
            # 10.Click mouse if distance is Short
            if length < 60 :
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (228, 246, 172), cv2.FILLED)
                # autopy.mouse.click()
                pyautogui.click(button='right')

        # 9. Find distance between Fingers
        # 10.Click mouse if distance is Short

    # 11.Frame Rate
    # cTIme = time.time()
    # fps = (1/(cTIme-pTime))
    # pTime = cTIme
    fps = cap.get(cv2.CAP_PROP_FPS)
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # 12.Display
    cv2.imshow("IMAGE", img)
    cv2.waitKey(1)


