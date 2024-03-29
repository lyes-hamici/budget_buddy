from model import User
from services import register_verification

class User_repository:
    def __init__(self, db):
        self.db = db

#================VERIFIERS=======================#        
    def verify_if_exist(self, email):
        """
        Verifies if an user exist in the database+.
        Params: the email of the user that has to be verified.
        Returns: Boolean - True if the user exist, False if not.
        """
        query = "SELECT id FROM user WHERE email = %s"
        response = self.db.query(query, (email,))
        return len(response) > 0
    
    def verify_if_correct(self, email, password):
        """
        Verifies if the user credential are correct.
        Params: the email and the password of the user that has to be verified.
        Returns: Boolean - True if the credentials are correct, False if not.
        """
        if self.verify_if_exist(email):
            query = "SELECT id FROM user WHERE email = %s AND password = %s"
            response = self.db.query(query, (email, password))
            return len(response) > 0
#================GETTERS=======================#
    def get_user(self, email):
        """
        Get the user from the database.
        Params: the email of the user.
        Returns: an User object.
        """
        query = "SELECT * FROM user WHERE email = %s"
        response = self.db.query(query, (email,))
        return User(*response[0])

#================SETTERS=======================# 
    def create_user(self, name, lastname, email, password):
        """
        Create an user in the database.
        Params: the email and password of the user.
        Returns: Boolean - True if the user is created, False if not.
        """
        if register_verification.is_valid_registration(email, password) and not self.verify_if_exist(email):
            query = "INSERT INTO user (name, lastname, email, password) VALUES (%s, %s, %s, %s)"
            self.db.execute(query, (name, lastname, email, password))
            return True
        else:
            return False
#================AUTHENTICATION=======================#
    def connect_user(self, email, password):
        """
        Connect the user to the application.
        Params: the email and password of the user.
        Returns: an User object if the credentials are correct, None if not.
        """
        if self.verify_if_correct(email, password):
            return self.get_user(email)
        
    
    