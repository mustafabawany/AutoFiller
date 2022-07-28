# AutoFiller

## Problem Statement

Many job portals still don’t have any AI auto-form completion; even if they do, they fail on
resumes made with templates. This causes job applicants to fill out and correct the forms,
creating a time-consuming activity.

## Description

This project is dedicated to creating an OCR software that recognizes text and patterns on
resumes and CVs to auto-complete application forms. It is found that many job applicants
bounce off job portals with manual forms, so to address this problem we will parse out their
resumes.

## Proposed Solution 

Create an OCR-based AI model, trained on multiple templates from the internet which can
parse resumes and can fill out the information like Name, Email Address and Phone Number.

## Finished Product

![Finished Website](https://github.com/mustafabawany/AutoFiller/blob/main/AutoFiller_ProjectDemo.gif) 

## How to execute
NOTE: You must have pip and python pre-installed in your system

1. Clone this project on your local repository
```
git clone <repository link>
```
2. Install required packages
```
pip3 install -r requirements.txt
```
3. Retrieve language model for spacy
```
python3 -m spacy download en_core_web_sm
```
4. Go to the working directory
```
cd Autofiller
```
5. Execute the application
```
uvicorn main:app --reload
```
## Technology Used

<div>
  <img name = "Python" src = "https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white">
  <img name = "FastAPI" src = "https://img.shields.io/badge/FastAPI-FastAPI?style=for-the-badge&logo=fastapi&color=18191a">
  <img name = "OpenCV" src = "https://img.shields.io/badge/OpenCV-OpenCV?style=for-the-badge&logo=opencv&logoColor=fff&color=5C3EE8">
  <img name = "Jupyter" src = "https://img.shields.io/badge/Jupyter%20-%23F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white">
  <img name = "Numpy" src = "https://img.shields.io/badge/numpy%20-%23013243.svg?&style=for-the-badge&logo=numpy&logoColor=white">
  <br>
  <img name = "Jinja" src = "https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black">
  <img name = "JavaScript" src = "https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"> 
  <img name = "HTML" src = "https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white">
  <img name = "CSS" src = "https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white">
  <img name = "Bootstrap" src = "https://img.shields.io/badge/bootstrap%20-%23563D7C.svg?&style=for-the-badge&logo=bootstrap&logoColor=white">
  <br>
  <img name = "Docker" src = "https://img.shields.io/badge/Docker-Docker?style=for-the-badge&logo=docker&color=18191a">
  <img name = "Postman" src = "https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white">
  <img name = "BitBucket" src = "https://img.shields.io/badge/bitbucket-%230047B3.svg?style=for-the-badge&logo=bitbucket&logoColor=white">
  <img name = "Firebase" src = "https://img.shields.io/badge/firebase-%23039BE5.svg?style=for-the-badge&logo=firebase">
</div>

## Future Roadmap
<ul>
  <li>Expand to parse more fields like Education, Experience and Skills</li>
  <li>Adding an additional feature of evaluating resumes based on grammar and design, and
providing recommendations to improve.</li>
</ul>

## Dataset Source 
<a href = "https://www.kaggle.com/datasets/aishikai/resume-dataset"><img src = "https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white"></a>

## Contact
<div> 
  <a href="mustafabawany204@gmail.com"><img name = "Gmail" src = "https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://pk.linkedin.com/in/mustafabawany"><img name = "LinkedIn" src = "https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white"></a>
</div>
