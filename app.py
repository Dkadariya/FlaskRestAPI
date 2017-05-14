from flask import Flask, jsonify, request


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

@app.route('/dbase/v1.0/list', methods=['GET'])
def get_tasks():
    return jsonify({'data': Data})


@app.route('/dbase/v1.0/list', methods=['POST'])
def create_task():
    if not request.json or not 'name' in request.json:
        abort(400)
    task = {
        'id': Data[-1]['id'] + 1,
        'name': request.json['name'],
        'job': request.json.get('job', ""),
        'age': False
    }
    Data.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
