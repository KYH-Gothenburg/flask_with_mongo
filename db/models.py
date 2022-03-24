from db.mongo_access import Document, db


class User(Document):
    collection = db.users


class Product(Document):
    collection = db.products
