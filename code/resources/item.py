from flask import Flask
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import Itemmodel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float,required = True, help = "need price field")
    parser.add_argument('store_id', type=int,required = True, help = "item needs a store id")

    def get(self, name):
        item = Itemmodel.find_by_name(name)
        if item:
            return item.json()
        else:
            return {'message': 'item does not exist'}, 404


    def post(self, name):
        if Itemmodel.find_by_name(name):
            return {"message":"items with '{}' already exists".format(name)}, 400
        request_data = Item.parser.parse_args()
        new_item=Itemmodel(name,request_data["price"], request_data['store_id'])

        try:
            new_item.save_to_db()
        except:
            return {'message': 'Internal server error'}, 500

        return new_item.json(), 201

    def delete(self,name):
        if Itemmodel.find_by_name(name):
            Item.delete_from_db()
            return {"message": "deletion succesful"}, 200

        return {'message': 'item not found'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = Itemmodel.find_by_name(name)
        if item is None:
            item=Itemmodel(name, data['price'], data['store_id'])
        else:
            item.price=data['price']

        item.save_to_db()

        return item.json()

class Itemlist(Resource):
    def get(self):
        return {'Items': [item.json() for item in Itemmodel.query.all()]}
