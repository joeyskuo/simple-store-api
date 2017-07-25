from flask_restful import Resource
from models.StoreModel import StoreModel


class Store(Resource):

    def get(self, id):
        store = StoreModel.find_by_id(id)
        if store:
            return store.json()
        return {'message': 'Store with id: %d does not exist.' % id}, 400

class Stores(Resource):
    def get(self):
        stores = StoreModel.select_all()
        return {'stores': [store.json for store in stores]}