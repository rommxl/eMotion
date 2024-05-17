from django.shortcuts import render
from .models import Video
from .forms import UploadVideoForm
from keras.models import load_model
from django.http import JsonResponse
import numpy as np
import json
import cv2

model = load_model('fer50.h5')
face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_alt.xml')
result = { 'angry':0, 'disgust':0, 'fear':0, 'happy':0, 'neutral':0, 'sad':0, 'surprise':0 }

# Create your views here.
def get_emotion(img):
    categories = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
    img = np.expand_dims(img, axis=0)
    predictions = model.predict(img)
    predicted_class = np.argmax(predictions, axis=1)
    return categories[int(predicted_class)],str(np.max(predictions))

def upload_video(request):
    if request.method == 'POST':
        video = request.FILES.get('tobeanalyzed')       #handling sending file data
        file_path = 'media/video.mp4'                   #temp storage
        with open(file_path, 'wb') as destination:
            for chunk in video.chunks():
                destination.write(chunk)
        # upload_to_db = Video.objects.create(video_file = video)
        # upload_to_db.save()                    //removed db storage for temporary storage
        # return video
    
def predict(request):
    upload_video(request)
    vid = cv2.VideoCapture(r"media/video.mp4")
    while(True):
        ret, frame = vid.read()
        if not ret:
            break
        faces = face_cascade.detectMultiScale(frame)
        for x,y,w,h in faces:
            single_face = frame[y:y+h, x: x+w]
            resized_face = cv2.resize(single_face,(100,100))
            prediction = get_emotion(resized_face)
            result[prediction[0]]+=1
    vid.release()
    return JsonResponse(result)