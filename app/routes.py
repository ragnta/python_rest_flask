from app import app
from flask import json, request
from .reader import Reader

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/availabledata',  methods=['GET'])
def get_availabledata():
    return json.dumps(Reader.getListOfData())

@app.route('/postnewdata',  methods=['POST'])
def post_new_data():
    # TODO add BL
    valueFromRequest = request.values.get("something")
    print(f'\t{valueFromRequest}.')
    return json.dumps({"success": True})

@app.route('/getdatabyid',  methods=['GET'])
def get_data_by_id():
    id = request.args.get('id')
    listOfData = Reader.getListOfData()
    for x in listOfData:
        print(f'\t{x}.')
        if x["id"] == id:
           return json.dumps(x)
    return json.dumps({"error": "broken id"})
