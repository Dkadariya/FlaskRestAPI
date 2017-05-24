from flask import Flask, jsonify, request
from dBase import read, write,delete
from dateutil.parser import parse

app = Flask(__name__)

Data = [
    {
        'id': 1,
        'name': u'adam',
        'job': u'Data Analyst', 
        'age': 30
    },
    {
        'id': 2,
        'name': u'jack',
        'job': u'programmer', 
        'age': 27
    }
]

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
def get_tasks(id):
	Data=read(id)
	return jsonify({'contacts': Data})

@app.route('/dbase/v1.0/list/users', methods=['POST'])
def create_task():
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
    write(name, dob, gender, zipCode, otherZip, albuterol, ventolin, proAir, xopenex, atrovent)
    return jsonify({'task': 'done'}), 201

@app.route('/dbase/v1.0/list/users/<int:id>', methods=['DELETE'])
def delete_user(id):
	Data=delete(id)
	return jsonify({'data': Data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
