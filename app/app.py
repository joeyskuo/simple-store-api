from flask import Flask
from flask_restful import Api

from resources.item import Item, Items

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.secret_key = 'joeyskuo'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Item, '/item/<int:id>')
api.add_resource(Items, '/items')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)