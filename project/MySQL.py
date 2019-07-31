#!/usr/bin/python3


def VERSION(cursor):
    cursor.execute("select * from admin")
    data = cursor.fetchall()
    print(data)
    return data

def register(cursor, db,name, password):
    sql_insert = '''
    INSERT INTO
        admin(username, password)
    VALUES
        (%s, %s)
    '''
    # 参数拼接要用 %s，execute 中的参数传递必须是一个 tuple 类型
    try:
        # 执行sql语句
        cursor.execute(sql_insert, (name, password))
        # 提交到数据库执行
        db.commit()
        print("ture")
        return 1
    except:
        # 如果发生错误则回滚
        db.rollback()
        print("false")
        return 0

def agent_register(cursor, db,agent_username, agent_pw,agent_name,agent_phone,agent_company,agent_wechat):
    sql_insert = '''
    INSERT INTO
        agent(agent_username, agent_pw,agent_name,agent_phone,agent_company,agent_wechat)
    VALUES
        (%s, %s,%s,%s,%s,%s)
    '''
    # 参数拼接要用 %s，execute 中的参数传递必须是一个 tuple 类型
    try:
        # 执行sql语句
        cursor.execute(sql_insert, (agent_username, agent_pw,agent_name,agent_phone,agent_company,agent_wechat))
        # 提交到数据库执行
        db.commit()
        return True
    except:
        # 如果发生错误则回滚
        db.rollback()
        return False

def login(cursor,name,password):
    sql = '''SELECT  username, password from admin where username = %s '''
    try:
        cursor.execute(sql,(name,))
        results = cursor.fetchall()
        print(results)
        if(results[0][1]==password):
            return True
        else:
            return False
    except:
        return False

def agent_login(cursor,agent_username,agent_pw):
    sql = '''SELECT  agent_username, agent_pw from agent where agent_username = %s '''
    try:
        cursor.execute(sql,(agent_username,))
        print(agent_username)
        results = cursor.fetchall()
        print(results)
        if(results[0][1]==agent_pw):
            return True
        else:
            return False
    except:
        return False

def query(cursor,name):
    sql = '''SELECT  username, password,compid,role from admin where username = %s '''
    try:
        cursor.execute(sql,(name,))
        results = cursor.fetchall()
        return results[0][2],results[0][3]
    except:
        return -1,False

def guest_register(cursor,db,guest_username,guest_pw,gender,guest_name,job,wechat,guest_phone,graduate_school,major,feature):
    sql_insert = '''
    INSERT INTO
        guest(guest_username,guest_pw,gender,guest_name,job,wechat,guest_phone,graduate_school,major,feature)
    VALUES
        (%s, %s, %s,%s, %s,%s,%s,%s,%s,%s)
    '''
    cursor.execute(sql_insert, (guest_username, guest_pw, gender, guest_name, job, wechat, guest_phone, graduate_school, major, feature))
    #     # 提交到数据库执行
    db.commit()

def guest_modify(cursor,db,guest_username,guest_pw,gender,guest_name,job,wechat,guest_phone,graduate_school,major,feature):
    sql_insert = '''
    UPDATE 
        guest
    SET
    guest_pw=%s,gender=%s,guest_name=%s,job=%s,wechat=%s,guest_phone=%s,graduate_school=%s,major=%s,feature=%s
    WHERE guest_username = %s
    '''
    try:
        cursor.execute(sql_insert, (guest_pw, gender, guest_name, job, wechat, guest_phone, graduate_school, major, feature,guest_username))
        db.commit()
        return True
    except:
        return False

def guest_login(cursor,name,password):
    sql = '''SELECT  username, password from guest where username = %s '''
    try:
        cursor.execute(sql,(name,))
        results = cursor.fetchall()
        print(results)
        if(results[0][1]==password):
            return results[0][3],True
        else:
            return -1,False
    except:
        return -1,False

def guest_feature(cursor,guest_username):
    sql = '''SELECT * FROM guest WHERE guest_username = %s'''
    try:
        cursor.execute(sql,(guest_username,))
        result = cursor.fetchall()
        guest = {}
        guest['guest_id'] = result[0][0]
        guest['guest_username'] = result[0][1]
        guest['guest_pw'] = result[0][2]
        guest['gender'] = int(result[0][3])
        guest['guest_name'] = result[0][4]
        guest['job'] = result[0][5]
        guest['wechat']=result[0][6]
        guest['guest_phone']=result[0][7]
        guest['graduate_school']=result[0][8]
        guest['major']=result[0][9]
        guest['feature']=result[0][10]
        guest['apply_status']=result[0][11]
        if guest['gender'] == 1:
            guest['gender']='男'
        else:
            guest['gender']='女'
        return True,guest
    except:
        return False,-1

