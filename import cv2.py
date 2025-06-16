import cv2
import mediapipe as mp
import numpy as np
import math
import os

# Initialize webcam
cap = cv2.VideoCapture(0)  # keep using iPhone cam

# Initialize Mediapipe Hand
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

# Volume range
minVol = 0
maxVol = 100  

def set_volume_mac(volume):
    volume = int(np.clip(volume, minVol, maxVol))
    os.system(f"osascript -e 'set volume output volume {volume}'")

while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []
    if results.multi_hand_landmarks:
        handLms = results.multi_hand_landmarks[0]
        for id, lm in enumerate(handLms.landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append((cx, cy))

        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        if len(lmList) >= 9:
            x1, y1 = lmList[4]   # Thumb tip
            x2, y2 = lmList[8]   # Index tip

            # Draw circle & line
            cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)

            length = math.hypot(x2 - x1, y2 - y1)

            # Map length to volume
            vol = np.interp(length, [20, 200], [minVol, maxVol])
            set_volume_mac(vol)

            # Volume bar
            bar = int(np.interp(length, [20, 200], [400, 150]))
            cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
            cv2.rectangle(img, (50, bar), (85, 400), (255, 0, 0), cv2.FILLED)
            cv2.putText(img, f'{int(vol)} %', (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Volume Controller", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

