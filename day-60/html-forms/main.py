from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    username = request.form['username']
    password = request.form['password']
    return render_template('login.html', username=username, password=password)
    # return f'<h1>name: {username} password: {password}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
