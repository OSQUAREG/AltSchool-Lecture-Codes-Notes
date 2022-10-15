from flask import Flask

app = Flask(__name__)

@app.route('/') # This is called a Decorator.
def hello_world():
    return "Hello World"

@app.route('/home')
def home():
    return "Yes, I am Home"

@app.route('/about')
def about():
    return "This is about me...LOL"

@app.route('/<name>') # passing a dynamic code to the route
def greetings(name):
    return f"Hello {name}! How are you doing?"

@app.route('/post/<int:id>') # to specify the data type to pass to the route
def post_id(id):
    return f"This post has an id of {id}"

@app.route('/aboutme/<string:name>/<string:birthmonth>/<int:birthday>') # passing different dynamic code to route.
def birthdate(name,birthmonth,birthday):
    return f"My name is {name}. I was born in {birthmonth} {birthday}."

if __name__ == "__main__":
    #app.run() 
    app.run(debug=True) #turning on the Debugger makes your server live to respond as you make changes

