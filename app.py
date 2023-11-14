import speech_recognition as sr
from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    transcript =""
    if request.method == "POST":
        print(" Form Data Received")
        
        if "file" not in request.files:
            return redirect(request.url)
        
        file = request.files["file"]
        if file.filename =="":
            return redirect(request.url)
        
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
                                  
            with audioFile as source:
                data = recognizer.record(source)
            #transcript = recognizer.recognize_google(data, key=None)
            transcript = recognizer.recognize_whisper(data)
            #print(transcript)
    return render_template('index.html', transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')