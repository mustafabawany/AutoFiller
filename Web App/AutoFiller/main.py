# Importing Packages 
import cv2
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles
from pdf2image import convert_from_path

# Firebase Package 
import firebase_admin
from firebase_admin import credentials , storage , initialize_app

# Importing Class Implementation 
import sys 
sys.path.insert(0, 'backend/')
from PreProcessing import *
from TextExtraction import *

# Assigning Firebase Credentials 
cred = credentials.Certificate("./config.json")
initialize_app(cred , {'storageBucket' : 'autofiller-6f0cc.appspot.com'}) 

app = FastAPI()

# Fetching Firebase Storage Bucket 
bucket = storage.bucket()

# Assigning frontend/templates directory as Jinja Templates
templates = Jinja2Templates(directory= 'frontend/templates')

# Assigning static directory as static to execute CSS  
app.mount('/static', StaticFiles(directory= 'frontend/static'), name = 'static')

@app.get("/")
def getHome(request : Request):
    """ Returns Home Page Template """
    return templates.TemplateResponse("homepage.html" , {"request" : request})

@app.get("/about-us")
def getAboutUs(request : Request):
    """ Returns About Us Page Template """
    return templates.TemplateResponse("about.html" , {"request":request})

@app.get("/auto-complete")
def getAutocomplete(request : Request):
    """ Returns Auto Complete Page Template """
    return templates.TemplateResponse("autocomplete.html" , {"request":request})

@app.get("/auto-complete/{resume_id}")
async def ProcessResume(resume_id: str , request : Request):
    """ Returns Name, Email ID, Contact Number parsed from Resume """

    # Extracting PDF from Firebase Storage
    resume = bucket.get_blob("Resume/" + resume_id + ".pdf").download_to_filename('backend/Resume/resume.pdf')
    images = convert_from_path('backend/Resume/resume.pdf')    
    images[0].save('backend/Resume/page0.jpeg' , 'JPEG')
    
    # Creating Instances
    preprocessing = PreProcessing()
    text_extraction = TextExtraction()

    # Image Pre Processing Phase
    img = cv2.imread('backend/Resume/page0.jpeg')
    img = preprocessing.ZoomImage(img , 3)
    img = preprocessing.GrayScaleImage(img)
    img = preprocessing.CropImage(img)
    img = preprocessing.InvertImage(img)
    
    # Save & Read Image From Directory
    preprocessing.SaveImage(img, "preprocessed")
    img = preprocessing.ReadImage("preprocessed")

    # Text Extraction And Processing Phase
    text = text_extraction.ExtractText(img)
    personName = text_extraction.extract_name(text.title())
    contactNum = text_extraction.extract_phone_number(text.lower())
    emailID = text_extraction.extract_emails(text.lower())
    emailID = text_extraction.process_emails(emailID)
    if type(emailID) == list and len(emailID) > 0:
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
    """ Returns Success Page Template """
    return templates.TemplateResponse("success.html" , {"request":request})