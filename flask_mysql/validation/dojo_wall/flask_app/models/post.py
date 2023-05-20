from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Post:
    db = "dojo_wall_schema"
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = data["user"]

    @classmethod
    def save(cls, data):
        if not cls.validate_post(data):
            print("Post save has failed")
            return False
        print("Post save is successful", data)
        query = "INSERT INTO posts (content, user_id) VALUES (%(content)s, %(user_id)s);"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def delete(cls, post_id):
        query = "DELETE FROM posts WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, {"id": post_id})
        return post_id
    
    @classmethod
    def validate_post(cls, data):
        is_valid = False
        if len(data["content"]) == 0:
            flash("Content cannot be empty", "posts")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM posts
                JOIN users on posts.user_id = users.id;
                """
        results = connectToMySQL(cls.db).query_db(query)
        print("Raw data for all posts: ", results)
        all_posts = []
        for row in results:
            post_user = User({
                "id": row["user_id"],
                "email": row["email"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "password": row["password"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
            })
            new_post = Post({
                "id": row["id"],
                "content": row["content"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "user": post_user
            })
            all_posts.append(new_post)
        return all_posts