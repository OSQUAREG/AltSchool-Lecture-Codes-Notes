from flask import Flask

app = Flask(__name__)

# App Routing means mapping URLs to a specific function that will handle to logic of the URL

@app.route('/') # This is called a Decorator. 
def hello_world():
    return "Hello World"

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/<name>') # passing a dynamic code to the route
def greetings(name):
    return f"Hello {name}! How are you doing?"

@app.route('/post/<int:id>') # passing a dynamic code to the route with specified data type.
def post_id(id):
    return f"This post has an id of {id}"

@app.route('/aboutme/<string:name>/<string:birthmonth>/<int:birthday>') # passing different dynamic code to route.
def birthdate(name,birthmonth,birthday):
    return f"My name is {name}. I was born in {birthmonth} {birthday}."

if __name__ == "__main__":
    #app.run() 
    app.run(debug=True) #turning on the Debugger makes your server live to respond as you make changes

