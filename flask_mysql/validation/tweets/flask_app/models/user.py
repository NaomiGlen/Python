from twitter_app.models import tweet
# Other imports here...
class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.handle = data['handle']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # [] can represent a currently empty place to store all of the tweets that a single User instance has created, as a User creates MANY Tweets
        self.tweets = [] 

