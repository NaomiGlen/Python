from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.dojo_id = db_data['dojo_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO ninjas (first_name,last_name,age,created_at,updated_at)
                VALUES (%(first_name)s,%(last_name)s,%(age)s,NOW(),NOW())
                """
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        ninjas_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for n in ninjas_from_db:
            ninjas.append(cls(n))
        return ninjas

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
        ninja_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(ninja_from_db[0])