def query_others(cursor,name,password): #查看其他合租者
    sql = '''SELECT  username, password from guest where username = %s '''
    try:
        cursor.execute(sql,(name,))
        results = cursor.fetchall()
        print(results)
        if(results[0][1]==password):
            return results[0][3],True
        else:
            return -1,False
    except:
        return -1,False

def querry_all_apartment(cursor):
    sql = '''SELECT
apartment.apt_id,
apartment.bathroom_count,
apartment.bedroom_count,
apartment.room_area,
apartment.transport,
apartment.max_people_number,
building.building_name,
a.address_name,
b.address_name,
apartment.price,
c.address_name,
apartment.apt_name,
apartment.pic_url
FROM apartment NATURAL JOIN building NATURAL JOIN address as a INNER JOIN address as b ON b.address_id = a.distinct_id JOIN address as c ON b.province_id = c.address_id
WHERE max_people_number >0
'''
    try:
        cursor.execute(sql)
        resultsset = cursor.fetchall()
        apartment_set = []
        print(resultsset)
        for results in resultsset:
            apartment = {}
            apartment['apt_id'] = results[0]
            apartment['bathroom_count'] = results[1]
            apartment['bedroom_count'] = results[2]
            apartment['room_area'] = results[3]
            apartment['transport'] = results[4]
            apartment['max_people_number'] = results[5]
            apartment['building_name'] = results[6]
            apartment['distinct'] = results[7]
            apartment['city'] = results[8]
            apartment['price'] = results[9]
            apartment['province'] = results[10]
            apartment['apt_name'] = results[11]
            apartment['pic_url'] = results[12]
            apartment_set.append(apartment)
        return apartment_set,True
    except:
        return -1,False

def query_single_apartment(cursor,id):
    sql = '''SELECT
apartment.apt_id,
apartment.bathroom_count,
apartment.bedroom_count,
apartment.room_area,
apartment.transport,
apartment.max_people_number,
building.building_name,
a.address_name,
b.address_name,
apartment.price,
c.address_name,
apartment.apt_name,
apartment.pic_url,
building.building_manager,
building.building_phone,
building.other_details,
apartment.direction,
agent.agent_name,
agent.agent_company,
agent.agent_phone
FROM apartment NATURAL JOIN building NATURAL JOIN address as a INNER JOIN address as b ON b.address_id = a.distinct_id JOIN address as c ON b.province_id = c.address_id NATURAL JOIN agent
WHERE apartment.apt_id = %s
'''
    cursor.execute(sql, (id,))
    try:
        print(id,type(id))
        cursor.execute(sql,(id,))
        results = cursor.fetchall()
        print(results)
        apartment = {}
        apartment['apt_id'] = results[0][0]
        apartment['bathroom_count'] = results[0][1]
        apartment['bedroom_count'] = results[0][2]
        apartment['room_area'] = results[0][3]
        apartment['transport'] = results[0][4]
        apartment['max_people_number'] = results[0][5]
        apartment['building_name'] = results[0][6]
        apartment['distinct'] = results[0][7]
        apartment['city'] = results[0][8]
        apartment['price'] = results[0][9]
        apartment['province'] = results[0][10]
        apartment['apt_name'] = results[0][11]
        apartment['pic_url'] = results[0][12]
        apartment['building_manager'] = results[0][13]
        apartment['building_phone'] = results[0][14]
        apartment['other_details'] = results[0][15]
        apartment['direction'] = results[0][16]
        apartment['agent_name'] = results[0][17]
        apartment['agent_company'] = results[0][18]
        apartment['agent_phone'] = results[0][19]
        return apartment,True
    except:
        return -1,False

