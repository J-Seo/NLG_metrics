# 도커를 사용하고 싶으면 참고하세용 :)
# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Download spacy models
RUN python -m spacy download en_core_web_md
RUN python -m spacy download en
