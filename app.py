import dbcreds
import dbhelper
import uuid
from flask import Flask, request, make_response, jsonify
app = Flask(__name__)

######## client endpoints ##################
@app.get('/api/client')
def get_client():
    try:
        # using dbhelper.check_endpoint_info to check for required data
        error=dbhelper.check_endpoint_info(request.args,["client_id"])
        if(error != None):
            return make_response(jsonify(error),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results=dbhelper.run_procedure("call get_client(?)",[request.args.get("client_id")])
        # if results return from db as list jsonify results with and return 200
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
        # using dbhelper.check_endpoint_info to check for required data
        error=dbhelper.check_endpoint_info(request.json,["email","first_name","last_name","image_url","username","password"])
        if(error != None):
            return make_response(jsonify(error),400)
        # generating token using uuid
        token=uuid.uuid4().hex
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results=dbhelper.run_procedure("call new_client(?,?,?,?,?,?,?)",
                                       [request.json.get("email"),request.json.get("first_name"),request.json.get("last_name"),
                                        request.json.get("image_url"),request.json.get("username"),request.json.get("password"),token])
        # if results return from db as list jsonify results with and return 200
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
        # using dbhelper.check_endpoint_info to check for the header token 
        header_check=dbhelper.check_endpoint_info(request.headers,["token"])
        # dont check sent data becuase user can send whatever they want to edit
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results=dbhelper.run_procedure("call client_edit(?,?,?,?,?,?,?)",[request.headers.get("token"),request.json.get("email"),request.json.get("first_name"),
                                                              request.json.get("last_name"),request.json.get("image_url"),request.json.get("username"),request.json.get("password")])
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
        # using dbhelper.check_endpoint_info to check for the header token 
        header_check=dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        # using dbhelper.check_endpoint_info to check for required data
        error = dbhelper.check_endpoint_info(request.json,["password"])
        if(error != None):
            return make_response(jsonify(error),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results=dbhelper.run_procedure("call delete_client(?,?)",[request.headers.get("token"),request.json.get("password")])
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

######## client login endpoints ############
@app.post('/api/client-login')
def client_login():
    try:
        # using dbhelper.check_endpoint_info to check for required data
        error=dbhelper.check_endpoint_info(request.json,["email","password"])
        if(error != None):
            return make_response(jsonify(error),400)
        # generating token using uuid
        token = uuid.uuid4().hex
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results=dbhelper.run_procedure("call client_login(?,?,?)",[token,request.json.get("email"),request.json.get("password")])
        # if results return from db as list jsonify results with and return 200
        if(type(results) ==  list):
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

@app.delete('/api/client-login')
def delete_client_login():
    try:
        # using dbhelper.check_endpoint_info to check for the header token 
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
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
        # using dbhelper.check_endpoint_info to check for required data
        error=dbhelper.check_endpoint_info(request.args,["restaurant_id"])
        if(error != None):
            return make_response(jsonify(error),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results=dbhelper.run_procedure("call get_restaurant(?)",[request.args.get("restaurant_id")])
        # if results return from db as list jsonify results with and return 200
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
        # using dbhelper.check_endpoint_info to check for required data
        error=dbhelper.check_endpoint_info(request.json,["email","name","address","phone_number","bio","city","profile_url","banner_url","password"])
        if(error != None):
            return make_response(jsonify(error),400)
        # generating token using uuid
        token=uuid.uuid4().hex
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results=dbhelper.run_procedure("call new_restaurant(?,?,?,?,?,?,?,?,?,?)",
                                       [request.json.get("email"),request.json.get("name"),request.json.get("address"),
                                        request.json.get("phone_number"),request.json.get("bio"),request.json.get("city"),
                                        request.json.get("profile_url"),request.json.get("banner_url"),request.json.get("password"),token])
        # if results return from db as list jsonify results with and return 200
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
        # using dbhelper.check_endpoint_info to check for the header token 
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results=dbhelper.run_procedure("call restaurant_edit(?,?,?,?,?,?,?,?,?,?)",
                                       [request.headers.get("token"),request.json.get("email"),request.json.get("name"),request.json.get("address"),
                                        request.json.get("phone_number"),request.json.get("bio"),request.json.get("city"),
                                        request.json.get("profile_url"),request.json.get("banner_url"),request.json.get("password")])
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
        # using dbhelper.check_endpoint_info to check for the header token 
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        # using dbhelper.check_endpoint_info to check for required data
        error = dbhelper.check_endpoint_info(request.json,["password"])
        if(error != None):
            return make_response(jsonify(error),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results=dbhelper.run_procedure("call delete_restaurant(?,?)",[request.headers.get("token"),request.json.get("password")])
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
@app.post('/api/restaurant-login')
def restaurant_login():
    try:
        # using dbhelper.check_endpoint_info to check for required data
        error = dbhelper.check_endpoint_info(request.json,["email","password"])
        if(error != None):
            return make_response(jsonify(error),400)
        # generating token using uuid
        token=uuid.uuid4().hex
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results = dbhelper.run_procedure("call restaurant_login(?,?,?)",[token,request.json.get("email"),request.json.get("password")])
        # if results return from db as list jsonify results with and return 200
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

@app.delete('/api/restaurant-login')
def delete_restaurant_login():
    try:
        # using dbhelper.check_endpoint_info to check for the header token 
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
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
        # setting results variable as dbhelper.run_procedure calling procedure with empty data
        results=dbhelper.run_procedure("call get_all_restaurants()",[])
        # if results return from db as list jsonify results with and return 200
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
        # using dbhelper.check_endpoint_info to check for required data
        error = dbhelper.check_endpoint_info(request.args,["restaurant_id"])
        if(error != None):
            return make_response(jsonify(error),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results =  dbhelper.run_procedure("call get_menu(?)",[request.args.get("restaurant_id")])
        # if results return from db as list jsonify results with and return 200
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
def new_menu():
    try:
        # using dbhelper.check_endpoint_info to check for the header token 
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        # using dbhelper.check_endpoint_info to check for required data
        error = dbhelper.check_endpoint_info(request.json,["description","image_url","name","price"])
        if(error != None):
            return make_response(jsonify(error),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results = dbhelper.run_procedure("call new_menu(?,?,?,?,?)",[request.headers.get("token"),request.json.get("description"),request.json.get("image_url"),request.json.get("name"),request.json.get("price"),])
        # if results return from db as list jsonify results with and return 200
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
        # using dbhelper.check_endpoint_info to check for the header token 
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        # using dbhelper.check_endpoint_info to check for required data
        error = dbhelper.check_endpoint_info(request.json,["menu_id"])
        if(error != None):
            return make_response(jsonify(error),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results = dbhelper.run_procedure("call menu_edit(?,?,?,?,?,?)",[request.headers.get("token"),request.json.get("menu_id"),request.json.get("description"),request.json.get("image_url")
                                         ,request.json.get("name"),request.json.get("price")])
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
        # using dbhelper.check_endpoint_info to check for the header token 
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results = dbhelper.run_procedure("call delete_menu(?,?)",[request.headers.get("token"),request.json.get("menu_id")])
        if(results == None):
            return make_response("delete successful",200)
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
def get_client_order():
    try:
        # using dbhelper.check_endpoint_info to check for the header token 
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results = dbhelper.run_procedure("call get_client_order(?,?,?)",[request.headers.get("token"),request.args.get("is_confirmed"),request.args.get("is_complete")])
        # if results return from db as list jsonify results with and return 200
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("something went wrong",400)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again")

@app.post('/api/client-order')
def new_client_order():
    try:
        # using dbhelper.check_endpoint_info to check for the header token 
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        # using dbhelper.check_endpoint_info to check for required data
        error = dbhelper.check_endpoint_info(request.json,["menu_items","restaurant_id"])
        if(error != None):
            return make_response(jsonify(header_check),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results = dbhelper.run_procedure("call new_client_order(?,?,?)",[request.headers.get("token"),request.json.get("menu_items"),request.json.get("restaurant_id")])
        if(results == None):
            return make_response("new order successful",200)
        else:
            return make_response("something went wrong",400)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again")

######## restaurant order endpoints ########
@app.get('/api/restaurant-order')
def get_restaurant_order():
    try:
        # using dbhelper.check_endpoint_info to check for the header token 
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results = dbhelper.run_procedure("call get_restaurant_order(?,?,?)",[request.headers.get("token"),request.json.get("is_confirmed"),request.json.get("is_complete")])
        # if results return from db as list jsonify results with and return 200
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("something went wrong",400)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again")

@app.patch('/api/restaurant-order')
def patch_restaurant_order():
    try:
        # using dbhelper.check_endpoint_info to check for the header token 
        header_check = dbhelper.check_endpoint_info(request.headers,["token"])
        if(header_check != None):
            return make_response(jsonify(header_check),400)
        # using dbhelper.check_endpoint_info to check for required data
        error =  dbhelper.check_endpoint_info(request.json,["restaurant_id"])
        if(error != None):
            return make_response(jsonify(header_check),400)
        # setting results variable as dbhelper.run_procedure calling procedure with data
        results = dbhelper.run_procedure("call patch_restaurant_order(?,?,?,?)",[request.headers.get("token"),request.json.get("restaurant_id"),request.json.get("is_confirmed"),request.json.get("is_complete")])
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







if(dbcreds.production_mode == True):
    print("Running Production Mode")
    import bjoern #type: ignore
    bjoern.run(app,"0.0.0.0",5000)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode")
    app.run(debug=True)
