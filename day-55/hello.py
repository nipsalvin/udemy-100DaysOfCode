from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper

def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper

@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return '<h1 style="text-align:center">Hello, World!</h1>'\
            '<p style="text-align:center">This is a paragrapgh</p>'\
            '<img src="https://media.giphy.com/media/rt7Q7PuqSlINnUNKAL/giphy.gif" height=500>'

#Different route using app.route decorator
@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'

#Creating variable paths and converting path to a specified data-type
@app.route('/username/<name>/<int:number>')
def greeting(name, number):
    name = name.title()
    return f'Hello {name}! \n Are you {number} years old?'


if __name__ == '__main__':
    app.run(debug=True) #When debug is set to true, the server auto-reloads
    

