from flask_restful import Resource, reqparse
from models.StoreModel import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    def get(self, id):
        store = StoreModel.find_by_id(id)
        if store:
            return store.json()
        return {'message': 'Store with id: %d does not exist.' % id}, 400

    def post(self, id):

        if StoreModel.find_by_id(id):
            return {'message': "Store with id '%d' already exists" % id}, 400

        request_data = Store.parser.parse_args()
        store = StoreModel(request_data['name'])
        store.id = id

        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred while creating the store'}, 500
        return store.json()


    def delete(self, id):
        store = StoreModel.find_by_id(id)
        if store:
            store.delete_from_db()
            return {'message': 'Store deleted'}
        return {'message':"Error: Store with id '%d' does not exist." % id}

class Stores(Resource):
    def get(self):
        stores = StoreModel.select_all()
        return {'stores': [store.json() for store in stores]}