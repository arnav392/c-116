from flask import Flask 
from flask import render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():
    
    Name = "Arnav" # write your name
    Age = "16" # write your age

    return render_template('index.html' , name = Name , age = Age)

# define the route to father webpage
def father():
    name="Gagandeep"
    age="41"

    return render_template('father.html',name=name,age=age)

# define the route to mother webpage
def mother():
    name="Mandeep"
    age="35"

    return render_template('mother.html',name=name,age=age)

# define the route to friends webpage
def friend():
    name="Kunal"
    age="16"

    return render_template('friend.html',name=name,age=age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
