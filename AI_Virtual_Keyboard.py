import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone
from pynput.keyboard import Controller

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

finalText = ""
keyboard = Controller()

# def drawAll(img, buttonList):
#
#     for button in buttonList:
#         x, y = button.pos
#         w, h = button.size
#         cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]), 20, rt=0)
#         cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
#         cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
#     return img


def drawAll(img, buttonList):
    imgNew = np.zeros_like(img, np.uint8)
    for button in buttonList:
        x, y = button.pos
        cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                          20, rt=0)
        cv2.rectangle(imgNew, button.pos, (x + button.size[0], y + button.size[1]),
                      (255, 0, 255), cv2.FILLED)
        cv2.putText(imgNew, button.text, (x + 40, y + 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

    out = img.copy()
    alpha = 0.5
    mask = imgNew.astype(bool)
    print(mask.shape)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
    return out


class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.text = text
        self.size = size

    # def draw(self, img):
    #     x,y = self.pos
    #     w,h = self.size
    #     cv2.rectangle(img, self.pos, (x+w, y+h), (255, 0, 255), cv2.FILLED)
    #     # cv2.rectangle(img, (100, 100), (200, 200), (255, 0, 255), cv2.FILLED)
    #     # cv2.putText(img, "Q", (120, 175), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    #     # cv2.putText(img, self.text, (self.pos[0]+25, self.pos[1]+25), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    #     cv2.putText(img, self.text, (x+20, y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
        # return img


buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

# buttonList.append(Button([100, 100], "Q"))
# for x in range(0,5):
#     buttonList.append(Button([100*x+50, 100], "Q"))

# myButton = Button([100, 100], "Q")
# myButton2 = Button([300, 100], "W")
# myButton3 = Button([400, 100], "E")

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bboxTnfo = detector.findPosition(img)
    img = drawAll(img, buttonList)

    if lmList:
        for button in buttonList:
            x, y = button.pos
            w,h = button.size

            if x < lmList[8][0] < x+w and y < lmList[8][1] < y+h:
                cv2.rectangle(img, (x-10,y-10), (x +w+ 10, y + h + 10), (175, 0, 175), cv2.FILLED)
                # cv2.rectangle(img, button.pos, (x + w, y + h), (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                l, _, _ = detector.findDistance(8, 12, img, draw=False)
                print(l)

                ## when clicked
                if l<50:
                    keyboard.press(button.text)
                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    finalText += button.text
                    sleep(0.5)
    cv2.rectangle(img, (50 , 350), (700, 430), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (60, 425), cv2.FONT_HERSHEY_PLAIN, 4, (255,255, 2555), 5)

    # for i in range(len(keys)):
    #     for j, key in enumerate(keys[i]):
    #         buttonList.append(Button([100 * j + 50, 100*i+50], key))

    # mybutton = Button([100, 100], "Q")

    # img = myButton.draw(img)
    # img = myButton2.draw(img)
    # img = myButton3.draw(img)


    cv2.imshow('Image', img)
    cv2.waitKey(1)

