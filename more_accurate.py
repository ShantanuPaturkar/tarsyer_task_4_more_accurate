from importlib.resources import path
from re import S, T
# from tkinter import font
import cv2
import mediapipe as mp


#for capturing video and increase size
cap = cv2.VideoCapture(0)
cap.set(3, 1280)# increase size of o/p screen
cap.set(4, 720)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
thicknes=2
# out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width , frame_height))
# out = cv2.VideoWriter('Demo.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (3,4))

#hands detection

while True:
    
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
    
    thickness=2
#   checking whether a hand is detected   
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: # working with each hand
            for id, lm in enumerate(handLms.landmark): #The second for loop helps us get the hand landmark information which will give us the x and y coordinates of each listed point in the hand landmark diagram. This loop will also give us the id of each point.
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
           
                #getting 'y 'co-ordinates of each finger tip
                # middle_fingure_mcp=[] 
                # if id==9:
                #     # middle_fingure_mcp=[]
                #     middle_fingure_mcp.append(cy)
                #     k=middle_fingure_mcp[-1]

                if id == 3:
                    thumb_low = []
                    # thumb_lowX=[]
                    thumb_low.append(cy)
                    # thumb_lowX.append(cx)
                    Tl=thumb_low[-1]
                    # TlX=thumb_lowX[-1]

                if id == 4:
                    thumb = []
                    thumb.append(cy)
                    T=thumb[-1]
                    if T<Tl-25:
                        S='T'
                        cv2.circle(image, (cx, cy), 20 , (255,255 ,0), cv2.FILLED) 
                        cv2.putText(image, S, (cx, cy), fontFace=3, fontScale= 1 ,color=(1, 0,0))
                       

                if id == 8:
                    index = []
                    index.append(cy)
                    I=index[-1]
                    if I<Il :
                        S='I'
                        cv2.circle(image, (cx, cy), 20 , (255,255 ,0), cv2.FILLED) 
                        cv2.putText(image, S, (cx, cy), fontFace=3, fontScale= 1 ,color=(1, 0,0))
                        
                if id == 7:
                    index_low = []
                    index_low.append(cy)
                    Il=index_low[-1]




                if id == 12:
                    middle = []
                    middle.append(cy)
                    M=middle[-1]
                    if M<Ml :
                        S='M'
                        cv2.circle(image, (cx, cy), 20 , (255,255 ,0), cv2.FILLED) 
                        cv2.putText(image, S, (cx, cy), fontFace=3, fontScale= 1 ,color=(1, 0,0))
                        
                if id == 11:
                    middle_low = []
                    middle_low.append(cy)
                    Ml=middle_low[-1]



                if id == 16:
                    Ring = []
                    Ring.append(cy)
                    R=Ring[-1]
                    if R<Rl :
                        S='R' 
                        cv2.circle(image, (cx, cy), 20 , (255,255 ,0), cv2.FILLED)
                        cv2.putText(image, S, (cx, cy), fontFace=3, fontScale= 1 ,color=(1, 0,0))
                        
                if id == 15:
                    Ring_low = []
                    Ring_low.append(cy)
                    Rl=Ring_low[-1]



                if id == 19:
                    baby_low = []
                    baby_low.append(cy)
                    Bl=baby_low[-1]
                    
                if id == 20:
                    baby = []
                    baby.append(cy)
                    B=baby[-1]
                    if B<Bl :
                        S='B'
                        cv2.circle(image, (cx, cy), 20 , (255,255 ,0), cv2.FILLED) 
                        cv2.putText(image, S, (cx, cy), fontFace=3, fontScale= 1 ,color=(1, 0,0))
                        
              
                    

                    


            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
            
#displaying output
    cv2.imshow("Output", image)
    if cv2.waitKey(1) == ord(' '): #space to return from the window
        cv2.imwrite('detected finger.jpg', image)

        cap.release()
        exit()