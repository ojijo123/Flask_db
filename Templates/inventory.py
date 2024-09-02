from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Erick Ojijo',
        'title': 'stock',
        'content': 'stock records',
        'date_posted': 'September 03, 2024'
    },
    {
        'author': 'Erick Ojijp',
        'title': 'Finance',
        'content': 'Financial records',
        'date_posted': 'September 03, 2024'
    },
    {'author': 'Erick Ojijo',
        'title': 'customers',
        'content': 'customers record',
        'date_posted': 'September 03, 2024'
    },
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
