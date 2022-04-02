from flask import Flask, request, render_template
from textblob import TextBlob


app = Flask(__name__) #__xx__

#which directory is file in
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST": #when user press 'Enter' in front end
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", result=r))
    else: #before user press 'Enter' in front end
        return(render_template("index.html", result="Type in text"))


if __name__ == "__main__": #need this to run in cloud environment, to verify that code is mine
    app.run()
    

