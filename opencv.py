import cv2
import os
import numpy as np
import time

choice_ = ["hammer", "scissor", "paper"]
isContinue = True
path = "C:/Users/tatsa/Desktop/test_save_image/"
cap = cv2.VideoCapture(0)
h = 0
s = 0
p = 0
b = 0

def fight(human, bot):
    choice_ = ["hammer", "scissor", "paper"]
    for idx, c in enumerate(choice_):
        if human == c:
            human = idx
        if bot == c:
            bot = idx
    print(human - bot)
    if(human - bot == -1):
        return False
    return True

while isContinue:
    _, frame = cap.read()
    key = cv2.waitKey(1) & 0xFF
    if key == ord('h'): 
        h+=1
        cv2.imwrite(path + "hammer_" + str(h) + ".png", frame)

    elif key == ord('s'): 
        s+=1
        cv2.imwrite(path + "scissor_" + str(s) + ".png", frame)

    elif key == ord('p'): 
        p+=1
        cv2.imwrite(path + "paper_" + str(p) + ".png", frame)

    elif key == ord('b'): 
        b+=1
        cv2.imwrite(path + "blank_" + str(b) + ".png", frame)

    y = []
    D = []
    for fname in os.listdir(path):
        if ".png" in fname:
            x = cv2.imread(path + fname)
            y.append(fname.split("_")[0])
            D.append(np.sum((cv2.cvtColor(x, cv2.COLOR_BGR2GRAY) - cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))**2))

    if len(D) > 0:
        human = y[np.argmax(D)]
        bot = np.random.choice(choice_)
        cv2.putText(frame, human, (10, 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
        cv2.putText(frame, bot, (480, 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
        #print(y[np.argmax(D)])
        #isContinue = fight(human, bot)

    #if isContinue == False:
        #cv2.putText(frame, "Loss", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 4, (0, 0, 255))
        #time.sleep(3)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
