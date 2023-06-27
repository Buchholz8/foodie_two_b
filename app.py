from flask import Flask, request, jsonify, make_response
import dbcreds, dbhelpers

app = Flask(__name__)


@app.post("/api/client")
def post_client():
    error = dbhelpers.check_endpoint_info(request.json, ["username","email", "password", "image_url", "bio"])
    if(error != None):
        return make_response(jsonify(error), 500)
    results = dbhelpers.run_procedures("CALL insert_client_rid(?,?,?,?,?)", [request.json.get('username'), request.json.get('email'), request.json.get('password'), request.json.get('image_url'), request.json.get('bio')])
    if(type(results) == list):
        return make_response(jsonify({results == "client_id"}), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))





if(dbcreds.production_mode == True):
    print("Runing in production mode")
    app.run(debug=True)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in developer mode")
    app.run(debug=True)