from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles
from pdf2image import convert_from_path
import pyrebase
import cv2

import sys 
sys.path.insert(0, 'backend/')
from PreProcessing import *
from TextExtraction import *


app = FastAPI()

firebaseConfig = {

    "apiKey": "AIzaSyDradRFBuygrz3wUYnF22DrR_OrLyMcJB4",

    "authDomain": "autofiller-6f0cc.firebaseapp.com",

    "databaseURL": "https://autofiller-6f0cc-default-rtdb.firebaseio.com",

    "projectId": "autofiller-6f0cc",

    "storageBucket": "autofiller-6f0cc.appspot.com",

    "messagingSenderId": "398218048520",

    "appId": "1:398218048520:web:2095feb70bd4ff07610dbd"
}

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

templates = Jinja2Templates(directory= 'frontend/templates')
app.mount('/static', StaticFiles(directory= 'frontend/static'), name = 'static')

@app.get("/")
def getHome(request : Request):
    return templates.TemplateResponse("homepage.html" , {"request" : request})

@app.get("/about-us")
def getAboutUs(request : Request):
    return templates.TemplateResponse("about.html" , {"request":request})

@app.get("/auto-complete")
def getAutocomplete(request : Request):
    return templates.TemplateResponse("autocomplete.html" , {"request":request})

@app.get("/auto-complete/{resume_id}")
async def ProcessResume(resume_id: str , request : Request):
    
    # Extracting PDF from Firebase Storage
    resume = storage.child("Resume/" + resume_id + ".pdf").download('backend/Resume/resume.pdf')
    images = convert_from_path('backend/Resume/resume.pdf')    
    images[0].save('backend/Resume/page0.jpeg' , 'JPEG')
    
    preprocessing = PreProcessing()
    text_extraction = TextExtraction()

    img = cv2.imread('backend/Resume/page0.jpeg')
    img = preprocessing.ZoomImage(img , 3)
    img = preprocessing.GrayScaleImage(img)
    img = preprocessing.CropImage(img)
    img = preprocessing.InvertImage(img)
    
    preprocessing.SaveImage(img, "preprocessed")
    img = preprocessing.ReadImage("preprocessed")
    
    boundedImg = preprocessing.CreateBoundingBox(img)

    preprocessing.SaveImage(boundedImg, "bounded")
    img = preprocessing.ReadImage("preprocessed")

    text = text_extraction.ExtractText(img)
    personName = text_extraction.extract_name(text.title())
    personName = personName.replace("\n" , "")
    contactNum = text_extraction.extract_phone_number(text.lower())
    emailID = text_extraction.extract_emails(text.lower())
    emailID = text_extraction.process_emails(emailID)

    if emailID == list:
        return templates.TemplateResponse('parsedResume.html' , {
            'request' : request,
            'name' : personName,
            'email' : emailID[0],
            'contact': contactNum
        })
    else:
        return templates.TemplateResponse('parsedResume.html' , {
            'request' : request,
            'name' : personName,
            'email' : emailID[0],
            'contact': contactNum
        })

@app.get("/success")
def setSuccess(request : Request):
    return templates.TemplateResponse("success.html" , {"request":request})