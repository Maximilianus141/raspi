from flask import Flask as f

app = f(__name__)

@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"