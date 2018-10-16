from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from Plant import plant
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(plant)


def hello_world():
    init_db()
    if (request.method == 'GET'):
        return jsonify(
            hhh = "ddd"
        )
    return ''


def init_db():
    engine = create_engine('mysql+pymysql://root:Floppy9side@localhost:3306/PLNT') #TODO: REMOVE
    connection = engine.connect()
    result = connection.execute("select name from plant")
    for row in result:
        print("name:", row['name'])


if __name__ == '__main__':
    app = Flask(__name__)
    app.run(debug=True)
