import cv2
import pyautogui

pyautogui.FAILSAFE = False

from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1)

cap = cv2.VideoCapture(0)

w, h = pyautogui.size()

i1_p, i2_p = 0, 0
i1_c, i2_c = 0, 0

while True:
    mp_x, mp_y = pyautogui.position()
    success, img = cap.read()
    hands, img = detector.findHands(img, draw=True, flipType=True)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        i1_p, i2_p = i1_c, i2_c
        i1_c, i2_c = lmList[8][0:2]

        m1, m2 = lmList[12][0:2]

        fingers = detector.fingersUp(hand)
        cv2.circle(img, (i1_c, i2_c), 10, (255, 0, 255), cv2.FILLED)

        if fingers == [0, 1, 0, 0, 0]:
            x = (i1_c - i1_p) * (-10)
            y = (i2_c - i2_p) * 10
            pyautogui.move(x, y)

        elif fingers == [0, 1, 1, 0, 0]:
            pyautogui.click()


    cv2.imshow("Mouse", img)
    cv2.waitKey(1)
