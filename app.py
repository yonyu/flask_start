from flask import Flask, render_template, request

app = Flask(__name__) # use app as name by convention; turn file as flask app

@app.route('/') #decorator; the default page
def index(): # the function name can be anything, just name it as index

    return  render_template("index.html") # index.html, but we can't use it directly