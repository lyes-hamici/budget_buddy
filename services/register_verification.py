import re

def verify_is_email(email):
    """
    Verifies if the email is a valid email.
    Params: the email that has to be verified.
    Returns: Boolean - True if the email is valid, False if not.
    """
    if len(email) < 5:
        return False
    if email.count("@") != 1:
        return False
    if email.count(".") < 1:
        return False
    print("email is valid")
    return True

def verify_password_is_strong(password):
    """
    Verifies if the password is strong.
    Params: the password that has to be verified.
    Returns: Boolean - True if the password is strong, False if not.
    """
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    print("password is strong")
    return True

def is_valid_registration(email, password):
    return verify_is_email(email) and verify_password_is_strong(password)

        