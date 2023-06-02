from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from controllers import Controller


app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route("/api/twit", methods=['GET','POST'])
def twitdata():
    controller = Controller()
    return controller.gettwit()



if __name__ == "__main__":
    app.run(debug=True, port=5000)