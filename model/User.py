class User:
    def __init__(self, user_id, name, lastname, email, password, is_overdraft):
        self.user_id = user_id
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.is_overdraft = is_overdraft