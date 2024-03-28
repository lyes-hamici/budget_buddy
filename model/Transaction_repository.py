from model import Transaction

class Transaction_repository:
    def __init__(self,db):
        self.db = db
    #=================SETTERS=======================#
    def create_transaction(self, user_id, name, description, amount, category_id, type, date):
        """
        Creates a transaction in the database.
        Params: user_id: The ID of the user, name: The name of the transaction, description: The description of the transaction, amount: The amount of the transaction, category_id: The ID of the category, type: The type of the transaction, date: The date of the transaction
        """
        query = "INSERT INTO transaction (user_id, name, description, amount, category_id, type, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.db.query(query, (user_id, name, description, amount, category_id, type, date))
        
    #=================GETTERS=======================#
    def get_all_transactions_of_user(self, user_id):
        """
        Retrieves all transactions of a specific user from the database.
        Params: user_id: The ID of the user
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = "SELECT * FROM transaction WHERE user_id = %s"
        response = self.db.query(query, (user_id,))
        return [Transaction(*row) for row in response]

    def get_all_transactions_last_month(self, user_id):
        """
        Retrieves all transactions of the last month from the database.
        Params: user_id: The ID of the user
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = "SELECT * FROM transaction WHERE user_id = %s AND date >= DATE_SUB(NOW(), INTERVAL 1 MONTH)"
        response = self.db.query(query, (user_id,))
        return [Transaction(*row) for row in response]
    
    def get_expenses(self, user_id):
        """
        Retrieves all expenses from the database.
        Params: user_id: The ID of the user
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, 0, date)
        """
        query = "SELECT * FROM transaction WHERE type = 0 and user_id = %s"
        response = self.db.query(query, (user_id,))
        return [Transaction(*row) for row in response]
    
    def get_incomes(self, user_id):
        """
        Retrieves all incomes from the database.
        Params: user_id: The ID of the user
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, 1, date)
        """
        query = "SELECT * FROM transaction WHERE type = 1 and user_id = %s"
        reponse = self.db.query(query, (user_id,))
        return [Transaction(*row) for row in reponse]
    
    def get_transaction_by_category(self, user_id, category_id):
        """
        Retrieves all transactions of a specific category from the database.
        Params: user_id: The ID of the user, category_id: The ID of the category
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = "SELECT * FROM transaction WHERE user_id = %s AND category_id = %s"
        response = self.db.query(query, (user_id, category_id))
        return [Transaction(*row) for row in response]
    
    def get_transaction_by_date(self, user_id, date):
        """
        Retrieves all transactions of a specific date from the database.
        Params: user_id: The ID of the user, date: The date of the transactions
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = "SELECT * FROM transaction WHERE user_id = %s AND date = %s"
        response = self.db.query(query, (user_id, date))
        return [Transaction(*row) for row in response]
    
    def get_transaction_by_date_fork(self, user_id, start_date, end_date):
        """
        Retrieves all transactions between two dates from the database.
        Params: user_id: The ID of the user, start_date, end_date
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = "SELECT * FROM transaction WHERE user_id = %s AND date BETWEEN %s AND %s"
        response = self.db.query(query, (user_id, start_date, end_date))
        return [Transaction(*row) for row in response]
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
        response = self.db.query(query, (user_id,))
        return [Transaction(*row) for row in response]
    
    def get_all_transactions_sorted_by_amount(self, user_id, reverse=False):
        """
        Retrieves all transactions sorted by amount from the database.
        Params: user_id: The ID of the user, reverse: True to sort descending
        Returns: [tuple] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = "SELECT * FROM transaction WHERE user_id = %s ORDER BY amount"
        if reverse:
            query += " DESC"
        response = self.db.query(query, (user_id,))
        return [Transaction(*row) for row in response]
    
    #=================LOGIC - OPERATIONS=======================#
    def calculate_balance(self, user_id):
        """
        Calculates the balance of a user.
        Params: user_id: The ID of the user
        Returns: [float] - The balance
        """
        query = "SELECT SUM(amount) FROM transaction WHERE user_id = %s"
        result = self.db.query(query, (user_id,))
        response = result[0][0]
        return response
    
    def calculate_income(self, user_id):
        """
        Calculates the income of a user.
        Params: user_id: The ID of the user
        Returns: [float] - The income
        """
        query = "SELECT SUM(amount) FROM transaction WHERE user_id = %s AND type = 1"
        result = self.db.query(query, (user_id,))
        response = result[0][0]
        return response
    
    def calculate_expense(self, user_id):
        """
        Calculates the expenses of a user.
        Params: user_id: The ID of the user
        Returns: [float] - The expenses
        """
        query = "SELECT SUM(amount) FROM transaction WHERE user_id = %s AND type = 0"
        result = self.db.query(query, (user_id,))
        response = result[0][0]
        return response
    
if __name__ == "__main__":
    from services import Db
    db = Db()
    tr = Transaction_repository(db)
    print(tr.get_all_transactions_of_user(1))