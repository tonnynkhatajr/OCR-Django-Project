import base64
import os
import numpy as np
import re
#import mysql.connector
import pytesseract
from django.contrib import messages
from django.shortcuts import render
from PIL import Image
from ocr.models import RecInsert


# you have to install tesseract module too from here - https://github.com/UB-Mannheim/tesseract/wiki
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Path to tesseract.exe
)
def Insertrecord(request):
    if request.method == "POST":
        if request.POST.get('fname') and request.POST.get('age') and request.POST.get('gender') and request.POST.get('dateofentry'):
            saverecord=RecInsert()
            saverecord.fname=request.POST.get('fname')
            saverecord.age=request.POST.get('age')
            saverecord.gender=request.POST.get('gender')
            saverecord.dateofentry=request.POST.get('dateofentry')
            saverecord.save()
            messages.success(request,'Record Saved Successfully...')
            return render(request,'home.html')
    else:
            return render(request,'home.html')
       



def homepage(request):
    if request.method == "POST":
        try:
            image = request.FILES["imagefile"]
            # encode image to base64 string
            image_base64 = base64.b64encode(image.read()).decode("utf-8")
        except:
            messages.add_message(
                request, messages.ERROR, "No image selected or uploaded"
            )
            return render(request, "home.html")
        lang = request.POST["language"]
        img = np.array(Image.open(image))
        text = pytesseract.image_to_string(img, lang=lang)
        
        text_list = text.split('\n')
        fname = ''
        age = ''
        gender = ''
        dateofentry =''
        for i in text_list:
            if 'Name' in i:
                fname = i.split(':')[1].strip()
            elif 'Age' in i:
                age = i.split(':')[1].strip()
            elif 'Gender' in i:
                gender = i.split(':')[1].strip()
            elif 'Date of Entry' in i:
                dateofentry = i.split(':')[1].strip()

                
        return render(request, 'home.html', {'fname': fname, 'age': age, 'gender': gender, 'dateofentry' : dateofentry})
    return render(request, 'home.html')


