from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$')


class User:
    db="dojo_wall_schema"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO users(first_name,last_name,email,password)
                VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
                """
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def get_all(cls,data):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query,data)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users Where id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query,user)
        for field in user:
            if len(user[field]) <= 0:
                is_valid = False
                message = f"{field} is required!".capitalize()
                make_pretty=message.maketrans("_", " ")
                flash(message.translate(make_pretty),"register")
        if len(results) >= 1:
            flash("Email address is already registered to a user!", "register")
            is_valid = False
        if len(user['email']) > 0 and not EMAIL_REGEX.match(user['email']):
            flash("Invalid email format!", "register")
            is_valid = False
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters in length!","register")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters in length!", "register")
            is_valid = False
        if len(user['password']) < 8 and not PASSWORD_REGEX.match(user['password']):
            flash("Password must be at least 8 characters in length, contain at least one uppercase letter and one number!", "register")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Passwords do not match, please try again","register")
            is_valid = False
        return is_valid