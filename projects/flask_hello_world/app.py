#OLD VERSION FOR TESTING 

#from flask import Flask        # import Flask's core class

#app = Flask(__name__)          # create the app; __name__ tells Flask where it's running from

#@app.route('/')                # decorator: map URL path '/' to the function below
#def home():                    # this function runs when someone visits '/'
#    return "Hello, Ali!"       # whatever this returns becomes the HTTP response body

#if __name__ == '__main__':     # only run the server if this file is executed directly
#    app.run(host='0.0.0.0', port=5000)
    # host='0.0.0.0' = accept connections from any network interface, not just localhost
    # port=5000 = listen on port 5000

#NEW VERSION FOR TESTING ALL 5 METHODS WITH A RANDOM AHH PORT, PORT 6503 (TOP OF MY HEAD)

from flask import Flask, request        # import Flask's core class + request object

app = Flask(__name__)                     # create the app; __name__ tells Flask where it's running from

@app.route('/', methods=['GET'])          # "when someone GETs the homepage..."
def get_data():
    return "GET received — you're retrieving data"

@app.route('/', methods=['POST'])         # "when someone POSTs to the homepage..."
def post_data():
    data = request.get_data(as_text=True)     # grab whatever data was sent
    return f"POST received — you sent: {data}"

@app.route('/', methods=['PUT'])          # "when someone PUTs to the homepage..."
def put_data():
    data = request.get_data(as_text=True)
    return f"PUT received — updating with: {data}"

@app.route('/', methods=['DELETE'])       # "when someone DELETEs on the homepage..."
def delete_data():
    return "DELETE received — something got removed"

@app.route('/', methods=['PATCH'])        # "when someone PATCHes the homepage..."
def patch_data():
    data = request.get_data(as_text=True)
    return f"PATCH received — partially updating with: {data}"

if __name__ == '__main__':                # only run if this file is executed directly
    app.run(host='0.0.0.0', port=6503)
    # host='0.0.0.0' = accept connections from any interface
    # port=6503 = listen on this port (confirmed free via ss -tulpn)