def query_order_people(cursor,apt_id):
    sql = '''
    SELECT DISTINCT
order_detail.guest_username,
order_detail.guest_name,
order_detail.job,
order_detail.wechat,
order_detail.guest_phone,
order_detail.graduate_school,
order_detail.major,
order_detail.feature,
order_detail.gender
FROM
order_detail
WHERE
order_detail.apt_id = %s
    '''
    print("#######&&&&&@@@@@@@@")
    # try:
    cursor.execute(sql,(apt_id,))
    resultsset = cursor.fetchall()
    apartment_set = []
    print("#######",resultsset)
    for results in resultsset:
        apartment = {}
        apartment['guest_username'] = results[0]
        apartment['guest_name'] = results[1]
        apartment['job'] = results[2]
        apartment['wechat'] = results[3]
        apartment['guest_phone'] = results[4]
        apartment['graduate_school'] = results[5]
        apartment['major'] = results[6]
        apartment['feature'] = results[7]
        apartment['gender'] = int(results[8])
        if apartment['gender'] == 1:
            apartment['gender'] = '男'
        else:
            apartment['gender'] = '女'
        apartment_set.append(apartment)
    return apartment_set, True
    # except:
    #     return -1,False

def querry_index_apartment(cursor,province,city,district,minroom,maxroom,people):
    if people == -1:
        people = '%'
        print("people")
    if minroom == 0:
        print("minroom")
        sql = '''SELECT
apartment.apt_id,
apartment.bathroom_count,
apartment.bedroom_count,
apartment.room_area,
apartment.transport,
apartment.max_people_number,
building.building_name,
a.address_name AS district,
b.address_name AS city,
apartment.price,
c.address_name AS province,
apartment.apt_name,
apartment.pic_url
FROM apartment NATURAL JOIN building NATURAL JOIN address as a INNER JOIN address as b ON b.address_id = a.distinct_id JOIN address as c ON b.province_id = c.address_id
WHERE c.address_name = %s and b.address_name = %s and a.address_name = %s and apartment.max_people_number LIKE %s
'''
        try:
            cursor.execute(sql,(province,city,district,people))
            resultsset = cursor.fetchall()
            apartment_set = []
            print(resultsset)
            for results in resultsset:
                apartment = {}
                apartment['apt_id'] = results[0]
                apartment['bathroom_count'] = results[1]
                apartment['bedroom_count'] = results[2]
                apartment['room_area'] = results[3]
                apartment['transport'] = results[4]
                apartment['max_people_number'] = results[5]
                apartment['building_name'] = results[6]
                apartment['distinct'] = results[7]
                apartment['city'] = results[8]
                apartment['price'] = results[9]
                apartment['province'] = results[10]
                apartment['apt_name'] = results[11]
                apartment['pic_url'] = results[12]
                apartment_set.append(apartment)
            return apartment_set, True
        except:
            return -1,False
    else:
        sql = '''SELECT
apartment.apt_id,
apartment.bathroom_count,
apartment.bedroom_count,
apartment.room_area as room,
apartment.transport,
apartment.max_people_number,
building.building_name,
a.address_name AS district,
b.address_name AS city,
apartment.price,
c.address_name AS province,
apartment.apt_name,
apartment.pic_url
FROM apartment NATURAL JOIN building NATURAL JOIN address as a INNER JOIN address as b ON b.address_id = a.distinct_id JOIN address as c ON b.province_id = c.address_id
WHERE c.address_name = %s and b.address_name = %s and a.address_name = %s and apartment.max_people_number like %s and apartment.room_area between %s and %s
        '''
        try:
            cursor.execute(sql, (province, city, district, people, minroom, maxroom))
            resultsset = cursor.fetchall()
            apartment_set = []
            print(resultsset)
            for results in resultsset:
                apartment = {}
                apartment['apt_id'] = results[0]
                apartment['bathroom_count'] = results[1]
                apartment['bedroom_count'] = results[2]
                apartment['room_area'] = results[3]
                apartment['transport'] = results[4]
                apartment['max_people_number'] = results[5]
                apartment['building_name'] = results[6]
                apartment['distinct'] = results[7]
                apartment['city'] = results[8]
                apartment['price'] = results[9]
                apartment['province'] = results[10]
                apartment['apt_name'] = results[11]
                apartment['pic_url'] = results[12]
                apartment_set.append(apartment)
            return apartment_set, True
        except:
            return -1,False

