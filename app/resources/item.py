from flask_restful import Resource
from models.ItemModel import ItemModel

class Item(Resource):
    def get(self, id):
        item = ItemModel.find_by_id(id)
        if item:
            return item.json()
        return {'message': "Item with id %d does not exist." % id}, 400

class Items(Resource):
    def get(self):
        items = ItemModel.select_all()
        return {'items': [item.json() for item in items]}