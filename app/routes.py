from app import app
from flask import json, request
from flask_cors import CORS, cross_origin
from .reader import Reader

cors = CORS(app)

@cross_origin()
@app.route('/availabledata',  methods=['GET'])
def get_availabledata():
    return json.dumps(Reader.getListOfData())

@cross_origin()
@app.route('/postnewdata',  methods=['POST'])
def post_new_data():
    # TODO add BL
    valueFromRequest = request.values.get("something")
    print(f'\t{valueFromRequest}.')
    return json.dumps({"success": True})

@cross_origin()
@app.route('/getdatabyid',  methods=['GET'])
def get_data_by_id():
    id = request.args.get('id')
    listOfData = Reader.getListOfData()
    for x in listOfData:
        print(f'\t{x}.')
        if x["id"] == id:
           return json.dumps(x)
    return json.dumps({"error": "broken id"})
