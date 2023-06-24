import dbcreds
import dbhelper
import uuid
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)
######## client endpoints ##################
@app.get('/api/client')
def get_client():
    try:
        error=dbhelper.check_endpoint_info(request.json,["client_id"])
        if(error != None):
            return make_response(jsonify(error),400)
        results=dbhelper.run_procedure("call get_client(?)",[request.json.get("client_id")])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 

@app.post('/api/client')
def new_client():
    try:
        error=dbhelper.check_endpoint_info(request.json,["email","first_name","last_name","image_url","username","password"])
        if(error != None):
            return make_response(jsonify(error),400)
        token=uuid.UUID.hex()
        results=dbhelper.run_procedure("call new_client(?,?,?,?,?,?,?)",
                                       [request.json.get("email"),request.json.get("first_name"),request.json.get("last_name"),
                                        request.json.get("image_url"),request.json.get("username"),request.json.get("password"),token])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors   
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 
@app.patch('/api/client')
def client_edit():
    try:
        header_check=dbhelper.check_endpoint_info(request.headers,["token"])
        # dont check sent data becuase user can send whatever they want to edit
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        results=dbhelper.run_procedure("call client_edit(?)",[request.headers.get("token"),request.json.get("email"),request.json.get("first_name")
                                                              ,request.json.get("last_name"),request.json.get("image_url"),request.json.get("username"),request.json.get("password")])
        if(results ==  None):
            return make_response("edit successful",200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 
@app.delete('/api/client')
def delete_client():
    try:
        error = dbhelper.check_endpoint_info(request.json,["username","password"])
        if(error != None):
            return make_response(jsonify(error),400)
        token=uuid.UUID.hex()
        results=dbhelper.run_procedure("call client_login(?,?)",[request.headers.get("username"),request.json.get("password"),token])
        if(type(results) ==  list):
            return make_response("login successful",200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 

######## client login endpoints ############
@app.post('/api/client-login')
def client_login():
    try:
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        error=dbhelper.check_endpoint_info(request.json,["password"])
        if(error != None):
            return make_response(jsonify(error),400)
        results=dbhelper.run_procedure("call delete_client(?,?)",request.headers.get("token"),request.json.get("password"))
        if(results ==  None):
            return make_response("delete successful",200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 
@app.delete('/api/client-login')
def delete_client_login():
    try:
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        results=dbhelper.run_procedure("call delete_client_login(?)",[request.headers.get("token")])
        if(results ==  None):
            return make_response("logged out",200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 

######## restaurant endpoints ##############
@app.get('/api/restaurant')
def get_restaurant():
    try:
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        results=dbhelper.run_procedure("call get_restaurant(?)",[request.headers.get("token")])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 
    
@app.post('/api/restaurant')
def new_restaurant():
    try:
        error=dbhelper.check_endpoint_info(request.json,["email","name","address","phone_number","bio","city","profile_url","banner_url","password"])
        if(error != None):
            return make_response(jsonify(error),400)
        token=uuid.UUID.hex()
        results=dbhelper.run_procedure("call new_restaurant(?,?,?,?,?,?,?,?,?,?)",
                                       [request.json.get("email"),request.json.get("name"),request.json.get("address"),
                                        request.json.get("phone_number"),request.json.get("bio"),request.json.get("city"),
                                        request.json.get("profile_url"),request.json.get("banner_url"),request.json.get("password"),token])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors   
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 

@app.patch('/api/restaurant')
def restaurant_edit():
    try:
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        results=dbhelper.run_procedure("call restaurant_edit(?,?,?,?,?,?,?,?,?,?)",
                                       [request.json.get("email"),request.json.get("name"),request.json.get("address"),
                                        request.json.get("phone_number"),request.json.get("bio"),request.json.get("city"),
                                        request.json.get("profile_url"),request.json.get("banner_url"),request.json.get("password"),
                                        request.headers.get("token")])
        if(results == None):
            return make_response("edit successful",200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors   
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 

@app.delete('/api/restaurant')
def delete_restaurant():
    try:
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        results=dbhelper.run_procedure("call delete_restaurant(?)"[request.headers.get("token")])
        if(results == None):
            return make_response("delete successful",200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors   
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 

######## restaurant login endpoints ########
@app.post('/api/restuarant-login')
def restaurant_login():
    try:
        error = dbhelper.check_endpoint_info(request.json,["email","password"])
        if(error != None):
            return make_response(jsonify(error),400)
        results = dbhelper.run_procedure("call restaurant_login(?,?)",[request.json.get("email"),request.json.get("password")])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again")
@app.delete('/api/restuarant-login')
def delete_restaurant_login():
    try:
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        results = dbhelper.run_procedure("call delete_restaurant_login(?)",[request.headers.get("token")])
        if(results == None):
            return make_response("successful logout",200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again")
        

######## restaurants get endpoint ##########
@app.get('/api/restaurants')
def get_all_restaurants():
    try:
        results=dbhelper.run_procedure("call get_all_restaurants()",[])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 

######## menu endpoints ####################
@app.get('/api/menu')
def get_menu():
    try:
        error = dbhelper.check_endpoint_info(request.json,["restaurant_id"])
        if(error != None):
            return make_response(jsonify(error),400)
        results =  dbhelper.run_procedure("call get_menu")
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again")

@app.post('/api/menu')
def newmenu():
    try:
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        error = dbhelper.check_endpoint_info(request.json,["description","image_url","name","price"])
        if(error != None):
            return make_response(jsonify(error),400)
        results = dbhelper.run_procedure
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again")
@app.patch('/api/menu')
def menu_edit():
    try:
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        results = dbhelper.run_procedure("call menu_edit(?,?,?,?,?)",request.headers.get("token"),request.json.get("description"),request.json.get("image_url")
                                         ,request.json.get("name"),request.json.get("price"))
        if(results == None):
            return make_response("edit successful",200)
        else:
            return make_response("something went wrong",400)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again")

@app.delete('/api/menu')
def delete_menu():
    try:
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        results = dbhelper.run_procedure("call delete_menu(?,?)",request.headers.get("token"),request.json.get("menu_id"))
        if(results == None):
            return make_response("edit successful",200)
        else:
            return make_response("something went wrong",400)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again")
######## client order endpoints ############
@app.get('/api/client-order')
@app.post('/api/client-order')
######## restaurant order endpoints ########
@app.get('/api/restaurant-order')
@app.patch('/api/restaurant-order')






if(dbcreds.production_mode == True):
    print("Running Production Mode")
    import bjoern #type: ignore
    bjoern.run(app,"0.0.0.0",5000)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode")
    app.run(debug=True)
