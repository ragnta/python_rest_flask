from app import app
from flask import json, request, jsonify
from flask_cors import CORS, cross_origin
from .reader import Reader
from .controllers import Admin
# this file contains every route. It defines a REST interface for communicate with the client (eg.: browser)
# cors see https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
cors = CORS(app)

# you can get all data by http://<ipadress>:<port:default:5000>/availabledata
@cross_origin()
@app.route('/availabledata',  methods=['GET'])
def get_availabledata():
    all_vehicles = [x.asdict() for x in app.admincontrol.getAllElement()]
    return json.dumps(all_vehicles)

@cross_origin()
@app.route('/postnewdata',  methods=['POST'])
def post_new_data():
    # TODO add BL
    valueFromRequest = request.values.get("something")
    print(f'\t{valueFromRequest}.')
    return json.dumps({"success": True})

# you can get a data by http://<ipadress>:<port:default:5000>/getdatabyid?id=<id>
@cross_origin()
@app.route('/getdatabyid',  methods=['GET'])
def get_data_by_id():
    id = request.args.get('id')
    listOfData = Reader.getListOfData()
    for x in listOfData:
        if x["id"] == id:
           return json.dumps(x)
    return json.dumps({"error": "broken id"})
