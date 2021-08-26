import sqlite3
from flask_restful import Resource ,reqparse
from models.user import UserModel


class User_Register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type = str,
        required = True,
        help = 'this field can not be  empty'
    )
    parser.add_argument(
        'password',
        type = str,
        required = True,
        help = 'this field can not be  empty'
    )
    
    
    def post(self):
        data = User_Register.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {"message": 'user with username {} already exist'.format(data['username'])},400
            
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        insert_query = 'INSERT INTO users VALUES(NULL,?,?)'
        cursor.execute(insert_query,(data['username'],data['password']))
        
        connection.commit()
        connection.close()
        return {"message": 'user is successfully Registerd with username {} and password {}'.format(data['username'], data['password'])}
        
        
    