def querry_detail_apartment(cursor,province,city,district,minroom,maxroom,people,minprice,maxprice):
    if people == -1:
        people = '%'
        print("people")
    if minroom == 0:
        print("minroom")
        sql = '''SELECT
apartment.apt_id,
apartment.bathroom_count,
apartment.bedroom_count,
apartment.room_area,
apartment.transport,
apartment.max_people_number,
building.building_name,
a.address_name AS district,
b.address_name AS city,
apartment.price,
c.address_name AS province,
apartment.apt_name,
apartment.pic_url
FROM apartment NATURAL JOIN building NATURAL JOIN address as a INNER JOIN address as b ON b.address_id = a.distinct_id JOIN address as c ON b.province_id = c.address_id
WHERE c.address_name = %s and b.address_name = %s and a.address_name = %s and apartment.max_people_number LIKE %s and apartment.price between %s and %s
'''
        try:
            print(province,city,district,people,minprice,maxprice)
            cursor.execute(sql,(province,city,district,people,minprice,maxprice))
            resultsset = cursor.fetchall()
            apartment_set = []
            print(resultsset)
            for results in resultsset:
                apartment = {}
                apartment['apt_id'] = results[0]
                apartment['bathroom_count'] = results[1]
                apartment['bedroom_count'] = results[2]
                apartment['room_area'] = results[3]
                apartment['transport'] = results[4]
                apartment['max_people_number'] = results[5]
                apartment['building_name'] = results[6]
                apartment['distinct'] = results[7]
                apartment['city'] = results[8]
                apartment['price'] = results[9]
                apartment['province'] = results[10]
                apartment['apt_name'] = results[11]
                apartment['pic_url'] = results[12]
                apartment_set.append(apartment)
            return apartment_set, True
        except:
            return -1,False
    else:
        sql = '''SELECT
apartment.apt_id,
apartment.bathroom_count,
apartment.bedroom_count,
apartment.room_area as room,
apartment.transport,
apartment.max_people_number,
building.building_name,
a.address_name AS district,
b.address_name AS city,
apartment.price,
c.address_name AS province,
apartment.apt_name,
apartment.pic_url
FROM apartment NATURAL JOIN building NATURAL JOIN address as a INNER JOIN address as b ON b.address_id = a.distinct_id JOIN address as c ON b.province_id = c.address_id
WHERE c.address_name = %s and b.address_name = %s and a.address_name = %s and apartment.max_people_number like %s and apartment.room_area between %s and %s and apartment.price between %s and %s
        '''
        try:
            cursor.execute(sql, (province, city, district, people, minroom, maxroom,minprice,maxprice))
            resultsset = cursor.fetchall()
            apartment_set = []
            print(resultsset)
            for results in resultsset:
                apartment = {}
                apartment['apt_id'] = results[0]
                apartment['bathroom_count'] = results[1]
                apartment['bedroom_count'] = results[2]
                apartment['room_area'] = results[3]
                apartment['transport'] = results[4]
                apartment['max_people_number'] = results[5]
                apartment['building_name'] = results[6]
                apartment['distinct'] = results[7]
                apartment['city'] = results[8]
                apartment['price'] = results[9]
                apartment['province'] = results[10]
                apartment['apt_name'] = results[11]
                apartment['pic_url'] = results[12]
                apartment_set.append(apartment)
            return apartment_set, True
        except:
            return -1,False

def order_submit(cursor):
    sql = '''SELECT * FROM apartment'''
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        return results
    except:
        return -1,False

def select_apartment(cursor):
    sql = '''SELECT * FROM apartment'''
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        return results,True
    except:
        return -1,False

# 管理员查看所有申请者
def query_apply(cursor):
    sql = '''SELECT * FROM guest WHERE apply_status = %s'''
    try:
        cursor.execute(sql,(0,))
        results = cursor.fetchall()
        print(results)
        return results,True
    except:
        return -1,False

# 管理员通过验证
def pass_apply(db,cursor,guest_username):
    sql = '''UPDATE guest SET apply_status = %s WHERE guest_username = %s'''
    try:
        cursor.execute(sql,(1,guest_username))
        db.commit()
        return True
    except:
        return False

# def find_guest(cursor,guest_id):
#     sql = '''SELECT'''

def submit_order(db,cursor,apt_id,guest_username,status_id,submit_time):
    sql_user = '''SELECT guest_id from guest where guest_username = %s
    '''
    cursor.execute(sql_user,(guest_username,))
    result = cursor.fetchall()
    guest_id = result[0][0]
    print(guest_id)
    apt_id = int(apt_id)
    guest_id = int(guest_id)
    status_id = int(status_id)
    sql = '''INSERT INTO booking(apt_id,guest_id,status_id,submit_time) VALUES (%s,%s,%s,%s)
    '''

    try:
        cursor.execute(sql,(apt_id,guest_id,status_id,submit_time))
        db.commit()
        return True
    except:
        return False

