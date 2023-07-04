from flask import Flask, request, jsonify, make_response
import dbcreds, dbhelpers

app = Flask(__name__)
##Client Handlers
@app.post("/api/client")
def post_client():
    error = dbhelpers.check_endpoint_info(request.json, ["username","password", "img_url", "bio", "email", "first_name" , "last_name"])
    if(error != None):
        return make_response(jsonify(error), 500)
    results = dbhelpers.run_procedures("CALL client_post(?,?,?,?,?,?,?)", [request.json.get('username'), request.json.get('password'), request.json.get('img_url'), request.json.get('bio'), request.json.get('email'), request.json.get('first_name'), request.json.get('last_name')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))
    
@app.get("/api/client")
def get_client():
    token = request.args.get("token")
    results = dbhelpers.run_procedures("CALL client_get(?)", [token])
    if isinstance(results, list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("Sorry, something went wrong"), 500)
@app.patch("/api/client")
def patch_client():
    error = dbhelpers.check_endpoint_info(request.json, ["username", "email", "img_url", "bio", "first_name", "last_name", "password_input", "username_input"])
    if error:
        return make_response(jsonify(error), 500)
    
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    img_url = request.json.get('img_url')
    bio = request.json.get('bio')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    
    results = dbhelpers.run_procedures("CALL client_patch(?,?,?,?,?,?,?,?)", [username, email, password, img_url, bio, first_name, last_name, username_input])
    
    if isinstance(results, list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("Sorry, something went wrong"), 500)


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
def post_client_login():
    token = dbhelpers.generate_token()
    error = dbhelpers.check_endpoint_info(request.json, ["email","password"])
    
    if(error != None):
        return make_response(jsonify(error), 500)
    results = dbhelpers.run_procedures("call client_login_post(?,?,?)", [request.json.get('email'), request.json.get('password'), token])
    if (type(token) == str):
        return make_response(jsonify({'token': token}, results), 200)
    elif (type(results) == list):
        return make_response(jsonify(results) , 200)
    else:
        return make_response(jsonify('Sorry, something went wrong'))
    
@app.delete("/api/client-login")
def delete_client_login():
    token_input = request.json.get("token_input")
    results = dbhelpers.run_procedures("CALL client_login_delete(?)", [token_input])
    
    if (type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("Sorry, something went wrong"), 500)
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
    
@app.get("/api/restaurant")
def get_restaurant():
    token = request.args.get("token")
    results = dbhelpers.run_procedures("CALL restaurant_get(?)", [token])
    
    if isinstance(results, list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("Sorry, something went wrong"), 500)


@app.patch("/api/restaurant")
def patch_restaurant():
    data = request.json
    error = dbhelpers.check_endpoint_info(data, ["name", "address", "phone_number", "bio", "password", "email", "city", "profile_url", "banner_url"])
    if error:
        return make_response(jsonify(error), 500)
    
    params = [
        data.get('name'),
        data.get('address'),
        data.get('phone_number'),
        data.get('bio'),
        data.get('password'),
        data.get('email'),
        data.get('city'),
        data.get('profile_url'),
        data.get('banner_url')
    ]
    
    results = dbhelpers.run_procedures("CALL restaurant_patch(?,?,?,?,?,?,?,?,?)", params)
    if isinstance(results, list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("Sorry, something went wrong"), 500)


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
def post_restaurant_login():
    token = dbhelpers.generate_token()
    error = dbhelpers.check_endpoint_info(request.json, ["email","password"])
    if(error != None):
        return make_response(jsonify(error), 500)
    results = dbhelpers.run_procedures("CALL restaurant_login_post(?,?,?)", [request.json.get('email'), request.json.get('password'), token])
    if (type(token) == str):
        return make_response(jsonify({'token': token}, results), 200)
    elif (type(results) == list):
        return make_response(jsonify(results) , 200)
    else:
        return make_response(jsonify('Sorry, something went wrong'))
@app.delete("/api/restaurant-login")
def delete_restaurant_login():
    token_input = request.json.get("token_input")
    results = dbhelpers.run_procedures("CALL restaurant_login_delete(?)", [token_input])
    
    if isinstance(results, list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("Sorry, something went wrong"), 500)

##end of restaurant login handlers
## Restarants hnadler
@app.get("/api/restaraunts")
def get_restaurants():
    restaurant_search = request.args.get("name_input")
    results = dbhelpers.run_procedures("CALL restaurants_get(?)", [restaurant_search])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))
##end of restaurants handler
## Menu Handlers
@app.post("/api/menu")
def post_menu():
    error = dbhelpers.check_endpoint_info(request.json, ["name","price","description", "img_url", "restaurant_id"])
    if(error != None):
        return make_response(jsonify(error), 500)
    results = dbhelpers.run_procedures("CALL menu_post(?,?,?,?,?)", [request.json.get('name'), request.json.get('price'), request.json.get('description'), request.json.get('img_url'), request.json.get('restaurant_id')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))
    
@app.get("/api/menu")
def get_menu():
    results = dbhelpers.run_procedures("CALL menu_get()", [])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))

@app.patch("/api/menu")
def patch_menu():
    error = dbhelpers.check_endpoint_info(request.json, ["name","price","description","img_url"])
    if(error != None):
        return make_response(jsonify(error), 500)
    results = dbhelpers.run_procedures("CALL menu_patch(?,?,?,?)", [request.json.get('name'), request.json.get('rice'), request.json.get('description'), request.json.get('img_url')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))

@app.delete("/api/menu")
def delete_menu():
    menu_id_input = request.json.get("id")
    results = dbhelpers.run_procedures("CALL menu_delete(?)", [menu_id_input] )
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))
##end of menu handlers
## Client Order handlers
@app.post("/api/client-order")
def post_client_order():
    error = dbhelpers.check_endpoint_info(request.json, ["item_id", "token", "restaurant_id"])
    if error is not None:
        return make_response(jsonify(error), 500)

    results = dbhelpers.run_procedures("CALL client_order_post(?, ?, ?)", [
        request.json.get('item_id'),
        request.json.get('token'),
        request.json.get('restaurant_id')
    ])

    if type(results) == list:
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("Sorry, something went wrong"), 500)

    
@app.get("/api/client-order")
def get_client_order():
    order_id = request.args.get('order_id')
    if order_id is not None:
        results = dbhelpers.run_procedures("CALL client_order_get(?)", [int(order_id)])
        if type(results) == list:
            return make_response(jsonify(results), 200)
    return make_response(jsonify("Sorry, something went wrong"), 500)

##end of order handlers
## Restaurant Order Handlers
@app.patch("/api/restaurant-order")
def patch_rest_order():
    error = dbhelpers.check_endpoint_info(request.json, ["name","price","description","img_url"])
    if(error != None):
        return make_response(jsonify(error), 500)
    results = dbhelpers.run_procedures("CALL restaurant_order_patch(?,?,?,?)", [request.json.get('name'), request.json.get('price'), request.json.get('description'), request.json.get('img_url')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))
    
@app.get("/api/restaurant-order")
def get_rest_order():
    rest_id = request.args.get("restaurant_id")
    order_id = request.args.get("order_id")
    results = dbhelpers.run_procedures("CALL restaurant-order_get()", [rest_id , order_id])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"))
##end of restaurant order handlers


if dbcreds.production_mode == True:
    print("Running in production mode")
    app.run(debug=True)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in developer mode")
    app.run(debug=True)
