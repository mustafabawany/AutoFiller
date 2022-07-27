# AutoFiller

## Problem Statement

A utility to fill out form automatically by automatically pulling name, email id and contact number out of your resume.
These results are then used to auto-complete the job application forms.

## Description

Product title classication is merely an instance of text classication problems, which are well-studied
in literature. However, product titles possess some properties very different from general
documents. A title is usually a very short description, and an incomplete sentence. A product title
classier may need to be designed differently from a text classier. 
<br>
We will do exploratory data analysis on the dataset to remove noisy data, then we will perform
feature selection and extraction to identify suitable algorithms for multi-class classification. The
observations and results will be put into production to make it available for the end-users.

<br>

## Finished Product

![Finished Website](https://github.com/mustafabawany/AutoFiller/blob/main/AutoFiller_ProjectDemo.gif) 

## How to execute
NOTE: You must have pip and python pre-installed in your system
<br>
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
  <img name = "JavaScript" src = "https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"> 
  <img name = "Jupyter" src = "https://img.shields.io/badge/Jupyter%20-%23F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white">
  <img name = "Numpy" src = "https://img.shields.io/badge/numpy%20-%23013243.svg?&style=for-the-badge&logo=numpy&logoColor=white">
  <br>
  <img name = "HTML" src = "https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white">
  <img name = "CSS" src = "https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white">
  <img name = "Bootstrap" src = "https://img.shields.io/badge/bootstrap%20-%23563D7C.svg?&style=for-the-badge&logo=bootstrap&logoColor=white">
  <img name = "Docker" src = "https://img.shields.io/badge/Docker-Docker?style=for-the-badge&logo=docker&color=18191a">
  <img name = "OpenCV" src = "https://img.shields.io/badge/OpenCV-OpenCV?style=for-the-badge&logo=opencv&logoColor=fff&color=5C3EE8">
  <br>
  <img name = "Jinja" src = "https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black">
  <img name = "Postman" src = "https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white">
  <img name = "BitBucket" src = "https://img.shields.io/badge/bitbucket-%230047B3.svg?style=for-the-badge&logo=bitbucket&logoColor=white">
  <img name = "Firebase" src = "https://img.shields.io/badge/firebase-%23039BE5.svg?style=for-the-badge&logo=firebase">
</div>
