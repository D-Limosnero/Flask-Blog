from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy Data
posts = [
    {
        'author': 'Dean Limosnero',
        'title': 'Blog Post 1',
        'content': 'Hello world',
        'date_posted': 'July 22, 2023'
    }, 
    {
        'author': 'guitarhero',
        'title': 'Bocchi the Rock',
        'content': 'hello',
        'date_posted': 'October 9, 2022'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)