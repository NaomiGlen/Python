from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self,db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.ninjas = []
    
    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO dojos(name,created_at,updated_at)
                VALUES (%(name)s,NOW(),NOW());
                """
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for d in dojos_from_db:
            dojos.append(cls(d))
        return dojos

    @classmethod
    def get_dojo_with_ninjas(cls,data):
        query = """
                SELECT * FROM dojos
                LEFT JOIN ninjas
                ON ninjas.dojo_id = dojos.id
                WHERE dojos.id = %(id)s;
                """
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        dojo = cls(results[0])
        for row_from_db in results:
            dojo_ninjas = {
                "id" : row_from_db["id"],
                "name" : row_from_db["name"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db["updated_at"],
                "ninjas_id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "dojo_id" : row_from_db["dojo_id"],
                "ninjas.created_at" : row_from_db["ninjas.created_at"],
                "ninjas.updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja(dojo_ninjas))
        return dojo
