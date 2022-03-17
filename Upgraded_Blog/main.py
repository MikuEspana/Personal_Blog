from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home_page():
    blogs_link = "https://api.npoint.io/5deaf41b4f8078c817e6"
    blogs_response = requests.get(blogs_link)
    blogs = blogs_response.json()
    return render_template('index.html', all_blogs=blogs)


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/read/<blog_id>')
def blog_page(blog_id):
    blogs_link = "https://api.npoint.io/5deaf41b4f8078c817e6"
    blogs_response = requests.get(blogs_link)
    blogs = blogs_response.json()
    return render_template("post.html", id=int(blog_id), all_blogs=blogs)


if __name__ == "__main__":
    app.run(debug=True)
