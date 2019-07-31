from flask import Blueprint
from flask import flash,request,redirect,render_template, url_for
import time
from project import config, MySQL
from model import User
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user
import time

apartment = Blueprint('apartment',__name__,template_folder='templates')
db = config.db
cursor = db.cursor()

@apartment.route('/')
def apart():
    result,flag = MySQL.querry_all_apartment(cursor)
    if flag:
        return render_template("apartment.html",result = result)
        # return str(result)
    else:
        return "wrong"


@apartment.route('/detail')
def detail():
    id = request.args.get('apt_id')
    id = int(id)
    result,flag1 = MySQL.query_single_apartment(cursor,id)
    place = result['province']+'/'+result['city']+'/'+result['distinct']
    people,flag2 = MySQL.query_order_people(cursor,id)
    if flag1 and flag2:
        return render_template('detail.html',result = result,place=place,apt_id=id,people=people)
        # return str(result)
    else:
        return "wrong"
    # return "y"


@apartment.route('/list')
def list():
    result, flag = MySQL.querry_all_apartment(cursor)
    if flag:
        return render_template("apartment.html", result=result)
    else:
        return "wrong"


@apartment.route('/findindex',methods=['GET','POST'])
def findindex():
    if request.method == 'POST':
        data = request.form
        # print(data)
        place = str(data['place'])
        room = int(data['room'])
        min_room = room
        people = int(data['adults'])
        full_place = place.split('/')
        province = full_place[0]
        city = full_place[1]
        distinct = full_place[2]
        if room != 140 and room != 0 :
            max_room = room+20
        elif room != 0:
            max_room = 999
        else:
            max_room = 0
        print(province,city,distinct,min_room,max_room,people)
        result,flag = MySQL.querry_index_apartment(cursor,province,city,distinct,min_room,max_room,people)
        if flag:
            return render_template("apartment.html", result=result)
        else:
            return "wrong"
    # result,flag = MySQL.querry_all_apartment(cursor)
    return "yes"

@apartment.route('/find',methods=['GET','POST'])
# @login_required
def find():
    # guest_username = current_user.id
    # f = MySQL.guest_check_pass(cursor,guest_username)
    # if not f:
    #     return render_template("notallowed.html")
    if request.method == 'POST':
        data = request.form
        print(data)
        place = str(data['place'])
        room = int(data['room'])
        min_room = room
        people = int(data['adults'])
        full_place = place.split('/')
        province = full_place[0]
        city = full_place[1]
        distinct = full_place[2]
        if room != 140 and room != 0 :
            max_room = room+20
        elif room != 0:
            max_room = 999
        else:
            max_room = 0
        price = str(data['hugo'])
        print(price)
        price = price.split('￥')
        maxprice = int(price[2])
        temp = price[1].split("-")
        minprice = int(temp[0])
        print(province,city,distinct,min_room,max_room,people,minprice,maxprice)
        result,flag = MySQL.querry_detail_apartment(cursor,province,city,distinct,min_room,max_room,people,minprice,maxprice)
        if flag:
            return render_template("apartment.html", result=result)
        else:
            return "wrong"
    # result,flag = MySQL.querry_all_apartment(cursor)
    #     return str(data)

@apartment.route('/order',methods=['POST','GET'])
@login_required
def order():
    guest_username = current_user.id
    f = MySQL.guest_check_pass(cursor,guest_username)
    if not f:
        return render_template("notallowed.html")
    apt_id = request.args.get('apt_id2')
    # apt_id = id
    username = current_user.id
    print("#####",username,"######")
    submit_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    flag = MySQL.submit_order(db,cursor,apt_id,username,0,submit_time)
    # return render_template('check_order.html',apt_id=apt_id)
    if flag:
        return render_template('success.html')
    else:
        return "fail"
    # elif request.method == 'POST':
