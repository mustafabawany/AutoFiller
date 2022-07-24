from fastapi import FastAPI, Request, File , UploadFile
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles
from pdf2image import convert_from_path
# import requests
# from bs4 import BeautifulSoup
import pyrebase
import os
import cv2
# import PyPDF2
import matplotlib.pyplot as plt

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

templates = Jinja2Templates(directory= 'templates')
app.mount('/static', StaticFiles(directory= 'static'), name = 'static')

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
    # We can get resume from here and then process it
    resume = storage.child("Resume/" + resume_id + ".pdf").download('resume.pdf')
    # path = os.getcwd()
    images = convert_from_path('resume.pdf')    
    images[0].save('page0.jpeg' , 'JPEG')
    return {"Success" : "Yayy"}
    

@app.post("/auto-complete")    
async def getPDF(resume : UploadFile = File(...)):
    return {"resume" : resume}

@app.get("/success")
def successPage(request : Request):
    return {"Success" : "Yayyy!"}

@app.post("/success")
def getInfo(name: str , email : str , contact : str):
    return {"Success" : "Yayyy!!"}


