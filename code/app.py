from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegistration
from resources.item import Item, Itemlist
from resources.store import Store, Storelist

app = Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_tables():
    db.drop_all()
    db.create_all()

jwt=JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:name>")
api.add_resource(Itemlist,"/items")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(Storelist,"/stores")
api.add_resource(UserRegistration, "/register")

if __name__ == '__main__':
    from resources.db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
