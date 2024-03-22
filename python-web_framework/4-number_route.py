'''import flask server'''
from flask import Flask
app = Flask(__name__)

        
@app.route("/",strict_slashes=False)

def Hello_HBNB():
    return "Hello HBNB!"

@app.route("/hbnb")
def HBNB():
    return "HBNB"

@app.route("/c/<text>")
def khadija(text):
    formated_text = text.replace("_", " ")
    return "C {}".format(formated_text)

    #return f"C {formated_text}" 

@app.route("/python/<text>")
@app.route("/python/")
def python_text(text = "is cool"):
    formated_text = text.replace("_", " ")
    return "Python {}".format(formated_text)

@app.route("/number/<int:n>")
def python_integer(n):
    return "{} is a number".format(n)
    
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)