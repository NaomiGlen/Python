from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import topping,restaurant

class Burger:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated']
        self.toppings = []

    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO burgers (name,bun,meat,calories,restaurant_id,created_at,updated_at)
                VALUES(%(name)s,%(bun)s,%(meat)s,%(calories)s,%(restaurant_id)s,NOW(),NOW());
                """
        burger_id = connectToMySQL('burger_schema').query_db(query,data)
        return burger_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers"
        burgers_from_db = connectToMySQL('burger_schema').query_db(query)
        burgers = []
        for b in burgers_from_db:
            burgers.append(cls,(b))
        return burgers

    @classmethod
    def get_burger_with_toppings( cls , data ):
        query = """SELECT * FROM burgers 
                LEFT JOIN add_ons ON add_ons.burger_id = burgers.id 
                LEFT JOIN toppings ON add_ons.topping_id = toppings.id 
                WHERE burgers.id = %(id)s;
                """
        results = connectToMySQL('burger_schema').query_db( query , data )
        burger = cls( results[0] )
        for row_from_db in results:
            topping_data = {
                "id" : row_from_db["toppings.id"],
                "topping_name" : row_from_db["topping_name"],
                "created_at" : row_from_db["toppings.created_at"],
                "updated_at" : row_from_db["toppings.updated_at"]
            }
            burger.toppings.append( topping.Topping( topping_data ) )
        return burger

    @staticmethod
    def validate_burger(burger):
        is_valid = True
        if len(burger['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(burger['bun']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        if int(burger['calories']) < 200:
            flash("Calories must be 200 or greater.")
            is_valid = False
        if len(burger['meat']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        return is_valid