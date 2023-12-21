import cv2
import mediapipe as mp
import numpy as np

handsDetector = mp.solutions.hands.Hands()
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
        break
    flipped = np.fliplr(frame)
    flippedRGB = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)
    results = handsDetector.process(flippedRGB)
    if results.multi_hand_landmarks is not None:
        x_tip = int(results.multi_hand_landmarks[0].landmark[4].x *
                     flippedRGB.shape[1])
        y_tip = int(results.multi_hand_landmarks[0].landmark[4].y *
                     flippedRGB.shape[0])
        x1_tip = int(results.multi_hand_landmarks[0].landmark[8].x *
                flippedRGB.shape[1])
        y1_tip = int(results.multi_hand_landmarks[0].landmark[8].y *
                flippedRGB.shape[0])
        x2_tip = int(results.multi_hand_landmarks[0].landmark[12].x *
                    flippedRGB.shape[1])
        y2_tip = int(results.multi_hand_landmarks[0].landmark[12].y *
                    flippedRGB.shape[0])
        x3_tip = int(results.multi_hand_landmarks[0].landmark[16].x *
                    flippedRGB.shape[1])
        y3_tip = int(results.multi_hand_landmarks[0].landmark[16].y *
                    flippedRGB.shape[0])
        x4_tip = int(results.multi_hand_landmarks[0].landmark[20].x *
                     flippedRGB.shape[1])
        y4_tip = int(results.multi_hand_landmarks[0].landmark[20].y *
                     flippedRGB.shape[0])
        cv2.circle(flippedRGB,(x_tip, y_tip), 10, (255, 0, 0), -1)
        cv2.circle(flippedRGB, (x1_tip, y1_tip), 10, (0, 255, 0), -1)
        cv2.circle(flippedRGB, (x2_tip, y2_tip), 10, (0, 0, 255), -1)
        cv2.circle(flippedRGB, (x3_tip, y3_tip), 10, (0, 0, 0), -1)
        cv2.circle(flippedRGB, (x4_tip, y4_tip), 10, (255, 255, 255), -1)
        print(f"Большой: {x_tip, y_tip};", f"Указательный: {x1_tip, y1_tip};", f"Средний: {x2_tip, y2_tip};", f"Безымянный: {x3_tip, y3_tip};", f"Мизинец: {x4_tip, y4_tip}")
        if (abs(y_tip-y1_tip) < 20 and abs(y1_tip-y2_tip) < 20 and abs(y2_tip-y3_tip) < 20 and abs(y3_tip-y4_tip) < 20):
            if (abs(x2_tip-x_tip) > abs(x1_tip-x_tip)):
                print('A')
                cv2.putText(flippedRGB, 'LETTER: A', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
            else:
                print('E')
                cv2.putText(flippedRGB, 'LETTER: E', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
        elif (abs(x_tip-x4_tip) < 310 and abs(y_tip-y4_tip) < 120 and abs(x_tip-x4_tip) > 110):
            print('Y')
            cv2.putText(flippedRGB, 'LETTER: Y', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
        elif (abs(x1_tip-x2_tip) < 30 and abs(x3_tip-x2_tip) < 30 and abs(y3_tip-y2_tip) < 20 and y1_tip > 250 and y2_tip > 250 and y4_tip < y1_tip):
            print('M')
            cv2.putText(flippedRGB, 'LETTER: M', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
        elif (abs(x1_tip-x2_tip) < 30 and y1_tip < 250 and y2_tip < 250 and y4_tip > y1_tip):
            print('U')
            cv2.putText(flippedRGB, 'LETTER: U', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
        elif (abs(x1_tip-x2_tip) < 30 and y1_tip > 250 and y2_tip > 250 and y4_tip < y1_tip):
            print('N')
            cv2.putText(flippedRGB, 'LETTER: N', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
        elif (y4_tip < y1_tip):
            print("I")
            cv2.putText(flippedRGB, 'LETTER: I', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
        elif (abs(x1_tip-x3_tip) < 135 and abs(y3_tip-y1_tip) < 30):
            print('W')
            cv2.putText(flippedRGB, 'LETTER: W', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
        elif (abs(y_tip-y1_tip) < 70 and abs(y_tip-y2_tip) < 80 and abs(x1_tip-x2_tip) > 50 and abs(x_tip-x1_tip) < 40):
            print('K')
            cv2.putText(flippedRGB, 'LETTER: K', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
        elif (abs(x1_tip-x2_tip) > 50):
            print('V')
            cv2.putText(flippedRGB, 'LETTER: V', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
        else:
            print('NO')
            cv2.putText(flippedRGB, 'LETTER: NO LETTERS', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
    else:
        print('NO')
        cv2.putText(flippedRGB, 'LETTER: NO LETTERS', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))

    res_image = cv2.cvtColor(flippedRGB, cv2.COLOR_RGB2BGR)
    cv2.imshow("English", res_image)

handsDetector.close()