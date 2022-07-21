from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles

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