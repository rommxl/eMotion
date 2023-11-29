from keras.models import load_model
import numpy as np
import cv2

model = load_model('fer50.h5')      #loading emotion recognizing model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')  #loading face detection model

def predict_class(img):     #passing face as argument
    categories = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
    img = np.expand_dims(img, axis=0)
    # img /= 255.0
    predictions = model.predict(img)       #using model to predict emotion in face that has been passed as argument
    predicted_class = np.argmax(predictions, axis=1)
    return categories[int(predicted_class)] +' '+ str(np.max(predictions))

vid = cv2.VideoCapture(0)
while(True):
    ret, frame = vid.read() #reading all frames of video
    frame = cv2.flip(frame,1)
    faces = face_cascade.detectMultiScale(frame)    #detect faces in given frame
    for x,y,w,h in faces:
        single_face = frame[y:y+h, x: x+w]
        resized_face = cv2.resize(single_face,(100,100))    #resizing face to appropriate dimensions
        cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0),1)
        cv2.putText(frame,predict_class(resized_face),(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),1) #writing emotion and confidence level on screen
    cv2.imshow('frame',frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

vid.release() 
cv2.destroyAllWindows() 