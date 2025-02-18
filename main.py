"""Main"""

from os import environ
from flask import Flask, render_template
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5

try:
    from .helpers import load_user, csrf
    from .controller.posts import router as posts
    from .controller.auth import router as login
except ImportError:
    from helpers import load_user, csrf
    from controller.posts import router as posts
    from controller.auth import router as login

load_dotenv()

app = Flask(__name__)
app.secret_key = environ.get("SECRET_KEY", "secret")
login_manager = LoginManager()
bootstrap = Bootstrap5()

# ==== API/CONTROLLER INJECTION ====

bootstrap.init_app(app)
csrf.init_app(app)
login_manager.init_app(app)
login_manager.user_loader(load_user)
posts.init_app(app)
login.init_app(app)


# ==== WEB ROUTE ====

@app.get('/')
def root():
    """Index"""
    return render_template('index.html')

@app.get('/dashboard')
def dashboard():
    """Dashboard"""
    return render_template('dashboard.html')

@app.get('/about')
def about():
    """About us"""
    return render_template('about.html')

# ==== RUN ====

if __name__ == '__main__':
    app.run('127.0.0.1', 8000, debug=True, use_reloader=True, threaded=True)
