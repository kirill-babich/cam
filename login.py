from flask import Flask, render_template, Response,request
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('login.html')
database = {'admin' : 'admin', 'babich' : 'babich'}

@app.route('/form_login', methods=['POST', 'GET'])
def login():
    name = request.form['username']
    password = request.form['password']
    if name not in database:
        return render_template('login.html', info='Invalid User')
    else:
        if database[name]!=password:
            return render_template('login.html', info='Invalid Password')
        else:
            return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)