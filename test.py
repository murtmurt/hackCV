from flask import Flask, render_template, Response
import cv2
import os
import re
import time

app = Flask(__name__)

def gen_frames():
    for filename in sorted(os.listdir("frames"), key = lambda f: int(re.sub('\D', '', f))):
        time.sleep(1 / 30)
        with open(os.path.join("frames", filename), "rb") as f:
            frame = f.read()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video")
def video():
    return Response(gen_frames(), mimetype = "multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run(debug = True)