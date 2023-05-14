from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    db="users_schema"
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.full_name=[]

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query="SELECT * FROM users;"
        results=connectToMySQL(cls.db).query_db(query)
        users=[]
        for x in results:
            users.append(cls(x))
        return users
    
    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO users(first_name,last_name,email)
                VALUES (%(first_name)s,%(last_name)s, %(email)s);
                """
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def update(cls,data):
        query = """ UPDATE users
                SET first_name=%(first_name)s,last_name=%(last_name)s, email=%(email)s
                WHERE id = %(id)s;
                """
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def is_valid_user(cls,user):
        is_valid=True
        for field in user:
            if len(user[field]) <= 0:
                is_valid=False
                message = f"{field} is required.".capitalize()
                make_pretty=message.maketrans("_", " ")
                flash(message.translate(make_pretty))
        if len(user['email']) > 0 and not EMAIL_REGEX.match(user['email']):
            flash("Invalid email format.")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_user(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            is_valid = False
        return is_valid