from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import bcrypt
from flask import flash
import re
EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
password_pattern = re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$")

class User:
    db="recipe_schema"
    def __init__(self,db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.email = db_data['email']
        self.password = db_data['password']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def get_all(cls,data):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def save(cls,form_data):
        hashed_data = {
            'first_name': form_data['first_name'],
            'last_name': form_data['last_name'],
            'email': form_data['email'],
            'password': bcrypt.generate_password_hash(form_data['password'])
        }
        query = """
                INSERT INTO users (first_name,last_name,email,password) 
                VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
                """
        return connectToMySQL(cls.db).query_db(query,hashed_data)

    @staticmethod
    def valid_registration(form_data):
        is_valid = True
        for field in form_data:
            if len(form_data[field]) <= 0:
                is_valid = False
                message = f"{field} is required!".capitalize()
                make_pretty = message.maketrans("_"," ")
                flash(message.translate(make_pretty),"register")
            if len(results) >= 1:
                flash("Email already exists!","register")
                is_valid = False
            if len(form_data['email']) > 0 and not EMAIL_REGEX.match(form_data['email']):
                flash("Invalid email!","register")
                is_valid = False
            if len(form_data['first_name']) < 3:
                flash("First name must be at least 3 characters long!","register")
                is_valid = False
            if len(form_data['last_name']) < 3:
                flash("Last name must be at least 3 characters long!","register")
                is_valid = False
            if len(form_data['password']) < 8 and not password_pattern.match(form_data['password']):
                flash("Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter and one number!","register")
                is_valid = False
            if form_data['password']!= form_data['confirm_password']:
                flash("Passwords do not match!","register")
                is_valid = False
        return is_valid

    @staticmethod
    def valid_login(form_data):
        if not EMAIL_REGEX.match(form_data['email']):
            flash("Invalid email!","login")
            return False
        user = User.get_by_email(form_data)
        if not user:
            flash("Invalid email!","login")
            return False
        if not bcrypt.check_password_hash(user.password,form_data['password']):
            flash("Invalid password!","login")
            return False
        return user