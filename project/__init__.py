# -*- coding: utf-8 -*-
import os

from flask import Flask,render_template
from flask_login import LoginManager,login_user,login_required,logout_user,current_user
from .admin import admin
from .guest import guest
from .apartment import apartment
from .order import order
from .agent import agent
from model import User
from flask_bootstrap import Bootstrap

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates_dir = os.path.join(BASE_DIR, 'templates')
static_dir = os.path.join(BASE_DIR, 'static')
app = Flask(__name__, static_folder=static_dir, template_folder=templates_dir)
app.secret_key = '12345'

# BOOTSTRAP
bootstrap = Bootstrap(app)

# BLUEPRINT
app.register_blueprint(guest,url_prefix='/guest')
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(apartment,url_prefix='/apartment')
app.register_blueprint(order,url_prefix='/order')
app.register_blueprint(agent,url_prefix='/agent')

login_manager = LoginManager()
login_manager.login_view = "notallowed"
login_manager.init_app(app)

# LOGIN

@login_manager.user_loader
def load_user(user_id):
    curr_user = User(user_id)
    return curr_user

# ROUTES
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# @app.route('/logout')
# @login_required
# def logout():
#     print(current_user.id)
#     logout_user()
#     return 'Logged out successfully'

@app.route('/notallowed', methods=['GET', 'POST'])
def notallowed():
    return render_template('notallowed.html')

if __name__ == '__main__':
    app.run()