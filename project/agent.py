from flask import Blueprint
from flask import flash,request,redirect,render_template, url_for
from project import config, MySQL
import time
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user

agent = Blueprint('agent',__name__,template_folder='templates')

db = config.db
cursor = db.cursor()

login_manager = LoginManager()
#没有访问权限时跳转到的页面
login_manager.login_view = 'agent.login'
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

# @admin.route('/')
# def hello_world():
#     data = MySQL.VERSION(cursor)
#     return 'Hello World!'+str(data)


@agent.route('/register',methods=['GET','POST'])
def register():
    return render_template("agent_register.html")

@agent.route('/postregister',methods=['GET','POST'])
def postregister():
    if(request.method=='POST'):
        data = request.form
        agent_username = data['agent_username']
        agent_pw = data['agent_pw']
        agent_name = data['agent_name']
        agent_phone = data['agent_phone']
        agent_company = data['agent_company']
        agent_wechat = data['agent_wechat']
        print(data)
        f = MySQL.agent_register(cursor, db, agent_username, agent_pw,agent_name,agent_phone,agent_company,agent_wechat)
        if f:
            flash("注册成功")
            time.sleep(2)
            return redirect(url_for('agent.login'))
        else:
            flash("请重试")
            return redirect(url_for('agent.register'))

@agent.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template("agent_login.html")

@agent.route('/postlogin/', methods=['GET', 'POST'])
def postlogin():
    if request.method=='POST':
        data = request.form
        username = str(data['username'])
        password = data['password']
        res = MySQL.agent_login(cursor, username, password)
        if(res):
            curr_user = User()
            curr_user.id = username
            login_user(curr_user)
            return redirect(url_for('agent.view_order'))
        else:
            return "not"


@agent.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@agent.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'GET':
        return render_template('agent_add.html')
    elif request.method == 'POST':
        data = request.form
        apt_name = data['apt_name']
        bathroom_count = int(data['bathroom_count'])
        bedroom_count = int(data['bedroom_count'])
        price = int(data['price'])
        direction = data['direction']
        building_name = data['building_name']
        place = data['place']
        building_manager = data['building_manager']
        building_phone = data['building_phone']
        other_details = data['other_details']
        pic_url = data['pic_url']
        room_area = data['room_area']
        transport = data['transport']
        max_people_count = int(data['max_people_number'])
        full_place = place.split('/')
        distinct = full_place[2]
        agent_username = current_user.id
        agent_id = MySQL.find_agent_id(cursor,agent_username)
        flag = MySQL.add_agent(db,cursor,agent_id,apt_name,bathroom_count,bedroom_count,room_area,transport,max_people_count,pic_url,price,direction,building_name,distinct,building_manager,building_phone,other_details)
        if flag:
            return "success"
        else:
            return str(data)

@agent.route('/view_order',methods = ['GET','POST'])
def view_order():
    agent_username = current_user.id
    result,flag = MySQL.agent_order(cursor,agent_username)
    if flag:
        return render_template('agent_order.html',result=result)
    else:
        return "wrong"

@agent.route('/feature')
def feature():
    return 1

@agent.route('/modify',methods=['POST','GET'])
def modify():
    if request.method == 'GET':
        apt_id = request.args.get('apt_id')
        t = apt_id
        result,flag = MySQL.agent_modify_view(cursor,apt_id)
        if flag:
            return render_template('agent_modify.html',result=result,apt_id = apt_id)
        return "success"
    elif request.method == 'POST':
        data = request.form
        apt_id = data['apt_id']
        apt_name = data['apt_name']
        bathroom_count = int(data['bathroom_count'])
        bedroom_count = int(data['bedroom_count'])
        price = data['price']
        direction = data['direction']
        building_name = data['building_name']
        place = data['place']
        building_manager = data['building_manager']
        building_phone = data['building_phone']
        other_details = data['other_details']
        pic_url = data['pic_url']
        room_area = data['room_area']
        transport = data['transport']
        max_people_count = int(data['max_people_number'])
        full_place = place.split('/')
        # province = full_place[0]
        # city = full_place[1]
        district = full_place[2]
        agent_username = current_user.id
        agent_id = MySQL.find_agent_id(cursor,agent_username)

        flag = MySQL.agent_modify(db,cursor,agent_id,apt_name,bathroom_count,bedroom_count,room_area,transport,max_people_count,pic_url,price,direction,building_name,district,building_manager,building_phone,other_details,apt_id)
        if flag:
            return "success"
        else:
            return str(data)

@agent.route('/apartment')
def apartment():
    agent_username = current_user.id
    result,flag = MySQL.agent_apartment(cursor,agent_username)
    if flag:
        return render_template('agent_apartment.html',result = result)
    else:
        return "wrong"

@agent.route('/delete')
def delete():
    apt_id = request.args.get('apt_id')
    MySQL.agent_delete(db,cursor,apt_id)
    return "删除成功"

@agent.route('/order_detail',methods=['POST','GET'])
def order_detail():
    if request.method == 'GET':
        order_id = request.args.get('order_id')
        result = MySQL.agent_order_detail(cursor,order_id)
        return render_template('agent_order_detail.html',result = result)

@agent.route('/change_order_status',methods=['POST','GET'])
def change_order_status():
    order_id = request.args.get('order_id')
    MySQL.change_order_status(db,cursor,order_id)
    return redirect(url_for('agent.view_order'))