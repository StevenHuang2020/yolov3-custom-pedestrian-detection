import numpy as np
import cv2
from yolo_opencv import detectionImg,getCalsses

def InitNet():
    if 1:
        #weights=r'./darknet-master/trainPennFudan/backupTiny/PF_yolov3-tiny_170000.weights'
        weights=r'./PF_yolov3-tiny_FinalEx.weights'
        config=r'./PF_yolov3-tiny.cfg'
        classFile = r'./PennFudan.names'
    else:
        weights=r'yolov3.weights'
        config=r'yolov3.cfg'
        classFile = r'yolov3.txt'
    
    return getCalsses(classFile), cv2.dnn.readNet(weights, config)

def showCamera():
    classes,net  = InitNet()
    #colors = [200,0,0]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
     
    saveVideo=False
    
    #fourcc = cv2.VideoWriter.fourcc('X','2','6','4')
    #fourcc = cv2.VideoWriter.fourcc('v','p','8','0')
    fourcc = cv2.VideoWriter.fourcc('M','J','P','G')
    out = cv2.VideoWriter('output2.mp4', fourcc, 25.0, (640,480))
    cap = cv2.VideoCapture(0)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print('fps=',fps)
    while(True):
        ret, frame = cap.read()
        #Our operations on the frame come here
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Display the resulting frame
        
        frame = detectionImg(frame,net,classes,colors)
        if saveVideo:
            out.write(frame)
            
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    
def main():
    showCamera()
    
if __name__=='__main__':
    main()
    