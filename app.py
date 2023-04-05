from flask import Flask, redirect, render_template, request, url_for

# Это callable WSGI-приложение
app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def index():
    return render_template('index.html')

