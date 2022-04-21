from urllib import request
from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)
#untuk membedakan scrip atau module imprt
#flask function butuh

# @app.route('/')
# def hello_world():
#     return "<h1>Hello, World! Hello World!</h1>"

# @app.route('/<name>')
# #kurung siku artinya menerima value 

# # localhost:5000/<name>  #value akan di tampung ke variabel
# # localhost:5000/hello
# # localhost:5000/lol
# # localhost:5000/kaki
# def hello_name(name):
#     # hello(hello)
#     # hello(lol)
#     # hello(kaki)
#     return f"Hello, {escape(name)} !"

# @app.route('/')
# def index():
#     return 'Index page'

# @app.route('/hello')
# def hello():
#     return 'Hello, word'

@app.route('/hello')
def hello():
    return 'Hello, word'

@app.route('/user/<username>')
def show_user_profile(username):
    #show username profile
    return f'User, {escape(username)}'

@app.route('/book/<string:title>')
def show_book_title(title):
    return f'Detail Book, {escape(title)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post, {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Post, {subpath}'

@app.route('/suka/<path:sukapath>')
def show_sukapath(sukapath):
    return f'suka makan, {sukapath}'



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    return 'Do the login ...'

def show_the_login_form():
    return 'Displaying login to form'

@app.route('/')
def index():
    return (render_template('index.html'))

if __name__=='__main__':
    app.run(debug=True)

