################################################################################
# Author: Dipesh Kadariya      <dipeshk2015@gmail.com>
################################################################################
from flask import Flask, jsonify, request
from dBase import read_usrs, write_usrs,delete_usrs,write_qtns
from dateutil.parser import parse

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

#@app.route('/dbase/v1.0/list/<int:id>', methods=['GET'])
#def get_tasks(id):
#    task = [task for task in Data if task['id'] == id]
#    if len(task) == 0:
#        abort(404)
#    return jsonify({'data': task[0]})

#@app.route('/dbase/v1.0/list', methods=['GET'])
#def get_tasks():
#    return jsonify({'data': Data})

@app.route('/dbase/v1.0/list/users/<int:id>', methods=['GET'])
def get_users(id):
	Data=read_usrs(id)
	return jsonify({'contacts': Data})

@app.route('/dbase/v1.0/list/users', methods=['POST'])
def add_users():
    if not request.json or not 'name' in request.json:
        abort(400)
    name =request.json['name']
    dob = request.json['dob']
    gender = request.json['gender']
    zipCode = request.json['zip']
    otherZip = request.json['otherZip']
    albuterol = request.json['albuterol']
    ventolin = request.json['ventolin']
    proAir = request.json['proAir']
    xopenex = request.json['xopenex']
    atrovent = request.json['atrovent']
    parse(dob).strftime("%Y-%m-%d")
    print name,dob,gender,zipCode,otherZip,albuterol,atrovent,proAir,xopenex
    write_usrs(name, dob, gender, zipCode, otherZip, albuterol, ventolin, proAir, xopenex, atrovent)
    return jsonify({'task': 'done'}), 201

@app.route('/dbase/v1.0/list/users/<int:id>', methods=['DELETE'])
def delete_user(id):
	Data=delete_usrs(id)
	return jsonify({'data': Data})

@app.route('/dbase/v1.0/list/questions', methods=['POST'])
def add_ans():
    name =request.json['user']
    ans =[[request.json['ans1'],request.json['q1_id']],[request.json['ans2'],request.json['q2_id']]]
    tmstp =request.json['timeStamp']
    Data=write_qtns(name,ans,tmstp)

    print ans, tmstp
    return jsonify({'contacts': "Data"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
