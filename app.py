from flask import Flask, render_template, request

app = Flask(__name__) # use app as name by convention; turn file as flask app

@app.route('/') #decorator; the default page
def index(): # the function name can be anything, just name it as index

    if "name" in request.args: # if there is a name in the request.args
        name = request.args["name"] # get the name from the request.args
    else:
        name = "world"
    
    return  render_template("index.html", name = name) # index.html, but we can't return it directly