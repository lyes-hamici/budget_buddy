import services
class Model:
    def __init__(self):
        self.db = services.Db()
    
#=============RETRIEVE INFO=================#    
        #=============RECOVER INFO BY ID=============#
    def get_category_by_id(self, category_id):
        """
        Retrieves the name of a category from its id.
        """
        query = "SELECT name FROM category WHERE category_id = %s"
        return self.db.query(query, (category_id,))
    
    def get_user_by_id(self, user_id):
        """
        Retrieves the information of a user from its id.
        """
        query = "SELECT * FROM user WHERE user_id = %s"
        return self.db.query(query, (user_id,))
    
    def get_transaction_by_id(self, transaction_id):
        """
        Retrieves the information of a transaction from its id.
        """
        query = "SELECT * FROM transaction WHERE transaction_id = %s"
        return self.db.query(query, (transaction_id,))
    
    
    
