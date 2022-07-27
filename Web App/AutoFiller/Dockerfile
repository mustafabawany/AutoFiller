FROM python:3.9-slim

# Copy all the files of current directory to app directory
COPY . /app

# Whenever docker will run, it will be by default in app directory
WORKDIR /app

RUN python3 -m pip install -r requirements.txt 

EXPOSE 8000

CMD [ "uvicorn" , "main:app" , "--reload" ]