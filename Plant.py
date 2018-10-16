from flask import Flask, request, jsonify, Blueprint
from sqlalchemy import create_engine
import json

plant = Blueprint('plant', __name__)


# Get plant route
# TODO: strip database stuff into its own utility file
@plant.route("/plant")
def get_plant():
    engine = create_engine('mysql+pymysql://root:Floppy9side@localhost:3306/PLNT')  # TODO: REMOVE
    connection = engine.connect()
    query = connection.execute("select * from plant")
    result_rows = query.fetchall()
    row_headers = [x for x in query._metadata.keys]
    json_result = format_output(row_headers, result_rows)
    return jsonify(json_result)


#formats data into json string, need to adjust for nested data
def format_output(row_headers, results):
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result)))
    return json_data[0]