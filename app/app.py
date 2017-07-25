from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity

from resources.item import Item, Items
from resources.user import Register
from resources.store import Store, Stores


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.secret_key = 'joeyskuo'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth endpoint

api.add_resource(Register, '/register')
api.add_resource(Store, '/store/<int:id>')
api.add_resource(Stores, '/stores')
api.add_resource(Item, '/item/<int:id>')
api.add_resource(Items, '/items')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)