# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route('/')
def home():

    name = "Dhruv Taritla" # write your name
    age = "15" # write your age

    return render_template('index.html',age=age, name=name)

# define the route to father webpage
@app.route('/father')
def father():
    name = "Venugopal Taritla"
    age = "50"
    return render_template('father.html',age=age, name=name)

# define the route to mother webpage
@app.route('/mother')
def mother():
    name = "Rupadevi Taritla"
    age = "41"
    return render_template('mother.html',age=age, name=name)

# define the route to friends webpage
@app.route('/friend')
def friend1():
    name = "Dhruv Tanwar"
    age = "14"
    return render_template('friend.html',age=age, name=name)

# add other routes, if you want


# run the file
if __name__  ==  '__main__':
    app.run()
