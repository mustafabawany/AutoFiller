FROM python:3.9-slim

# Copy all the files of current directory to app directory
COPY . /app

# Whenever docker will run, it will be by default in app directory
WORKDIR /app

# Install all the required packages to execute the program
RUN python3 -m pip install -r requirements.txt 

# Expose this port to client
EXPOSE 8000

# Command to execute the program
CMD [ "uvicorn" , "main:app" , "--reload" ]