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
last_play_time=0
#cooldown=0.4
cv2.namedWindow("live-instruments", cv2.WINDOW_NORMAL)
cv2.resizeWindow("live-instruments", 1200, 800)
while True:
    success,frames=cap.read()
    
    if not success:
        print("vedio capture failed")
        break
    drumbox=(50,50,150,150)
    guitarbox=(220,50,320,150)
    pianobox=(390,50,490,150)
    trumpetbox=(560,50,660,150)
    cv2.rectangle(frames,(drumbox[0],drumbox[1]),(drumbox[2],drumbox[3]),(0,255,0),-1)
    cv2.rectangle(frames,(guitarbox[0],guitarbox[1]),(guitarbox[2],guitarbox[3]),(255,0,0),-1)
    cv2.rectangle(frames,(pianobox[0],pianobox[1]),(pianobox[2],pianobox[3]),(0,0,255),-1)
    cv2.rectangle(frames,(trumpetbox[0],trumpetbox[1]),(trumpetbox[2],trumpetbox[3]),(0,255,255),-1)
    cv2.putText(frames,"DRUMS",(65,110),cv2.FONT_ITALIC,0.7,(255,255,255),2)
    cv2.putText(frames,"GUITAR",(225,110),cv2.FONT_ITALIC,0.7,(255,255,255),2)
    cv2.putText(frames,"PIANO",(405,110),cv2.FONT_ITALIC,0.7,(255,255,255),2)
    cv2.putText(frames,"TRUMPET",(520,110),cv2.FONT_ITALIC,0.7,(0,0,0),2)
    h,w,_=frames.shape
    rgb = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
  
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frames,
                hand_landmarks,
                mp_hand.HAND_CONNECTIONS
            )
            indexup=hand_landmarks.landmark[8].y<hand_landmarks.landmark[6].y
            middle_down=hand_landmarks.landmark[12].y>hand_landmarks.landmark[10].y
            ringdown=hand_landmarks.landmark[16].y>hand_landmarks.landmark[14].y
            pinkydown=hand_landmarks.landmark[20].y>hand_landmarks.landmark[18].y
            pointing=indexup and middle_down and ringdown and pinkydown
            x=int(hand_landmarks.landmark[8].x*w)
            y=int(hand_landmarks.landmark[8].y*h)
            cv2.circle(frames,(x,y),10,(255,255,255),-1)
            current_time=time.time()
            if not pointing:
                drums.stop()
                guitar.stop()
                piano.stop()
                trumpet.stop()
                continue
            if  pointing:
                if drumbox[0]<x<drumbox[2] and drumbox[1]<y<drumbox[3]:
                    drums.play()
                    #last_play_time=current_time
                elif guitarbox[0]<x<guitarbox[2] and guitarbox[1]<y<guitarbox[3]:
                    guitar.play()
                    #last_play_time=current_time
                elif pianobox[0]<x<pianobox[2] and pianobox[1]<y<pianobox[3]:
                    piano.play()
                    #last_play_time=current_time
                elif trumpetbox[0]<x<trumpetbox[2] and trumpetbox[1]<y<trumpetbox[3]:
                    trumpet.play()
                    #last_play_time=current_time
    
    cv2.imshow("live-instruments",frames)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

