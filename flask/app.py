# flask is web framework used to build web application
# it can handle both frontend and backend
# it when you're using any frontend framework you can use it for backend only 

from flask import Flask, render_template 
# in this code Flask is main class to create web wapp
# render_template is function used to render html file from template folder

app = Flask(__name__)
# this it create flask app instance
# __name__ tells flask where to look for resources like template, static, files

@app.route('/')
# specifiy route

def home():
    return render_template("home.html")

if __name__ == "__main__":
# only run if file is executed directly not imported
    app.run(debug=True)
    # start flsk development server
    # debut=True Enable auto-reloading no need to start the server for changes


@app.route("/user")
def  greet():
    name = "Etiene"
    return render_template("home.html", username = name)