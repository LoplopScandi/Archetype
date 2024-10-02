from flask import Flask, render_template
import cv2
import base64

app = Flask(__name__)

#Flaskのルートページ
@app.route('/')

def index():
    return 'Web Server is Running!'

#画像をキャプチャして表示するエンドポイント
@app.route('/capture')
def capture_image():
    #OpenCVでカメラキャプチャ
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        return "Failed to capture image"
    

def hello():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)