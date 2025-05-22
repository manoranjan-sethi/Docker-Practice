# Base image
FROM python:3.14.0a7-slim

# Create directory for the app
WORKDIR /flaskapp

# Copy the application files to the directory 
COPY app.py requirements.txt /flaskapp/

# Run requirements.txt
RUN pip install -r requirements.txt

# Run the flask app 
CMD ["python", "app.py"] 