from flask import Flask
# Importing the Flask class which typically means creating a Flask Object

# Creating a flask object
app = Flask(__name__) # Passing in _ _ name _ _ (no spaces) into Flask

# Basic Route that will give us some info
# When it detects someone going to 0.0.0.0(our machine)/ do this thing
@app.route("/") # Decoration / Annotations 
def flask_test():
    return "Hello World"


# Setting up my server
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000)

# Exercise - Use flask to create a web server that returns some text when the page is accessed