from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

response = requests.get('https://api.npoint.io/7770e7eff9765a42992b')
all_posts = response.json()

post_objects = []

for post in all_posts:
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'], post['date'], post['author'])
    post_objects.append(post_obj)

@app.route('/')
def get_all_posts():
    return render_template('index.html', all_posts = all_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/posts/<int:id>')
def show_post(id):
    requested_post = None
    for post in post_objects:
        if post.id == id:
            requested_post = post
    return render_template('post.html', post=requested_post)

if __name__ == '__main__':
    app.run(debug=True)