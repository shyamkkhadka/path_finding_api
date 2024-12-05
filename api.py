import json
import csv
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import Response

app = Flask("path")
CORS(app, resources={r"/*": {"origins": "http://demodev.responsible-internet.org"}})


@app.route('/paths/<int:asn>', methods=['GET'])
def get_path_by_asn(asn: int):
    path = get_path(asn)
    if path is None:
        return jsonify({ 'error': 'Path from that source asn does not exist'}), 404
    return jsonify(path)

def get_path(asn):
    if asn == 15625:
        csvFilePath = "/home/shyam/path_finding/ing.csv"
        data = get_json_from_csv(csvFilePath)
    elif asn == 15916:
        csvFilePath = "/home/shyam/path_finding/abn.csv"
        data = get_json_from_csv(csvFilePath)
    elif asn == 40985:
        csvFilePath = "/home/shyam/path_finding/eneco.csv"
        data = get_json_from_csv(csvFilePath)
    else:
        data = { 'error': 'Invalid input'}
    return data

def get_json_from_csv(csvFilePath):
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['No']
            data[key] = rows
    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
