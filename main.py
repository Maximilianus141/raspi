from flask import Flask as f


def readFile(fileName):
    with open(fileName) as f:
        return f.read
    

app = f(__name__)

@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

