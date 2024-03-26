import services
class Model:
    def __init__(self):
        self.db = services.Db()
    
#================SETTERS & GETTERS=======================#
    #=================GETTERS=======================#
    
            #======Transactions======#
    def get_all_transactions_of_user(self, user_id):
        """
        Retrieves all transactions of a specific user from the database.
        Params: user_id: The ID of the user
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = "SELECT * FROM transaction WHERE user_id = %s"
        return self.db.query(query, (user_id,))
    
    def get_expenses(self, user_id):
        """
        Retrieves all expenses from the database.
        Params: user_id: The ID of the user
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, 0, date)
        """
        query = "SELECT * FROM transaction WHERE type = 0 and user_id = %s"
        return self.db.query(query, (user_id,))
    
    def get_incomes(self, user_id):
        """
        Retrieves all incomes from the database.
        Params: user_id: The ID of the user
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, 1, date)
        """
        query = "SELECT * FROM transaction WHERE type = 1 and user_id = %s"
        return self.db.query(query, (user_id,))
    
    def get_transaction_by_category(self, user_id, category_id):
        """
        Retrieves all transactions of a specific category from the database.
        Params: user_id: The ID of the user, category_id: The ID of the category
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = "SELECT * FROM transaction WHERE user_id = %s AND category_id = %s"
        return self.db.query(query, (user_id, category_id))
    
    def get_transaction_by_date(self, user_id, date):
        """
        Retrieves all transactions of a specific date from the database.
        Params: user_id: The ID of the user, date: The date of the transactions
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = "SELECT * FROM transaction WHERE user_id = %s AND date = %s"
        return self.db.query(query, (user_id, date))
    
    def get_transaction_by_date_fork(self, user_id, start_date, end_date):
        """
        Retrieves all transactions between two dates from the database.
        Params: user_id: The ID of the user, start_date, end_date
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = "SELECT * FROM transaction WHERE user_id = %s AND date BETWEEN %s AND %s"
        return self.db.query(query, (user_id, start_date, end_date))
    # Sorts
    def get_all_transactions_sorted_by_date(self, user_id, reverse=False):
        """
        Retrieves all transactions sorted by date from the database.
        Params: user_id: The ID of the user, reverse: True to sort descending
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = "SELECT * FROM transaction WHERE user_id = %s ORDER BY date"
        if reverse:
            query += " DESC"
        return self.db.query(query, (user_id,))
    
    def get_all_transactions_sorted_by_amount(self, user_id, reverse=False):
        """
        Retrieves all transactions sorted by amount from the database.
        Params: user_id: The ID of the user, reverse: True to sort descending
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = "SELECT * FROM transaction WHERE user_id = %s ORDER BY amount"
        if reverse:
            query += " DESC"
        return self.db.query(query, (user_id,))
     
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
    
    
    
#=================LOGIC - OPERATIONS=======================#
    def calculate_balance(self, user_id):
        """
        Calculates the balance of a user.
        Params: user_id: The ID of the user
        Returns: [float] - The balance
        """
        query = "SELECT SUM(amount) FROM transaction WHERE user_id = %s"
        result = self.db.query(query, (user_id,))
        return result[0][0]
    
    def calculate_income(self, user_id):
        """
        Calculates the income of a user.
        Params: user_id: The ID of the user
        Returns: [float] - The income
        """
        query = "SELECT SUM(amount) FROM transaction WHERE user_id = %s AND type = 1"
        result = self.db.query(query, (user_id,))
        return result[0][0]
    
    def calculate_expense(self, user_id):
        """
        Calculates the expenses of a user.
        Params: user_id: The ID of the user
        Returns: [float] - The expenses
        """
        query = "SELECT SUM(amount) FROM transaction WHERE user_id = %s AND type = 0"
        result = self.db.query(query, (user_id,))
        return result[0][0]