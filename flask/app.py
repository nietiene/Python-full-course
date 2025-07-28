# flask is web framework used to build web application
# it can handle both frontend and backend
# it when you're using any frontend framework you can use it for backend only 

from flask import Flask, render_template 
# in this code flask is mai

app = Flask(__name__)

@app.route('/')

def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)