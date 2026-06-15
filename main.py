import cv2
import mediapipe as mp
import pygame
import time
cap=cv2.VideoCapture(0)
pygame.mixer.init()
drums=pygame.mixer.Sound("music/drums.mp3")
guitar=pygame.mixer.Sound("music/guitar.mp3")
trumpet=pygame.mixer.Sound("music/trumpet.mp3")
piano=pygame.mixer.Sound("music/piano.mp3")
mp_hand=mp.solutions.hands
hands=mp_hand.Hands(static_image_mode=False,
                    max_num_hands=1,
                    min_detection_confidence=0.7,
                    min_tracking_confidence=0.7)
mp_draw=mp.solutions.drawing_utils
while True:
    success,frames=cap.read()
    
    if not success:
        print("vedio capture failed")
        break
    results = hands.process(frames)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frames,
                hand_landmarks,
                mp_hand.HAND_CONNECTIONS
            )
    cv2.imshow("live-instruments",frames)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

