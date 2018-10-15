from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/plant')
def hello_world():
    init_db()
    if (request.method == 'GET'):
        return jsonify(
            hhh = "ddd"
        )
    return ''

def init_db():
    engine = create_engine('mysql+pymysql://root:ffff@localhost:3306/PLNT')
    connection = engine.connect()
    result = connection.execute("select name from plant")
    for row in result:
        print("name:", row['name'])

if __name__ == '__main__':
    app.run()
