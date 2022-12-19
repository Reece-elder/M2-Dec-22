from flask import Flask
# Importing the Flask class which typically means creating a Flask Object

# Creating a flask object
app = Flask(__name__) # Passing in _ _ name _ _ (no spaces) into Flask

# Basic Route that will give us some info
# When it detects someone going to 0.0.0.0(our machine)/ do this thing
@app.route("/") # Decoration / Annotations 
def flask_test():
    return "Hello World"

@app.route("/route")
def route():
    colours = ["red","green", "blue", "purple"]
    for colour in colours:
        print(colour)
    return colours

@app.route("/shop/<id>")
def shop_page(id):
    # data = db.findData(id)
    # return data
    return f"Page for shop {id}"


# Setting up my server
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000)

# Exercise - Use flask to create a web server that returns some text when the page is accessed

# Second exercise - Create a new route for /about that just renders "About us.."
# - Add another route that takes in a string and adds "<name>'s profile" and returns it