#查看某位代理人的订单详情
def agent_order_detail(cursor,order_id):
    sql = '''SELECT * FROM order_detail WHERE order_id = %s'''
    try:
        cursor.execute(sql, (order_id,))
        results = cursor.fetchall()
        apartment = {}
        apartment['guest_id'] = results[0][0]
        apartment['apt_id'] = results[0][1]
        apartment['order_id'] = results[0][2]
        apartment['submit_time'] = results[0][3]
        apartment['status_describe'] = results[0][4]
        apartment['bathroom_count'] = results[0][5]
        apartment['bedroom_count'] = results[0][6]
        apartment['room_area'] = results[0][7]
        apartment['transport'] = results[0][8]
        apartment['max_people_number'] = results[0][9]
        apartment['building_name'] = results[0][10]
        apartment['district'] = results[0][11]
        apartment['city'] = results[0][12]
        apartment['price'] = results[0][13]
        apartment['province'] = results[0][14]
        apartment['apt_name'] = results[0][15]
        apartment['pic_url'] = results[0][16]
        apartment['building_manager'] = results[0][17]
        apartment['building_phone'] = results[0][18]
        apartment['other_details'] = results[0][19]
        apartment['direction'] = results[0][20]
        apartment['agent_name'] = results[0][21]
        apartment['agent_company'] = results[0][22]
        apartment['agent_phone'] = results[0][23]
        apartment['agent_username'] = results[0][24]
        apartment['guest_username'] = results[0][25]
        apartment['gender'] = results[0][24]
        apartment['guest_name'] = results[0][25]
        apartment['job'] = results[0][26]
        apartment['wechat'] = results[0][27]
        apartment['guest_phone'] = results[0][28]
        apartment['graduate_school'] = results[0][29]
        return apartment, True
    except:
        return -1, False

#查看某位代理人的所有订单
def agent_order(cursor,agent_username):
    sql = '''SELECT * FROM order_detail WHERE agent_username = %s'''
    try:
        cursor.execute(sql, (agent_username,))
        resultsset = cursor.fetchall()
        apartment_set = []
        print(resultsset)
        for results in resultsset:
            apartment = {}
            apartment['guest_id'] = results[0]
            apartment['apt_id'] = results[1]
            apartment['order_id'] = results[2]
            apartment['submit_time'] = results[3]
            apartment['status_describe'] = results[4]
            apartment['bathroom_count'] = results[5]
            apartment['bedroom_count'] = results[6]
            apartment['room_area'] = results[7]
            apartment['transport'] = results[8]
            apartment['max_people_number'] = results[9]
            apartment['building_name'] = results[10]
            apartment['district'] = results[11]
            apartment['city'] = results[12]
            apartment['price'] = results[13]
            apartment['province'] = results[14]
            apartment['apt_name'] = results[15]
            apartment['pic_url'] = results[16]
            apartment['building_manager'] = results[17]
            apartment['building_phone'] = results[18]
            apartment['other_details'] = results[19]
            apartment['direction'] = results[20]
            apartment['agent_name'] = results[21]
            apartment['agent_company'] = results[22]
            apartment['agent_phone'] = results[23]
            apartment['agent_username'] = results[24]
            apartment['guest_username'] = results[25]
            apartment['gender'] = results[24]
            apartment['guest_name'] = results[25]
            apartment['job'] = results[26]
            apartment['wechat'] = results[27]
            apartment['guest_phone'] = results[28]
            apartment['graduate_school'] = results[29]
            apartment_set.append(apartment)
        return apartment_set, True
    except:
        return -1, False

