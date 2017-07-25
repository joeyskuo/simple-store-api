from flask_restful import Resource, reqparse
from models.ItemModel import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, id):
        item = ItemModel.find_by_id(id)
        if item:
            return item.json()
        return {'message': "Item with id %d does not exist." % id}, 400

    def post(self, id):
        request_data = Item.parser.parse_args()
        if ItemModel.find_by_id(id):
            return {'message':"An item with id '%d' already exists." % id }
        
        new_item = ItemModel(request_data['name'], request_data['price'])
        try:
            new_item.save_to_db()
        except:
            return {'message': "An error occurred while inserting the item"}, 500

        return new_item.json(), 201


class Items(Resource):
    def get(self):
        items = ItemModel.select_all()
        return {'items': [item.json() for item in items]}