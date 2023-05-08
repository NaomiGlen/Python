from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import burger

class Topping:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.topping_name = db_data['topping_name']
        self.on_burgers = []
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO toppings ( topping_name, created_at , updated_at ) VALUES (%(topping_name)s,NOW(),NOW());"
        return connectToMySQL('burger_schema').query_db(query, data)

    @classmethod
    def get_topping_with_burgers( cls , data ):
        query = "SELECT * FROM toppings LEFT JOIN add_ons ON add_ons.topping_id = toppings.id LEFT JOIN burgers ON add_ons.burger_id = burgers.id WHERE toppings.id = %(id)s;"
        results = connectToMySQL('burger_schema ').query_db( query , data )
        topping = cls( results[0] )
        for row_from_db in results:
           burger_data = {
                "id" : row_from_db["burgers.id"],
                "name" : row_from_db["name"],
                "bun" : row_from_db["bun"],
                "calories" : row_from_db["calories"],
                "created_at" : row_from_db["toppings.created_at"],
                "updated_at" : row_from_db["toppings.updated_at"]
            }
           topping.on_burgers.append( burger.Burger( burger_data ))
        return topping

