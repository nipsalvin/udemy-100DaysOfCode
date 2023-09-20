from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv('MY_EMAIL')
EMAIL_PASSWORD = os.getenv('GMAIL_APP_PASSWORD')
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get('https://api.npoint.io/7770e7eff9765a42992b').json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        ### You can either pass the msg_sent as a variable from python to html or pass it as a boolean and write the message in HTML
        msg_sent = f'Message Successfully sent {data["message"]}'
        # return render_template("contact.html", msg_sent=msg_sent)
        return render_template("contact.html", msg_sent=True)
    else:
        # return render_template("contact.html")
        return render_template("contact.html", msg_sent = False)

def send_email(name, email, phone, message):
    pass


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/form-entry', methods=['GET', 'POST'])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return f'<h1>Message Successfully sent</h1> <p>{data["message"]}</p>'



if __name__ == "__main__":
    app.run(debug=True, port=5001)
