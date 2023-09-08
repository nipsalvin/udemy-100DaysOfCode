from flask import Flask, render_template
import requests
from post import Post


response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
posts = response.json()

post_objects = []

for post in posts:
    #Create `Post` objects with the below attributes and append them to `post_objects` list
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
