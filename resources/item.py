import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()                 # reqparse is used to get the selected information from json payload       
    parser.add_argument(
        'price',
        type = float,
        required = True,
        help = 'this field can not be left blank!'
    )
    
    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        
        if item:
            return item.json()
        return {"message": 'item does not exist'},404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message': "an item with name {} already exixt".format(name)},400
        
        data = Item.parser.parse_args()
        item =ItemModel(name, data['price'])
        
        try:
            item.insert()
        except:
            return {"Message": "An Error occured insertin the item."}
        
        return item.json(), 201

    def delete(self,name):
        
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name = ?"
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()
        return {'message': 'item {} deleted'.format(name)}
    
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])
        if item is None:
            try:
                updated_item.insert()
            except:
                return {"message": "An error occurred inserting the item."}
        else:
            try:
                updated_item.update()
            except:
                return {"message": "An error occurred updating the item."}
        return updated_item.json()


class Itemlist(Resource):
    TABLE_NAME = 'items'

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        connection.close()

        return {'items': items}