from flask import Blueprint
from flask import flash,request,redirect,render_template, url_for
from project import config, MySQL
from model import User
from flask_login import login_user,login_required,logout_user,current_user,login_manager
import time
guest = Blueprint('guest',__name__)
db = config.db
cursor = db.cursor()

login_manager.login_view = "guest.login"


@guest.route('/')
def hello_world():
    data = MySQL.VERSION(cursor)
    return 'Hello World!'+str(data)

@guest.route('/register',methods=['GET','POST'])
def register():
    return render_template("guest_register.html")

@guest.route('/postregister',methods=['GET','POST'])
def postregister():
    if(request.method=='POST'):
        data = request.form
        guest_username = data['guest_username']
        guest_pw = data['guest_pw']
        guest_name = data['guest_name']
        # birthday = data['birthday']
        gender = data['gender']
        job = data['job']
        wechat = data['wechat']
        guest_phone = data['guest_phone']
        graduate_school = data['graduate_school']
        major = data['major']
        data = data.to_dict()
        l = data.keys()
        value = ""
        for key in l:
            if key in ['read','music','movie','talkshow','fashion','weibo','zhihu','food','healthy','paint','drama','game']:
                value = value + str(data[key])+" "
        flag = MySQL.guest_register(cursor, db, guest_username, guest_pw, gender, guest_name, job, wechat, guest_phone, graduate_school, major,value)
        if flag == 1:
            flash("已提交申请，还需管理员审核")
        else:
            flash("注册失败，请重新注册！")
    return redirect(url_for('guest.login')) #需要更改！！！

@guest.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template("guest_login.html")

@guest.route('/postlogin/', methods=['GET', 'POST'])
def postlogin():
    if request.method=='POST' :
        data = request.form
        username = str(data['username'])
        password = data['password']
        res = MySQL.guest_login(cursor, username, password)
        if(res):
            curr_user = User(username)
            login_user(curr_user)
            print(current_user.id)
            return  redirect(url_for('index'))

        else:
            return "not" #用户注册失败，需要修改！！！

@guest.route('/success/', methods=['GET', 'POST'])
# @login_required
def success():
   return  render_template('check_order.html')


@guest.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@guest.route('/feature',methods=['GET','POST'])
@login_required
def feature():
    guest_username = current_user.id
    flag,result = MySQL.guest_feature(cursor,guest_username)
    if flag:
        return render_template('guest_feature.html',result = result)
    else:
        return "wrong"

@guest.route('/others',methods=['GET','POST'])
@login_required
def others():
    if request.method == 'GET':
        guest_username = request.args.get('guest_username')
        flag,result = MySQL.guest_feature(cursor,guest_username)
        if flag:
            return render_template('other_feature.html',result = result)
        else:
            return "wrong"

@guest.route('/modify',methods=['GET','POST'])
@login_required
def modify():
    if request.method == 'GET':
        guest_username = request.args.get('guest_username')
        flag, result = MySQL.guest_feature(cursor, guest_username)
        if flag:
            return render_template('guest_modify.html', result=result)
        else:
            return "wrong"
    if request.method=='POST':
        data = request.form
        guest_username = data['guest_username']
        guest_pw = data['guest_pw']
        guest_name = data['guest_name']
        # birthday = data['birthday']
        gender = data['gender']
        job = data['job']
        wechat = data['wechat']
        guest_phone = data['guest_phone']
        graduate_school = data['graduate_school']
        major = data['major']
        data = data.to_dict()
        l = data.keys()
        value = ""
        for key in l:
            if key in ['read','music','movie','talkshow','fashion','weibo','zhihu','food','healthy','paint','drama','game']:
                value = value + str(data[key])+" "
        flag = MySQL.guest_modify(cursor, db, guest_username, guest_pw, gender, guest_name, job, wechat, guest_phone, graduate_school, major,value)
        if flag:
            flash("修改成功!")
            time.sleep(2)
            return redirect(url_for('guest.feature'))
        else:
            flash("修改失败！")
            time.sleep(2)
            return redirect(url_for('index'))

@guest.route('/view_order',methods = ['GET','POST'])
def view_order():
    guest_username = current_user.id
    result,flag = MySQL.guest_order(cursor,guest_username)
    if flag:
        return render_template('guest_orderlist.html',result=result)
    else:
        return "wrong"
