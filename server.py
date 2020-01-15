from application import app 

if __name__ == '__main__':
    app.run(debug=True)

'''
from flask import Flask, render_template
app = Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=8000)
'''