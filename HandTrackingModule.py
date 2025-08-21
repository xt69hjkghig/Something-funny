import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands= 1, detectionCon=0.5, trackingCon= 0.5):
        self.mode = mode
        self.maxHands= maxHands
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,1,self.detectionCon,self.trackingCon)
        self.mpDraw = mp.solutions.drawing_utils
    def findHands(self,img,draw=True):
        results = self.hands.process(img)
        #print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                if draw:
                    mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS) 
        return img
    def findPosition(self, img):
        return None



                                        
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0


if __name__ == "__main__":
    cap = cv2.VideoCapture('https://192.168.7.107:8080/video')
    detector =handDetector()
    pTime = 0
    cTime = 0
    while cap.isOpened():
        success, img = cap.read()
        img = detector.findHands(img)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)