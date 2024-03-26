import uuid
import keyring
import getpass
from keyring.errors import PasswordDeleteError

from model.Model import Model

class Service:
    def __init__(self):
        self.auth_token = self.get_local_auth_token()
        self.auth = False
        self.model = Model()

    #===========================================================================
    # methodes for authentication
    #===========================================================================
        
    def automatic_login(self, remember_me_value):
        if remember_me_value == True and self.auth_token != None:
            result = self.model.check_auth_token(self.auth_token)
            if result != []:
                username = result[0][1]
                if result:
                    self.save_checkbox_state(remember_me_value)
                    self.auth = True
                    return self.auth , username
                else:
                    self.auth = False
                    return self.auth
        else: 
            pass

    def login(self, username, password, remember_me_value=False):
        if self.validate_credentials(username, password):
            if remember_me_value:
                usermail = self.model.get_user_information_by_username(username)[4]
                auth_token = str(uuid.uuid4())
                self.model.save_auth_token(usermail, auth_token)
                self.set_local_auth_token(auth_token)
            self.save_checkbox_state(remember_me_value)
            self.auth = True
        else:
            self.auth = False
        return self.auth

    def validate_credentials(self, username, password):
        user = self.model.get_user_by_username(username)
        if user:
            #! Keep for when passwords are hashed
            # Check hashed password with bcrypt
            hashed_password = user[1]
            '''if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                # Mot de passe correct
                return True'''
            if password == hashed_password:
                return True
        # Username not found or incorrect password
        return False
    
    def set_local_auth_token(self, auth_token):
        keyring.set_password('Harmony_password', getpass.getuser(), auth_token)

    def get_local_auth_token(self):
        token = keyring.get_password('Harmony_password', getpass.getuser())
        return token
    
    def save_checkbox_state(self, state):
        keyring.set_password('Harmony_checkbox', 'remember_me_value', str(state))

    def load_checkbox_state(self):
        state_str = keyring.get_password('Harmony_checkbox', 'remember_me_value')
        if state_str is not None:
            if state_str == 'True':
                return True
            else:    
                return False
        else:
            return False
        
    def reset_local_data(self):

        try:
            keyring.delete_password('Harmony_password', getpass.getuser())
            keyring.delete_password('Harmony_checkbox', 'remember_me_value')
        except PasswordDeleteError as e:
            print("No local data found to reset.")
        
        

    def logout(self):
        self.auth = False

    def isAuth(self):
        return self.auth
    