import cv2
import sys
import vlc
from fastai.vision import *

model = load_learner(path='.', file='export.pkl')
face_cascade = cv2.CascadeClassifier('face.xml')
sound_path = './police.mp3'
sound = vlc.MediaPlayer(sound_path)
sound_playing = False
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960) #1280, 640
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 544) #720, 480
    
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5) #detect faces
    no_masks = []
    for (x,y,w,h) in faces:
        sub_img = gray[y:y+h, x:x+w] #take part of image that contains the face only
        cv2.imwrite('to_be_deleted.jpg', sub_img) #save part of image that contains the face only
        img = open_image('to_be_deleted.jpg') #load face image for prediction
        pred = model.predict(img) # predict
        no_mask = pred[0].data.item() == 0
        no_masks.append(no_mask)
        mask_label = 'No Mask! :(' if no_mask else 'Mask ON :)'
        color = (0, 0, 255) if no_mask else (0, 255, 0)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 3) #draw box around detected face
        cv2.putText(img=frame, text=mask_label, org=(x,y-10), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=color)
    #check if at least one person is not wearing a mask. If so, play alert sound!
    if any(no_masks):
        if sound_playing == False:
            sound_playing = True
            sound.play()
    else:
        if sound_playing == True:
            sound_playing = False
            sound.stop()
        
    cv2.imshow('Driver_frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()