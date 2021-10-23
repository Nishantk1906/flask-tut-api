from flask_restful import Resource, reqparse
from models.store import Storemodel

class Store(Resource):
    def get(self, name):
        store= Storemodel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if Storemodel.find_by_name(name):
            return {'message': 'A store with name already exists'}, 400
        store = Storemodel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'internal server error'}, 500

        return store.json(), 201

    def delete(self, name):
        store = Storemodel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'store deleted'}

class Storelist(Resource):
    def get(self):
        return {'stores': [store.json() for store in Storemodel.query.all()]}
