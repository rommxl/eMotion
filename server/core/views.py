from django.shortcuts import render
from .models import Video
from .forms import UploadVideoForm
from keras.models import load_model
from django.http import HttpResponse
import numpy as np
import cv2

model = load_model('fer50.h5')
face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_alt.xml')

# Create your views here.
def get_emotion(img):
    categories = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
    img = np.expand_dims(img, axis=0)
    predictions = model.predict(img)
    predicted_class = np.argmax(predictions, axis=1)
    return categories[int(predicted_class)] +' '+ str(np.max(predictions))

def upload_video(request):
    submitted = False
    if request.method == 'POST':
        print(request.FILES.get('tobeanalyzed'))
        # form = UploadVideoForm(request.POST, request.FILE)
        # file = request.FILE
        # if form.is_valid():
        #     uploaded_vid = form.save(commit=False)
        #     uploaded_vid.save()
        video = request.FILES.get('tobeanalyzed')
        upload_to_db = Video.objects.create(video_file = video)
        upload_to_db.save()
        return HttpResponse("Uploaded")
def predict(request):
    upload_video(request)
    