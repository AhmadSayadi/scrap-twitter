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

@app.route("/api/twit2", methods=['GET'])
def twitdata2():
    controller = Controller()
    return controller.gettwit2()



if __name__ == "__main__":
    app.run()