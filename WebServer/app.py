from flask import Flask, render_template, request
import os
import cv2
import base64

app = Flask(__name__)

#動画保存用のディレイクトリ
#これでなかったら作る。
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

#Flaskのルートページ
@app.route('/')

def index():
    #templatesフォルダ内のindex.htmlを表示する
    return render_template('index.html')

#画像をキャプチャして表示するエンドポイント
@app.route('/capture')
def upload_video():
    if 'video' not in request.files:
        return "Not file part"
    
    file = request.files['video']
    
    if file.filename == '':
        return "No selected files"
    
    if file:
        #動画ファイルの保存
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return f"File uploaded successfully: {filepath}"

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