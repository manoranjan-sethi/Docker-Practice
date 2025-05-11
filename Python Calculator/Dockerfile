# Base Image
FROM python:3.14.0a7-slim
# create directory inside the container 
WORKDIR /calApp

# From my computer copy this image to the container
COPY calculator.py /calApp/

# Command to be run 
CMD ["python", "calculator.py"]