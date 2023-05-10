from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = 'friendships_schema'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.full_name = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name) VALUES(%(first_name)s.%(last_name)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        users = []
        results = connectToMySQL(cls.db).query_db(query)
        for row in results:
            users.append(cls(row))
        return users
