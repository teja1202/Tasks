from flask import Flask,request,jsonify
import json
import bcrypt
import new_my_task_.dbnewtask as db
import new_my_task_.test as test
from flask_jwt_extended import  create_access_token,create_refresh_token,get_jwt_identity,jwt_required,get_jwt,JWTManager
import datetime
app=Flask(__name__)


app.config["JWT_SECRET_KEY"]="teja"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=10)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = datetime.timedelta(minutes=10)
jwt=JWTManager(app)
key_1="TjRCw+wF0Bg06UKmzmpN0A==" ###key for all other apis
key_2="gYxhAQAHPeyvP3NthYEMWA==" ###key only for rigester and login
#all insert queries ie., for motivator level 1 and 2 and also for call level 0 ,call level 1 ,call level 2,call level 3 
@app.route("/motlevel1",methods=["POST"])
def motivator_level_1():
    thekey_1=request.headers["key_1"]
    if key_1!=thekey_1:
        return jsonify("message:the header key is wrong")
    req=request.get_json()
    value=req["value"]
    query1="INSERT INTO motivator_level1(values) VALUES('"+str(value)+"');"
    result=db.dbTransactionIUD(query1)
    return result
#############################insert response 
@app.route("/motlevel2",methods=["POST"])
def motivator_level_2():
    thekey_1=request.headers["key_1"]
    if key_1!=thekey_1:
       return jsonify("message:the header key is wrong")
    req=request.get_json()
    id_mot1=req["id_mot1"]
    id_mot2=req["id_mot2"]
    response=req["response"]
    query2="INSERT INTO motivator_level2(id_mot1,id_mot2,response) VALUES('"+str(id_mot1)+"','"+str(id_mot2)+"','"+str(response)+"');"
    result=db.dbTransactionIUD(query2)
    return result
########### insert level 0
@app.route("/calltypeinsert",methods=["POST"])
def calltypeinsert():
    thekey_1=request.headers["key_1"]
    if key_1!=thekey_1:
        return jsonify("message:the header key is wrong")
    req=request.get_json()
    value=req["value"]
    q="INSERT INTO call_map_table(call_direction)VALUES('"+str(value)+"');"
    result=db.dbTransactionIUD(q)
    return result
############## level 1 insert for call level 1
@app.route("/iclevel1",methods=["POST"])
def calllevel1():
    thekey_1=request.headers["key_1"]
    if key_1!=thekey_1:
        return jsonify("message:the header key is wrong")
    req=request.get_json()
    call_id=req["call_id"]
    io_id=req["io_id"]
    level_1=req["level_1"]
    incoming=req["incoming"]
    outgoing=req["outgoing"]
    q="INSERT INTO call_level_1(call_id, io_id, level_1)VALUES ('"+str(call_id)+"','"+str(io_id)+"','"+str(level_1)+"');"
    result=db.dbTransactionIUD(q)
    return result
#############################insert level 2 for call level 2
@app.route("/iclevel2",methods=["POST"])
def calleve2():
    thekey_1=request.headers["key_1"]
    if key_1!=thekey_1:
        return jsonify("message:the header key is wrong")
    req=request.get_json()
    call_id=req["call_id"]
    io_id=req["io_id"]
    roc_id=req["roc_id"]
    result_of_convo=req["result_of_convo"]
    q="INSERT INTO call_level_2(call_id, io_id, roc_id, result_of_convo)VALUES('"+str(call_id)+"','"+str(io_id)+"','"+str(roc_id)+"','"+str(result_of_convo)+"');"
    result=db.dbTransactionIUD(q)
    return result
