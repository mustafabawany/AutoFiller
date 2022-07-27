import cv2
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles
from pdf2image import convert_from_path
import firebase_admin
from firebase_admin import credentials , storage , initialize_app
import sys 
sys.path.insert(0, 'backend/')
from PreProcessing import *
from TextExtraction import *

#Assigning Firebase Credentials
cred = credentials.Certificate("./key.json")
initialize_app(cred , {'storageBucket' : 'autofiller-6f0cc.appspot.com'}) 

app = FastAPI()

#Fetching Firebase Storage Bucket
bucket = storage.bucket()

#Assigning frontend/templates directory as Jinja Templates
templates = Jinja2Templates(directory= 'frontend/templates')

#Assigning static directory as static to execute CSS 
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
    
    resume = bucket.get_blob("Resume/" + resume_id + ".pdf").download_to_filename('backend/Resume/resume.pdf')
    images = convert_from_path('backend/Resume/resume.pdf')    
    images[0].save('backend/Resume/page0.jpeg' , 'JPEG')
    
    
    preprocessing = PreProcessing()
    text_extraction = TextExtraction()

    # Image Pre Processing Phase
    img = cv2.imread('backend/Resume/page0.jpeg')
    img = preprocessing.ZoomImage(img , 3)
    img = preprocessing.GrayScaleImage(img)
    img = preprocessing.CropImage(img)
    img = preprocessing.InvertImage(img)
    
    preprocessing.SaveImage(img, "preprocessed")
    img = preprocessing.ReadImage("preprocessed")
    
    # boundedImg = preprocessing.CreateBoundingBox(img)

    # preprocessing.SaveImage(boundedImg, "bounded")
    
    # img = preprocessing.ReadImage("preprocessed")

    # Text Extraction And Processing Phase
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
            'email' : emailID,
            'contact': contactNum
        })

@app.get("/success")
def setSuccess(request : Request):
    return templates.TemplateResponse("success.html" , {"request":request})