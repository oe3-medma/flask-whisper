# Speech-to-text transcription service
Speech-to-text (S2T) transcription technology aims to convert spoken language into written text by processing and interpreting the complex patterns of human speech. 



## Installation

We recommend installing S2T transcription service in a virtual environment. Run the following commands using a terminal. This will:

```bash
mkdir flask-app-whisper
python3 -m venv venv
```

We used Python 3.10.11 and PyTorch to train and test our whisper model. the following command will pull and install the latest commit from this repository, along with its Python dependencies:

```bash
pip install git+https://github.com/openai/whisper.git 
```
It also requires the command-line tool ffmpeg to be installed on your system, which is available from most package managers:

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

We also install Flask Python module, Next create requirements.txt file. After that create a simple Flask application and run Flask app on port 5000

```bash
pip install Flask
pip freeze > requirements.txt
vi app.py
```

## Create a docker image 

To build a Docker image from a Dockerfile, we use the command docker build. With -t or –tag we can set a name and optionally a tag in the name:tag format. 

commands:
```bash
docker build -t flask-app-whisper .
docker images
```

## Create Docker Container

To run the container, we use the command docker run –name -d -p 5000:5000. With –name we can assign a name to the container. You can open the browser and enter localhost:5000


commands:
```bash
docker run -it -p 5000:5000 -d flask-app-whisper
docker container ls 
```

## Docker Hub
S2T transcription Webservice available on Docker Hub. You can find the latest version of this repository on docker hub for CPU.

Docker Hub: https://hub.docker.com/repository/docker/omeresdocker/whisper/general

Command:
```bash
docker pull omeresdocker/whisper:latest
```
