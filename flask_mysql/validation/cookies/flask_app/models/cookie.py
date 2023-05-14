from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Cookie:
    db="cookie_orders_schema"
    def __init__(self,data):
        self.id=data["id"]
        self.customer_name=data["customer_name"]
        self.cookie_type=data["cookie_type"]
        self.number_of_boxes=data["number_of_boxes"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]

    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO orders(customer_name,cookie_type,number_of_boxes)
                VALUES (%(customer_name)s,%(cookie_type)s,%(number_of_boxes)s);
                """
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def update(cls,data):
        query = """ UPDATE orders
                SET customer_name=%(customer_name)s, cookie_type=%(cookie_type)s, number_of_boxes=%(number_of_boxes)s
                WHERE id = %(id)s;
                """
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders;"
        results=connectToMySQL(cls.db).query_db(query)
        orders=[]
        for x in results:
            orders.append(cls(x))
        return orders

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM orders WHERE id=%(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def get_by_id(cls,order_id):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        data = {
            "id":order_id
        }
        result = connectToMySQL(cls.db).query_db(query,data)
        if result:
            order = result[0]
            return order
        return False

    @classmethod
    def is_valid_order(cls,order):
        is_valid=True
        
        if len(order['customer_name']) <= 0 or len(order['cookie_type']) <= 0 or len(order['number_of_boxes']) <= 0:
            flash("All fields required!")
            is_valid=False
        if len(order['customer_name']) < 2:
            flash("Customer name must be at least 2 characters in length!")
            is_valid=False
        if len(order['cookie_type']) < 2:
            flash("Cookie type must be at least 2 characters in length!")
            is_valid=False
        if int(order['number_of_boxes']) <= 0:
            flash("Number of boxes cannot be a negative number!")
            is_valid=False
        return is_valid