#查看某位顾客的所有订单
def guest_order(cursor,agent_username):
    sql = '''SELECT * FROM order_detail WHERE guest_username = %s'''
    try:
        cursor.execute(sql, (agent_username,))
        resultsset = cursor.fetchall()
        apartment_set = []
        print(resultsset)
        for results in resultsset:
            apartment = {}
            apartment['guest_id'] = results[0]
            apartment['apt_id'] = results[1]
            apartment['order_id'] = results[2]
            apartment['submit_time'] = results[3]
            apartment['status_describe'] = results[4]
            apartment['bathroom_count'] = results[5]
            apartment['bedroom_count'] = results[6]
            apartment['room_area'] = results[7]
            apartment['transport'] = results[8]
            apartment['max_people_number'] = results[9]
            apartment['building_name'] = results[10]
            apartment['district'] = results[11]
            apartment['city'] = results[12]
            apartment['price'] = results[13]
            apartment['province'] = results[14]
            apartment['apt_name'] = results[15]
            apartment['pic_url'] = results[16]
            apartment['building_manager'] = results[17]
            apartment['building_phone'] = results[18]
            apartment['other_details'] = results[19]
            apartment['direction'] = results[20]
            apartment['agent_name'] = results[21]
            apartment['agent_company'] = results[22]
            apartment['agent_phone'] = results[23]
            apartment['agent_username'] = results[24]
            apartment['guest_username'] = results[25]
            apartment['gender'] = results[24]
            apartment['guest_name'] = results[25]
            apartment['job'] = results[26]
            apartment['wechat'] = results[27]
            apartment['guest_phone'] = results[28]
            apartment['graduate_school'] = results[29]
            apartment_set.append(apartment)
        return apartment_set, True
    except:
        return -1, False

#查看所有订单
def admin_order(cursor):
    sql = '''SELECT * FROM order_detail'''
    try:
        cursor.execute(sql)
        resultsset = cursor.fetchall()
        apartment_set = []
        print(resultsset)
        for results in resultsset:
            apartment = {}
            apartment['guest_id'] = results[0]
            apartment['apt_id'] = results[1]
            apartment['order_id'] = results[2]
            apartment['submit_time'] = results[3]
            apartment['status_describe'] = results[4]
            apartment['bathroom_count'] = results[5]
            apartment['bedroom_count'] = results[6]
            apartment['room_area'] = results[7]
            apartment['transport'] = results[8]
            apartment['max_people_number'] = results[9]
            apartment['building_name'] = results[10]
            apartment['district'] = results[11]
            apartment['city'] = results[12]
            apartment['price'] = results[13]
            apartment['province'] = results[14]
            apartment['apt_name'] = results[15]
            apartment['pic_url'] = results[16]
            apartment['building_manager'] = results[17]
            apartment['building_phone'] = results[18]
            apartment['other_details'] = results[19]
            apartment['direction'] = results[20]
            apartment['agent_name'] = results[21]
            apartment['agent_company'] = results[22]
            apartment['agent_phone'] = results[23]
            apartment['agent_username'] = results[24]
            apartment['guest_username'] = results[25]
            apartment['gender'] = results[24]
            apartment['guest_name'] = results[25]
            apartment['job'] = results[26]
            apartment['wechat'] = results[27]
            apartment['guest_phone'] = results[28]
            apartment['graduate_school'] = results[29]
            apartment_set.append(apartment)
        return apartment_set, True
    except:
        return -1, False


def agent_apartment(cursor,agent_username):
    sql='''
SELECT
apartment_details.apt_id,
apartment_details.bathroom_count,
apartment_details.bedroom_count,
apartment_details.room_area,
apartment_details.transport,
apartment_details.max_people_number,
apartment_details.building_name,
apartment_details.district,
apartment_details.city,
apartment_details.price,
apartment_details.province,
apartment_details.apt_name,
apartment_details.pic_url
FROM
apartment_details
WHERE
apartment_details.agent_username=%s
    '''
    try:
        cursor.execute(sql,(agent_username,))
        resultsset = cursor.fetchall()
        apartment_set = []
        print(resultsset)
        for results in resultsset:
            apartment = {}
            apartment['apt_id'] = results[0]
            apartment['bathroom_count'] = results[1]
            apartment['bedroom_count'] = results[2]
            apartment['room_area'] = results[3]
            apartment['transport'] = results[4]
            apartment['max_people_number'] = results[5]
            apartment['building_name'] = results[6]
            apartment['district'] = results[7]
            apartment['city'] = results[8]
            apartment['price'] = results[9]
            apartment['province'] = results[10]
            apartment['apt_name'] = results[11]
            apartment['pic_url'] = results[12]
            apartment_set.append(apartment)
        return apartment_set,True
    except:
        return -1,False

