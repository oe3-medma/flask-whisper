# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY . /app


RUN apt-get update && apt-get install git -y

RUN pip install --no-cache-dir -r requirements.txt

#RUN pip3 install "git+https://github.com/openai/whisper.git" 
#RUN apt-get install -y ffmpeg


# Expose the port the app runs on
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

