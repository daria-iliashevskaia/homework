from flask import Flask, request

# Это уже знакомое callable WSGI-приложение
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, SkyPro"

@app.get('/users')
def users_get():
    return 'GET /users'

@app.post('/users')
def users():
    return 'Users', 302

@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'