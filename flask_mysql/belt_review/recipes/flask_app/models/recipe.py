from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Recipe:
    db = "recipe_schema"
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.instructions = db_data['instructions']
        self.submit_date = db_data['submit_date']
        self.under_30 = db_data['under_30']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']
        self.creator = None

    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM recipes
                JOIN users ON recipes.user_id = users.id;
                """
        results = connectToMySQL(cls.db).query_db(query)
        print("Raw data for all recipes: ", results)
        recipes = []
        for row in results:
            this_recipe = cls(row)
            user_data = {
                "id": row["user_id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            this_recipe.creator = user.User(user_data)
            recipes.append(this_recipe)
        return recipes
    
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO recipes (name, description, instructions, submit_date, under_30, user_id) 
                VALUES (%(name)s, %(description)s, %(instructions)s, %(submit_date)s, %(under_30)s, %(user_id)s);
                """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """ UPDATE recipes
                    SET name = %(name)s, 
                    description = %(description)s, 
                    instructions = %(instructions)s,
                    submit_date = %(submit_date)s,
                    under_30 = %(under_30)s
                    WHERE id = %(id)s;
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_by_id(cls, data):
        query = """
                SELECT * FROM recipes
                JOIN users on recipes.user_id = users.id
                WHERE recipes.id = %(id)s;
                """
        result = connectToMySQL(cls.db).query_db(query, data)
        if not result:
            return False
        result = result[0]
        this_recipe = cls(result)
        user_data = {
            "id": result["user_id"],
            "first_name": result["first_name"],
            "last_name": result["last_name"],
            "email": result["email"],
            "password": "",
            "created_at": result["created_at"],
            "updated_at": result["updated_at"]
        }
        this_recipe.creator = user.User(user_data)
        return this_recipe
    
    @staticmethod
    def valid_recipe(form_data):
        is_valid = True
        if len(form_data["name"]) <= 0 or len(form_data["description"]) <= 0 or len(form_data["instructions"]) <= 0:
            for field in form_data:
                if len(form_data[field]) <= 0:
                    is_valid = False
                    message = f"{field} cannot be empty!".capitalize()
                    make_pretty = message.maketrans("_", " ")
                    flash(message.translate(make_pretty), "recipe_error")
        if len(form_data["name"]) < 4 or len(form_data["description"]) < 4 or len(form_data["instructions"]) < 4:
            for field in form_data:
                if len(form_data[field]) < 4:
                    is_valid = False
                    message = f"{field} cannot be less than 4 characters!".capitalize()
                    make_pretty = message.maketrans("_", " ")
                    flash(message.translate(make_pretty), "recipe_error")
        return is_valid