# flask is web framework used to build web application
# it can handle both frontend and backend
# it when you're using any frontend framework you can use it for backend only 

from flask import Flask, render_template, request 
# in this code Flask is main class to create web wapp
# render_template is function used to render html file from template folder

app = Flask(__name__)
# this it create flask app instance
# __name__ tells flask where to look for resources like template, static, files

@app.route('/')
# specifiy route

def home():
    return render_template("home.html")

@app.route("/user")
def greet():
    name = "Etiene"
    return render_template("home.html", username = name)



# forms(get input from users) we use flask's request to capture data
@app.route("/form", methods=["GET", "POST"])
# methods allow both GET and PODT http method
def index():
    # define index functio that will runs when user visited /form
    if request.method == "POST":
        # this check if user is already clicked on post buttom
        name = request.form["name"]
        # req.form takes value name like input type="name"
        return render_template("greeting.html", username = name)
        #  render greeting page with user's name 
    return render_template("form.html")
# this is default page when user visit page without submitting

if __name__ == "__main__":
# only run if file is executed directly not imported
    app.run(debug=True)
    # start flsk development server
    # debut=True Enable auto-reloading no need to start the server for changes


# jinja2 is template engine used in flask it lets you insert Pythin logic int HTML using {{}} and {% %}
# on variables we use {{ variable }}

# on conditionals {% %}
# {% if age > 18 %}
#   <p>You are an adult</p>
# {% else: %}
#   <p><You are underage./p>

# on loops
# <ul>
#   {% for user in users %}
#     <li>{{ user }}</li>
#   {% endfor %}
# </ul>
# 