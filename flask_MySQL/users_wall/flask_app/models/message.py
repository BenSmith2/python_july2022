from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE, EMAIL_REGEX

class Message:
    def __init__(cls, data):
        self.id= data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender_id = data['sender_id']
        self.sender = data['sender']
        self.receiver_id = data['receiver_id']
        self.receiver = data['receiver']

    @classmethod
    def get_all_messages(cls, data):
        pass