#代理人修改房间时默认显示原始数据
def agent_modify_view(cursor,apt_id):
    sql = '''
    SELECT
    apartment_details.apt_id,
    apartment_details.bathroom_count,
    apartment_details.bedroom_count,
    apartment_details.room_area,
    apartment_details.transport,
    apartment_details.max_people_number,
    apartment_details.building_name,
    apartment_details.district,
    apartment_details.city,
    apartment_details.price,
    apartment_details.province,
    apartment_details.apt_name,
    apartment_details.pic_url,
    apartment_details.building_manager,
    apartment_details.building_phone,
    apartment_details.other_details,
    direction
    FROM
    apartment_details
    WHERE
    apartment_details.apt_id=%s
        '''
    try:
        cursor.execute(sql,(apt_id))
        results = cursor.fetchall()
        apartment = {}
        apartment['apt_id'] = results[0][0]
        apartment['bathroom_count'] = results[0][1]
        apartment['bedroom_count'] = results[0][2]
        apartment['room_area'] = results[0][3]
        apartment['transport'] = results[0][4]
        apartment['max_people_number'] = results[0][5]
        apartment['building_name'] = results[0][6]
        apartment['district'] = results[0][7]
        apartment['city'] = results[0][8]
        apartment['price'] = results[0][9]
        apartment['province'] = results[0][10]
        apartment['apt_name'] = results[0][11]
        apartment['pic_url'] = results[0][12]
        apartment['building_manager'] = results[0][13]
        apartment['building_phone'] = results[0][14]
        apartment['other_details'] = results[0][15]
        apartment['direction'] = results[0][16]
        apartment['place'] = apartment['province']+'/'+apartment['city']+'/'+apartment['district']
        return apartment,True
    except:
        return -1,False

#更新修改房屋信息
def agent_modify(db,cursor,agent_id,apt_name,bathroom_count,bedroom_count,room_area,transport,max_people_number,pic_url,price,direction,building_name,district,building_manager,building_phone,other_details,apt_id):
    sql1 = '''
    SELECT
    address.address_id
    FROM
    address
    WHERE
    address.address_name = %s
    '''
    sql2 = '''
        SELECT
    building.building_id
    FROM
    building
    WHERE
    building_name = %s AND address_id = %s
        '''

    sql3 = '''
       UPDATE building SET
       building_name=%s,address_id=%s,building_manager=%s,building_phone=%s,other_details=%s
       WHERE building_id = %s
       '''
    sql4 = '''
        UPDATE apartment SET
        agent_id = %s,building_id=%s,apt_name=%s,bathroom_count=%s,bedroom_count=%s,room_area=%s,transport=%s,max_people_number=%s,pic_url=%s,price=%s,direction=%s
        WHERE apt_id=%s
        '''
    # try:
    print(district)
    cursor.execute(sql1, (district,))
    result = cursor.fetchall()
    address_id = int(result[0][0])
    cursor.execute(sql2, (building_name, address_id))
    result = cursor.fetchall()
    building_id = int(result[0][0])
    # if not result:
    #     cursor.execute(sql3, (building_name, address_id, building_manager, building_phone, other_details))
    #     db.commit()
    #     cursor.execute(sql2, (building_name, address_id))
    #     result = cursor.fetchall()
    cursor.execute(sql3, (building_name, address_id, building_manager, building_phone, other_details,building_id))
    cursor.execute(sql4, (agent_id, building_id, apt_name, bathroom_count, bedroom_count, room_area, transport, max_people_number, pic_url,price, direction,apt_id))
    db.commit()


def add_agent(db,cursor,agent_id,apt_name,bathroom_count,bedroom_count,room_area,transport,max_people_number,pic_url,price,direction,building_name,district,building_manager,building_phone,other_details):
    sql1 = '''
SELECT
address.address_id
FROM
address
WHERE
address.address_name = %s
'''
    sql2 = '''
    SELECT
building.building_id
FROM
building
WHERE
building_name = %s AND address_id = %s
    '''
    sql3 = '''
    INSERT INTO 
    building(building_name,address_id,building_manager,building_phone,other_details)
    VALUES 
    (%s,%s,%s,%s,%s)
    '''

    sql4 = '''
    INSERT INTO 
    apartment(agent_id,building_id,apt_name,bathroom_count,bedroom_count,room_area,transport,max_people_number,pic_url,price,direction)
    values 
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    # try:
    print(district)
    cursor.execute(sql1,(district,))
    result = cursor.fetchall()
    address_id = int(result[0][0])
    cursor.execute(sql2,(building_name,address_id))
    result = cursor.fetchall()
    if not result:
        cursor.execute(sql3,(building_name,address_id,building_manager,building_phone,other_details))
        db.commit()
        cursor.execute(sql2,(building_name,address_id))
        result = cursor.fetchall()
    building_id = int(result[0][0])
    cursor.execute(sql4,(agent_id,building_id,apt_name,bathroom_count,bedroom_count,room_area,transport,max_people_number,pic_url,price,direction))
    db.commit()
    #     return True
    # except:
    #     return False

def find_agent_id(cursor,agent_username):
    sql = '''SELECT agent_id FROM agent WHERE agent_username = %s'''
    cursor.execute(sql,(agent_username))
    result = cursor.fetchall()
    print(agent_username)
    print(result)
    agent_id = result[0][0]
    return agent_id

#代理人删除房屋信息
def agent_delete(db,cursor,apt_id):
    sql = '''
    DELETE FROM apartment
    where apt_id = %s
    '''
    cursor.execute(sql,(apt_id))
    db.commit()

def admin_agentlist(cursor):
    sql = '''SELECT * FROM agent'''
    try:
        cursor.execute(sql)
        resultsset = cursor.fetchall()
        apartment_set = []
        print(resultsset)
        for results in resultsset:
            apartment = {}
            apartment['agent_username'] = results[1]
            apartment['agent_name'] = results[3]
            apartment['agent_phone'] = results[4]
            apartment['agent_company'] = results[5]
            apartment['agent_wechat'] = results[6]
            apartment_set.append(apartment)
        return apartment_set,True
    except:
        return -1,False

def admin_guestlist(cursor):
    sql = '''SELECT