############################# insert level 3 for call level 3
@app.route("/iclevel3",methods=["POST"])
def calleve3():
    thekey_1=request.headers["key_1"]
    if key_1!=thekey_1:
        return jsonify("message:the header key is wrong")
    req=request.get_json()
    call_id=req["call_id"]
    io_id=req['io_id']
    roc_id=req['roc_id']
    reason=req["reason"]
    q="INSERT INTO call_level_3(call_id,io_id,roc_id,reasons)VALUES ('"+str(call_id)+"','"+str(io_id)+"','"+str(roc_id)+"','"+str(reason)+"');"
    result=db.dbTransactionIUD(q)
    return result
######################################################## all select queries for motivator and call 
############################ MOTIVATOT LEVEL 1 select query
@app.route("/slevel1",methods=["GET"])
@jwt_required()
def motivato_level1():
      thekey_1=request.headers["key_1"]
      if key_1!=thekey_1:
          return jsonify("message:the header key is wrong")
      query="SELECT * FROM motivator_level1;"
      result=db.dbTransactionSelect(query)
      return result
################################# MOTIVATOR LEVEL 2 select query
@app.route("/all",methods=["post"])
@jwt_required()
def motivator_level2():
    thekey_1=request.headers["key_1"]
    if key_1!=thekey_1:
        return jsonify("message:the header key is wrong")
    req=request.get_json()
    id_mot1=req["id_mot1"]
    q2="select response from motivator_level2 WHERE id_mot1='"+str(id_mot1)+"';"
    r2=db.dbTransactionSelect(q2)
    return jsonify(r2)
############### CALL - LEVEL-  ################### for retreiving data in level 0
@app.route("/call",methods=["GET"])
@jwt_required()
def calltype():
    thekey_1=request.headers["key_1"]
    if key_1!=thekey_1:
        return jsonify("message:the header key is wrong")
    q="SELECT*FROM call_map_table;"
    result=db.dbTransactionSelect(q)
    return result
############### CALL - LEVEL-  ################### for retreiving data in level 1
@app.route("/call1level",methods=["GET"])
@jwt_required()
def call_level1():
    thekey_1=request.headers["key_1"]
    if key_1!=thekey_1:
        return jsonify("message:the header key is wrong")
    req=request.get_json()
    call_id=req["call_id"]
    q2="SELECT call_id,io_id,level_1 FROM call_level_1 WHERE call_id='"+str(call_id)+"';"
    r2=db.dbTransactionSelect(q2)
    return r2
############### CALL - LEVEL-  ################### for retreiving data in level 2
@app.route("/call2level",methods=["GET"])
@jwt_required()
def call_level2():
    thekey_1=request.headers["key_1"]
    if key_1!=thekey_1:
          return jsonify("message:the header key is wrong")
    req=request.get_json()
    call_id=req['call_id']
    io_id=req['io_id']
    q2="select call_id,io_id,roc_id,result_of_convo FROM call_level_2 WHERE call_id="+str(call_id)+" and io_id="+str(io_id)+";"
    r2=db.dbTransactionSelect(q2)
    return jsonify(r2)
########### CALL - LEVEL-  ################### for retreiving data in level 3
@app.route("/call3level",methods=["GET"])
@jwt_required()
def call_level3():
    thekey_1=request.headers["key_1"]
    if key_1!=thekey_1:
        return jsonify("message:the header key is wrong")
    req=request.get_json()
    call_id=req["call_id"]
    io_id=req["io_id"]
    roc_id=req["roc_id"]
    q2="SELECT call_id,io_id,roc_id,r_id,reasons FROM call_level_3 WHERE call_id='"+str(call_id)+"' and io_id='"+str(io_id)+"' and roc_id="+str(roc_id)+";"
    r2=db.dbTransactionSelect(q2)
    return r2
