from flask import Flask,jsonify
app = Flask(__name__)

tasks = [
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

@app.route('/dbase/v1.0/list', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
