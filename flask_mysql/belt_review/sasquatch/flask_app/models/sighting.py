from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Sighting:
    db = "sasquatch_schema"
    def __init__(self, db_data):
        self.id = db_data["id"]
        self.location = db_data["location"]
        self.content = db_data["content"]
        self.sight_date = db_data["sight_date"]
        self.num_sasquatch = db_data["num_sasquatch"]
        self.created_at = db_data["created_at"]
        self.updated_at = db_data["updated_at"]
        self.user_id = db_data["user_id"]
        self.reporter = None

    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM sightings
                JOIN users ON sightings.user_id = users.id
                """
        results = connectToMySQL(cls.db).query_db(query)
        print("Raw data for all sightings:", results)
        sightings = []
        for row in results:
            this_sighting = cls(row)
            user_data = {
                "id": row["user_id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            this_sighting.reporter = user.User(user_data)
            sightings.append(this_sighting)
        return sightings

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO sightings (location, content, sight_date, num_sasquatch, user_id)
                VALUES (%(location)s, %(content)s, %(sight_date)s, %(num_sasquatch)s, %(user_id)s);
                """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = """
                DELETE FROM sightings WHERE id = %(id)s;
                """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
                UPDATE sightings
                SET location = %(location)s, 
                content = %(content)s, 
                sight_date = %(sight_date)s, 
                num_sasquatch = %(num_sasquatch)s, 
                user_id = %(user_id)s
                WHERE id = %(id)s;
                """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        query = """
                SELECT * FROM sightings
                JOIN users on sightings.user_id = users.id
                WHERE sightings.id = %(id)s;
                """
        result = connectToMySQL(cls.db).query_db(query, data)
        if not result:
            return False
        result = result[0]
        this_sighting = cls(result)
        user_data = {
            "id": result["user_id"],
            "first_name": result["first_name"],
            "last_name": result["last_name"],
            "email": result["email"],
            "password": result["password"],
            "created_at": result["created_at"],
            "updated_at": result["updated_at"]
        }
        this_sighting.reporter = user.User(user_data)
        return this_sighting

    @staticmethod
    def validate_sighting(form_data):
        is_valid = True
        if len(form_data["location"]) <= 0 or len(form_data["content"]) <= 0 or len(form_data["sight_date"]) <= 0:
            for field in form_data:
                if len(form_data[field]) <= 0:
                    is_valid = False
                    message = f"{field} cannot be empty".capitalize()
                    make_pretty = message.maketrans("_", " ")
                    flash(message.translate(make_pretty), "sighting_error")
        if int(form_data["num_sasquatch"]) < 1:
            is_valid = False
            flash("Number of sasquatch cannot be 0", "sighting_error")
        return is_valid