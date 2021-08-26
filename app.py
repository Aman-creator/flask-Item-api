from flask import Flask
from flask_restful import Api
from flask_jwt import JWT,jwt_required
from security import authenticate,identity 
from resources.user import User_Register
from resources.item import Item,Itemlist

app = Flask(__name__)                                 #__name__ is an inbuilt variable which is used to get the name of file
app.secret_key = "aman"
api = Api(app)                                        # Entry point of api, used for routing easily 


jwt =JWT(app,authenticate,identity)                   # /auth

api.add_resource(Item, '/Item/<string:name>')
api.add_resource(Itemlist, '/items')
api.add_resource(User_Register, '/user_register')

if __name__ == '__main__':
    app.run(port=5000, debug = True)
    





