from flask import Blueprint
from flask import flash,request,redirect,render_template, url_for
import time
from project import config, MySQL
from model import User
from flask_login import login_user,login_required,logout_user,current_user

order = Blueprint('order',__name__,template_folder='templates')
db = config.db
cursor = db.cursor()

@order.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        return request.data