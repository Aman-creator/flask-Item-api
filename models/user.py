import sqlite3

class UserModel:
    def __init__(self,_id,username, password):
        self.id =_id
        self.username = username
        self.password = password
        
    @classmethod                                      # this would save us from using or passing self inside function
    def find_by_username(cls,username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM users WHERE username = ?"
        result = cursor.execute(query,(username,))
        row = result.fetchone()
        
        if row:
            user = cls(*row)                          # cls is used instead of self
        else:
            user = None
        
        connection.close()
        return user
    
    @classmethod                                      # this would save us from using or passing self inside function
    def find_by_id(cls,_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM users WHERE id = ?"
        result = cursor.execute(query,(_id,))
        row = result.fetchone()
        
        if row:
            user = cls(*row)                          # cls is used instead of self
        else:
            user = None
        
        connection.close()
        return user
        
        