guest.guest_username,
guest.guest_name,
guest.wechat,
guest.guest_phone,
apply_status
FROM
guest'''
    try:
        cursor.execute(sql)
        resultsset = cursor.fetchall()
        apartment_set = []
        print(resultsset)
        for results in resultsset:
            apartment = {}
            apartment['guest_username'] = results[0]
            apartment['guest_name'] = results[1]
            apartment['guest_wechat'] = results[2]
            apartment['guest_phone'] = results[3]
            apartment['apply_status'] = int(results[4])
            if apartment['apply_status'] == 1:
                apartment['apply_status'] = '已通过'
            else:
                apartment['apply_status'] = '未通过'
            apartment_set.append(apartment)
        return apartment_set,True
    except:
        return -1,False

def admin_pass_guest(db,cursor,guest_username):
    sql='''UPDATE guest SET apply_status = 1 WHERE guest_username = %s'''
    try:
        cursor.execute(sql,(guest_username))
        db.commit()
        return True
    except:
        return False

def agent_order_detail(cursor,booking_id):
    sql = '''SELECT * FROM order_detail WHERE booking_id = %s'''
    cursor.execute(sql,(booking_id,))
    results =  cursor.fetchall()
    apartment = {}
    apartment['guest_id'] = results[0][0]
    apartment['apt_id'] = results[0][1]
    apartment['order_id'] = booking_id
    apartment['bathroom_count'] = results[0][5]
    apartment['bedroom_count'] = results[0][6]
    apartment['room_area'] = results[0][7]
    apartment['transport'] = results[0][8]
    apartment['max_people_number'] = results[0][9]
    apartment['building_name'] = results[0][10]
    apartment['distinct'] = results[0][11]
    apartment['city'] = results[0][12]
    apartment['price'] = results[0][13]
    apartment['province'] = results[0][14]
    apartment['apt_name'] = results[0][15]
    apartment['pic_url'] = results[0][16]
    apartment['guest_username'] = results[0][17]
    apartment['guest_pw'] = results[0][18]
    apartment['gender'] = int(results[0][19])
    apartment['guest_name'] = results[0][20]
    apartment['job'] = results[0][21]
    apartment['wechat'] = results[0][22]
    apartment['guest_phone'] = results[0][23]
    apartment['graduate_school'] = results[0][24]
    apartment['major'] = results[0][25]
    apartment['feature'] = results[0][26]
    apartment['apply_status'] = results[0][27]
    if apartment['gender'] == 1:
        apartment['gender'] = '男'
    else:
        apartment['gender'] = '女'
    return apartment

def change_order_status(db,cursor,booking_id):
    sql = '''UPDATE booking SET status_id = %s WHERE booking_id =%s'''
    a= 1
    booking_id = int(booking_id)
    cursor.execute(sql,(a,booking_id,))
    db.commit()

def guest_check_pass(cursor,guest_username):
    try:
        sql = '''SELECT apply_status FROM guest WHERE guest_username = %s'''
        cursor.execute(sql,(guest_username))
        result = cursor.fetchall()
        r = int(result[0][0])
        if r == 0:
            return False
        else:
            return  True
    except:
        return False