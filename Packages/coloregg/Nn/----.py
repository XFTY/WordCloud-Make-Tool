from typing import overload
from flask import Flask

app = Flask(__name__)

@overload

@app.route('/')
def hello_world():
    return 'hello!'

@app.route('/retuen')
def main():
    return 'debug'

@app.route('/help')
def mains():
    return 'bbb'

@app.route('/text')
def sel():
    return '''
    <html>
        <head>
            <title>Tlag</title>
        </head>
        <body>
            <h1>hellp</h1>
        </body>
    </html>
    '''

app.run(debug=True,port=8000)