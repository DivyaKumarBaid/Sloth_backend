# mongoDB driver
from pymongo import MongoClient

# connection between mongodb and database.py
client = MongoClient(
    'mongodb+srv://code:code@cluster0.5jyfj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

database = client.code

user_col = database.users

posts = database.posts

code = database.code

unverified_user = database.unverified
