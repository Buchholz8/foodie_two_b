from flask import Flask, request, jsonify, make_response
import dbcreds, dbhelpers

app = Flask(__name__)
##Client Handlers
@app.post("/api/client")
def post_client():
    error = dbhelpers.check_endpoint_info(request.json, ["username","email", "password", "img_url", "bio", "first_name" , "last_name"])
    if(error != None):
        return make_response(jsonify(error), 500)
    results = dbhelpers.run_procedures("CALL client_post(?,?,?,?,?,?,?)", [request.json.get('username'), request.json.get('email'), request.json.get('password'), request.json.get('img_url'), request.json.get('bio'), request.json.get('first_name'), request.json.get('last_name')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))
    
@app.get("/api/client")
def get_client():
    results = dbhelpers.run_procedures("CALL client_get()", [])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))

@app.patch("/api/client")
def patch_client():
    error = dbhelpers.check_endpoint_info(request.json, ["username","email", "img_url", "bio", "first_name" , "last_name","password_input", "username_input"])
    if(error != None):
        return make_response(jsonify(error), 500)
    results = dbhelpers.run_procedures("CALL client_patch(?,?,?,?,?,?,?)", [request.json.get('username'), request.json.get('email'), request.json.get('password'), request.json.get('img_url'), request.json.get('bio'), request.json.get('first_name'), request.json.get('last_name')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))

@app.delete("/api/client")
def delete_client():
    client_password_input = request.json.get("password")
    results = dbhelpers.run_procedures("CALL client_delete(?)", [client_password_input] )
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))
##End of Client Handlers
##Client Login Handlers
@app.post("/api/client-login")
def post_client():
    error = dbhelpers.check_endpoint_info(request.json, ["username","password"])
    token = dbhelpers.generate_token()
    if(error != None):
        return make_response(jsonify(error), 500)
    results = dbhelpers.run_procedures("CALL client_login_post(?,?,?)", [request.json.get('username'), request.json.get('password'), token])
    if(type(token) == str):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))
    
@app.delete("/api/client-login")
def post_client():
    error = dbhelpers.check_endpoint_info(request.json, ["password"])
    if(error != None):
        return make_response(jsonify(error), 500)
    results = dbhelpers.run_procedures("CALL client_login_delete(?)", [request.json.get('password')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))
##End of Client Login Handlers
##restaurant handlers
@app.post("/api/restaurant")
def post_restaurant():
    error = dbhelpers.check_endpoint_info(request.json, ["name","address","phone_number","bio", "password","email", "city", "profile_url", "banner_url"])
    if(error != None):
        return make_response(jsonify(error), 500)
    results = dbhelpers.run_procedures("CALL restaurant_pos(?,?,?,?,?,?,?,?,?)", [request.json.get('name'), request.json.get('address'), request.json.get('phone_number'), request.json.get('bio'), request.json.get('password'), request.json.get('email'), request.json.get('city'), request.json.get('profile_url'), request.json.get('banner_url')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))
    
@app.get("/api/restaraunt")
def get_restaurant():
    results = dbhelpers.run_procedures("CALL restaurant_get()", [])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))

@app.patch("/api/restaurant")
def patch_client():
    error = dbhelpers.check_endpoint_info(request.json, ["name","address","phone_number","bio", "password","email", "city", "profile_url", "banner_url"])
    if(error != None):
        return make_response(jsonify(error), 500)
    results = dbhelpers.run_procedures("CALL restaurant_patch(?,?,?,?,?,?,?,?,?)", [request.json.get('name'), request.json.get('address'), request.json.get('phone_number'), request.json.get('bio'), request.json.get('password'), request.json.get('email'), request.json.get('city'), request.json.get('profile_url'), request.json.get('banner_url')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))

@app.delete("/api/restaurant")
def delete_restaurant():
    restaurant_password_input = request.json.get("password")
    results = dbhelpers.run_procedures("CALL restaurant_delete(?)", [restaurant_password_input] )
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))
## end of restaurant handlers
## Restaurant login handlers
@app.post("/api/restaurant-login")
def post_client():
    error = dbhelpers.check_endpoint_info(request.json, ["email","password"])
    token = dbhelpers.generate_token()
    if(error != None):
        return make_response(jsonify(error), 500)
    results = dbhelpers.run_procedures("CALL restaurant_login_post(?,?,?)", [request.json.get('email'), request.json.get('password'), token])
    if(type(token) == str):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))
    
@app.delete("/api/restaurant-login")
def post_client():
    error = dbhelpers.check_endpoint_info(request.json, ["password"])
    if(error != None):
        return make_response(jsonify(error), 500)
    results = dbhelpers.run_procedures("CALL restaurant_login_delete(?)", [request.json.get('password')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))
##end of restaurant login handlers
## Restarants hnadler
@app.get("/api/restaraunts")
def get_restaurant():
    restaurant_search = request.args.get("name_input")
    results = dbhelpers.run_procedures("CALL restaurants_get(?)", [restaurant_search])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))
##end of restaurants handler
if(dbcreds.production_mode == True):
    print("Runing in production mode")
    app.run(debug=True)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in developer mode")
    app.run(debug=True)