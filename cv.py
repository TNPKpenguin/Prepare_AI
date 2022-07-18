import cv2
import parinya

cap = cv2.VideoCapture(0)
yolo = parinya.YOLOv3('coco.names', 'yolov3.cfg', 'yolov3.weights')
while True:
    _, frame = cap.read()
    yolo.detect(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break