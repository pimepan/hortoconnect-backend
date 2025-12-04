from flask import Flask
from flask_cors import CORS
from firebase_admin import credentials, initialize_app
cred = credentials.Certificate("secret/firebase.json")
initialize_app(cred)
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "Hello, World!"




if __name__ == '__main__':
    app.run(debug=True)