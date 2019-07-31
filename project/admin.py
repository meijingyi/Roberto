from flask import Blueprint
from flask import flash,request,redirect,render_template, url_for
from project import config, MySQL
import time
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user

admin = Blueprint('admin',__name__,template_folder='templates')

db = config.db
cursor = db.cursor()

login_manager = LoginManager()
login_manager.login_view = "admin.login"

#没有访问权限时跳转到的页面
# login_manager.login_view = 'hello_world'
# login_manager.login_message_category = 'info'
# login_manager.login_message = 'Access denied.'
# login_manager.init_app(app)

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
        curr_user = User()
        curr_user.id = user_id
        return curr_user

@admin.route('/')
def hello_world():
    data = MySQL.VERSION(cursor)
    return 'Hello World!'+str(data)


@admin.route('/register',methods=['GET','POST'])
def register():
    return render_template("admin_register.html")

@admin.route('/postregister',methods=['GET','POST'])
def postregister():
    if(request.method=='POST'):
        data = request.form
        username = data['agent_username']
        password = data['agent_pw']

        print(data)
        MySQL.register(cursor, db, username, password)
        flash("注册成功")
        time.sleep(2)
    return redirect(url_for('login'))

@admin.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template("admin_login.html")

@admin.route('/postlogin/', methods=['GET', 'POST'])
def postlogin():
    if(request.method=='POST'):
        data = request.form
        username = str(data['username'])
        password = data['password']
        res = MySQL.login(cursor, username, password)
        if(res):
            curr_user = User()
            curr_user.id = username
            login_user(curr_user)
            return redirect(url_for('admin.orderlist'))
        else:
            return "not"

@admin.route('/success/', methods=['GET', 'POST'])
@login_required
def success():
   return  current_user.id


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@admin.route('/examine')
# @login_required
def examine():
    results = MySQL.query_apply(cursor)
    return str(results)

@admin.route('/passguest',methods = ['GET','POST'])
def passguest():
    guest_username = request.args.get('guest_username')
    flag = MySQL.admin_pass_guest(db,cursor,guest_username)
    if flag:
        return redirect(url_for('admin.orderlist'))
    else:
        return "wrong"

@admin.route('/orderlist',methods = ['GET','POST'])
def orderlist():
    result,flag = MySQL.admin_order(cursor)
    print(str(result))
    if flag:
        return render_template('admin_order.html',result=result)
    else:
        return "wrong"

@admin.route('/agentlist',methods = ['GET','POST'])
def agentlist():
    result,flag = MySQL.admin_agentlist(cursor)
    print(str(result))
    if flag:
        return render_template('admin_agentlist.html',result=result)
    else:
        return "wrong"

@admin.route('/guestlist',methods = ['GET','POST'])
def guestlist():
    result,flag = MySQL.admin_guestlist(cursor)
    if flag:
        return render_template('admin_guestlist.html',result=result)
    else:
        return "wrong"

@admin.route('/admin_guest_feature',methods=['GET','POST'])
@login_required
def admin_guest_feature():
    if request.method == 'GET':
        guest_username = request.args.get('guest_username')
        flag,result = MySQL.guest_feature(cursor,guest_username)
        if flag:
            return render_template('admin_guest_feature.html',result = result)
        else:
            return "wrong"