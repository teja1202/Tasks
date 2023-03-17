from flask import Flask,request,jsonify
import json
import new_my_task_.dbnewtask as db

app=Flask(__name__)
###########################################################http://127.0.0.1:5000/all
@app.route("/all",methods=["get"])
def motivation():
    data=request.get_json()
    return jsonify (data)
###########################################################http://127.0.0.1:5000/call
###########################################################http://127.0.0.1:5000/motivation
@app.route("/<t>",methods=["GET"])
def type(t):
     
    data=request.get_json()
    if t=="call":
          con=data[0][t]
    elif t=="motivation":
          con=data[1][t]
    req=[]
    for i in con:
          for y in i:
               req.append({"type":y})
    return jsonify(req)
####################################################################################################################
##########################################################MOTIVATION##################################################
#########################################################################################################
@app.route("/motivation/<f>",methods=["GET"])
def motivation_level1(f):
     
      data=request.get_json()
      con=data[1]["motivation"]
      req=[]
      if f=="money":
            mon=con[0][f]
      elif f=="property":
            mon=con[1][f]
      elif f=="reputation":
            mon=con[2][f]
      elif f=="status":
            mon=con[3][f]
      elif f=="fraud":
            mon=con[4][f]
      elif f=="relative":
            mon=con[5][f]
      elif f=="didint use arugement":
            mon=con[6][f]
      
      for i in mon:
              
            req.append(i)  
      return jsonify(req)
#####################################################################################################################
##########################################################call level 1#################################################
########################################################################################################################
@app.route("/call/<f>",methods=["GET"])
def call_level1(f):
      data=request.get_json()
      con=data[0]["call"]
      req=[]
      if f=="incoming":
            mon=con[0][f]
            for i in mon :
                  req.append(i)
      if f=="outgoing":
            mon=con[1][f]
      
            for i in mon:
                  for y in i:
                        req.append({"type":y})
      return jsonify(req)
#####################################################################################################################
###########################################################call level 2##############################################
#########################################################################################################################
@app.route("/call/outgoing/<f>",methods=["GET"])
def call_level2(f):
      data=request.get_json()
      req=[]
      con=data[0]["call"]
      mon=con[1]["outgoing"]
      if f=="negativetype":
            gon=mon[0][f]
            for i in gon:
                  req.append(i)
      elif f=="unknownperson":
            gon=mon[1][f]
            for i in gon:
                  req.append(i)
      elif f=="client":
            gon=mon[2][f]
            for i in gon:
                  for y in i :
                 
                   req.append({"type":y})
      elif f=="husbandorwife":
            gon=mon[3][f]
            for i in gon:
                  for y in i:
                   req.append({"type":y})
      elif f=="parents":
            gon=mon[4][f]
            for i in gon:
                  for y in i:
                        req.append({"type":y})
      elif f=="son or daughter":
            gon=mon[5][f]
            for i in gon:
                  for y in i:
                        req.append({"type":y})
      elif f=="friend or girlfriend":
            gon=mon[6][f]
            for i in gon:
                  for y in i:
                        req.append({"type":y})
      elif f=="another relative":
            gon=mon[7][f]
            for i in gon:
                  req.append(i)
      elif f=="collegue":
            gon=mon[8][f]
            for i in gon:
                  req.append(i)
      elif f=="familiar":
            gon=mon[9][f]
            for i in gon:
                  req.append(i)
      elif f=="third party knowing client":
            gon=mon[10][f]
            for i in gon:
                  req.append(i)
      
      return jsonify(req)
###########################################################################################################################
########################################################level3(client)######################################################
##################################################################################################################################
@app.route("/call/outgoing/client/<f>",methods=["GET"])
def call_level3(f):
      data=request.get_json()
      req=[]
      con=data[0]["call"]
      mon=con[1]["outgoing"]
      gon=mon[2]["client"]
      if f=="promise of pay":
            ton=gon[0][f]
            for i in ton:
                  req.append(i)
      if f=="refused to pay":
            ton=gon[1][f]
            for i in ton:
                  req.append(i)
      return jsonify(req)
##################################################################################################################################
#######################################################level(husband or wife)####################################################
#################################################################################################################################
@app.route("/call/outgoing/husbandorwife/<f>",methods=["GET"])
def husbandorwifel3(f):
      data=request.get_json()
      req=[]
      con=data[0]["call"]
      mon=con[1]["outgoing"]
      gon=mon[3]["husbandorwife"]
      if f=="promise of pay":
            ton=gon[0][f]
            for i in ton:
                  req.append(i)
      if f=="refused to pay":
            ton=gon[1][f]
            for i in ton:
                  req.append(i)
      return jsonify(req)
###################################################################################################################################
#################################################################level3(parents)###################################################
####################################################################################################################################
@app.route("/call/outgoing/parents/<f>",methods=["GET"])
def parentsl3(f):
      data=request.get_json()
      req=[]
      con=data[0]["call"]
      mon=con[1]["outgoing"]
      gon=mon[4]["parents"]
      if f=="promise of pay":
            ton=gon[0][f]
            for i in ton:
                  req.append(i)
      if f=="refused to pay":
            ton=gon[1][f]
            for i in ton:
                  req.append(i)
      return jsonify(req)
#########################################################################################################################################
#################################################################level3(son or daughter)################################################
#########################################################################################################################################
@app.route("/call/outgoing/son or daughter/<f>",methods=["GET"])
def sonordaughterl3(f):
      data=request.get_json()
      req=[]
      con=data[0]["call"]
      mon=con[1]["outgoing"]
      gon=mon[5]["son or daughter"]
      if f=="promise of pay":
            ton=gon[0][f]
            for i in ton:
                  req.append(i)
      if f=="refused to pay":
            ton=gon[1][f]
            for i in ton:
                  req.append(i)
      return jsonify(req)
########################################################################################################################################
##################################################################level3(friend or girlfriend)#########################################
#######################################################################################################################################
@app.route("/call/outgoing/friend or girlfriend/<f>",methods=["GET"])
def fogfl3(f):
      data=request.get_json()
      req=[]
      con=data[0]["call"]
      mon=con[1]["outgoing"]
      gon=mon[6]["friend or girlfriend"]
      if f=="promise of pay":
            ton=gon[0][f]
            for i in ton:
                  req.append(i)
      if f=="refused to pay":
            ton=gon[1][f]
            for i in ton:
                  req.append(i)
      return jsonify(req)
#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################
#################### A P I'S + D A T A B A S E



if __name__ == '__main__':
      app.run()



