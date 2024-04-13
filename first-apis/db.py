import pyodbc

class ItemDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=GZN00000333;DATABASE=cafe;')
        self.cursor = self.conn.cursor()

    def get_items(self):
        result = []
        query = "SELECT * FROM item"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict['id'] = row[0]
            item_dict['name'] = row[1]
            item_dict['price'] = row[2]
            result.append(item_dict)
        return result
    
    def get_item(self, item_id):
        query = f"SELECT * FROM item WHERE id = '{item_id}'"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict['id'] = row[0]
            item_dict['name'] = row[1]
            item_dict['price'] = row[2]
            return [item_dict]
        
    
    def add_item(self, item):
        pass
    
    def put_item(self, id, body_object):
        pass
    
    def delete_item(self, item_id):
        pass
    
# db = ItemDatabase()
# print(db.get_items())  # It will print all the results
#print(db.get_item('f87498038e0044f3bb49add503aa1520'))  # It will print one result