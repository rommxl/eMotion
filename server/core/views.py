from django.shortcuts import render
from .models import Video
from .forms import UploadFileForm
from keras.models import load_model
import numpy as np
import cv2

model = load_model('fer50.h5')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# Create your views here.
def get_emotion(img):
    categories = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
    img = np.expand_dims(img, axis=0)
    predictions = model.predict(img)
    predicted_class = np.argmax(predictions, axis=1)
    return categories[int(predicted_class)] +' '+ str(np.max(predictions))

def upload_video(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILE)
        file = request.FILE

        upload_to_db = Video.objects.create(video_file = file)
        upload_to_db.save()

def predict(request):
    print('hi')