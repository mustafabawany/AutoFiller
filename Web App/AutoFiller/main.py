from fastapi import FastAPI, Request, File , UploadFile
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles
from pdf2image import convert_from_path
import cv2
import matplotlib.pyplot as plt

app = FastAPI()
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
    return templates.TemplateResponse("parsedResume.html" , {"request" : request})

@app.post("/auto-complete")    
async def getPDF(resume : UploadFile = File(...)):
    return {"resume" : resume}

@app.get("/success")
def successPage(request : Request):
    return {"Success" : "Yayyy!"}

@app.post("/success")
def getInfo(name: str , email : str , contact : str):
    return {"Success" : "Yayyy!!"}