###########################################################################################################################################
#########register of user is done here 
@app.route("/register",methods=['POST'])
def ins_Data():
    thekey=request.headers["key_2"]
    if key_2!=thekey:
        return jsonify("message:the header key is wrong")
    req=request.get_json()
    user_name=req['user_name']
    mobile_num=req['mobile_num']
    email=req['email']
    password= req['password']
    d_salt=test.getDynamicSalt()
    s_salt=test.staticSalt
    created_date=datetime.datetime.now().strftime("%Y-%m-%d")
    hash_pw=test.generatePassword(password,d_salt)
    inst_data="INSERT INTO emp_user_info_table(user_name,mobile_num,email,hash_pw,d_salt,created_date)VALUES('"+str(user_name)+"','"+str(mobile_num)+"','"+str(email)+"','"+(hash_pw)+"','"+(d_salt)+"','"+str(created_date)+"');"
    result=db.dbTransactionIUD(inst_data)
    return result
#####################################LOGIN###########################################################
@app.route('/login',methods=['POST'])
def login():
    thekey=request.headers["key_2"]
    if key_2!=thekey:
        return jsonify("message:the header key is wrong")
    req=request.get_json()
    user_name=req['user_name']
    text_pw=req['text_pw']
    d_salt_query="SELECT d_salt  FROM emp_user_info_table WHERE user_name='"+str(user_name)+"';"
    d_salt= db.dbTransactionSelect(d_salt_query)
    d_salt=d_salt[0]['d_salt']
    hash_pw_query="SELECT hash_pw FROM emp_user_info_table WHERE user_name='"+str(user_name)+"';"
    hash_pw=db.dbTransactionSelect(hash_pw_query)
    hash_pw=hash_pw[0]['hash_pw']
    user_id_query="SELECT user_id FROM emp_user_info_table WHERE user_name='"+str(user_name)+"';"
    user_id=db.dbTransactionSelect(user_id_query)
    user_id=user_id[0]['user_id']
    check=test.checkPassword(text_pw,hash_pw,d_salt)
    if check==0:
        return "Password provided is wrong"
    nowq=datetime.datetime.now()
    insert1="INSERT INTO user_log (user_id,user_name,log_in)VALUES('"+str(user_id)+"','"+str(user_name)+"','"+str(nowq)+"')"
    result=db.dbTransactionIUD(insert1)
    access_token=create_access_token(identity=user_name,additional_claims={"user_id":user_id})
    refresh_token = create_refresh_token(identity=user_name,additional_claims={"user_id":user_id})
    return jsonify(access_token=access_token,refresh_token=refresh_token)
########################################ACCESSDATA##############################################
@app.route("/protected",methods=["GET"])
@jwt_required()
def prot():
    thekey=request.headers["key_1"]
    if key_1!=thekey:
        return jsonify("message:the header key is wrong")

    current_user=get_jwt_identity()
    user_name=get_jwt_identity()
    select="SELECT user_name,user_id,mobile_num,email,is_active FROM emp_user_info_table WHERE user_name='"+str(user_name)+"';"
    result=db.dbTransactionSelect(select)
    return result
    #return jsonify(logged_in_as=current_user)(result) 

###########################################REFRESH_TOKEN#####################################
@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    thekey=request.headers["key_1"]
    if key_1!=thekey:
        return jsonify("message:the header key is wrong")
    user_name = get_jwt_identity()
    user_id= get_jwt_identity()
    access_token = create_access_token(identity=user_name,additional_claims={"user_id":user_id})
    return jsonify(access_token=access_token)
##########################################LOGOUT##############################################
@app.route("/logout",methods=['GET'])
@jwt_required()
def logout():
    thekey_1=request.headers["key_1"]
    if key_1!=thekey_1:
        return jsonify("message:the header key is wrong")
    thekey_1=request.headers["key_1"]
    if key_1!=thekey_1:
        return jsonify("message:the header key is wrong")
    user_name=get_jwt_identity()
    
    log_out=datetime.datetime.now()
    update2="UPDATE user_log SET log_out='"+str(log_out)+"',is_log_in=false WHERE user_name='"+str(user_name)+"' AND is_log_in=true;"
    result=db.dbTransactionIUD(update2)
    return result

if __name__ == '__main__':
      app.run()