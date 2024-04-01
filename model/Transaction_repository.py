from model import Transaction

class Transaction_repository:
    def __init__(self,db):
        self.db = db
    #=================SETTERS=======================#
    def create_transaction(self, user_id, name, description, amount, category_id, date): #if don't use condition put type as parameter and erase the condition
        """
        Creates a transaction in the database.
        Params: user_id: The ID of the user, name: The name of the transaction, description: The description of the transaction, amount: The amount of the transaction, category_id: The ID of the category, type: The type of the transaction, date: The date of the transaction
        """
        if amount < 0:
            type = 0
        else:
            type = 1
        query = "INSERT INTO transaction (user_id, name, description, amount, category_id, type, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.db.execute(query, (user_id, name, description, amount, category_id, type, date))
    
    def update_transaction(self, transaction_id, user_id, name, description, amount, category_id, date):
        """
        Updates a transaction in the database.
        Params: transaction_id: The ID of the transaction, user_id: The ID of the user, name: The name of the transaction, description: The description of the transaction, amount: The amount of the transaction, category_id: The ID of the category, date: The date of the transaction
        """
        query = "UPDATE transaction SET user_id = %s, name = %s, description = %s, amount = %s, category_id = %s, date = %s WHERE id = %s"
        self.db.execute(query, (user_id, name, description, amount, category_id, date, transaction_id))
    
    def delete_transaction(self, transaction_id):
        """
        Deletes a transaction from the database.
        Params: transaction_id: The ID of the transaction
        """
        query = "DELETE FROM transaction WHERE id = %s"
        self.db.execute(query, (transaction_id,))
        
    #=================GETTERS=======================#
    def get_all_transactions_of_user(self, user_id):
        """
        Retrieves all transactions of a specific user from the database.
        Params: user_id: The ID of the user
        Returns: [Transactions] - (transaction_id, user_id, name, description, amount, category_name, type, date)
        """
        query = """
        SELECT t.id, t.user_id, t.name, t.description, t.amount, c.name, t.type, t.date
        FROM transaction t
        INNER JOIN category c ON t.category_id = c.id
        WHERE t.user_id = %s
        """
        response = self.db.query(query, (user_id,))
        return [Transaction(*row) for row in response]

    def get_all_transactions_last_month(self, user_id):
        """
        Retrieves all transactions of the last month from the database.
        Params: user_id: The ID of the user
        Returns: [Transaction] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = """
        SELECT t.transaction_id, t.user_id, t.name, t.description, t.amount, c.name, t.type, t.date
        FROM transaction t
        INNER JOIN category c ON t.category_id = c.id
        WHERE t.user_id = %s AND t.date >= DATE_SUB(NOW(), INTERVAL 1 MONTH)
        """
        response = self.db.query(query, (user_id,))
        return [Transaction(*row) for row in response]
    
    def get_3_last_transactions(self, user_id):
        """
        Retrieves the 3 last transactions of a user from the database.
        Params: user_id: The ID of the user
        Returns: [Transaction] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = """
            SELECT t.transaction_id, t.user_id, t.name, t.description, t.amount, c.name, t.type, t.date
            FROM transaction t
            INNER JOIN category c ON t.category_id = c.id
            WHERE t.user_id = %s
            ORDER BY t.date DESC
            LIMIT 3
            """
        response = self.db.query(query, (user_id,))
        return [Transaction(*row) for row in response]
        
    def get_expenses(self, user_id):
        """
        Retrieves all expenses from the database.
        Params: user_id: The ID of the user
        Returns: [Transaction] - (transaction_id, user_id, name, description, amount, category_id, 0, date)
        """
        query = """
        SELECT t.transaction_id, t.user_id, t.name, t.description, t.amount, c.name, t.type, t.date
        FROM transaction t
        INNER JOIN category c ON t.category_id = c.id
        WHERE t.type = 0 AND t.user_id = %s
        """
        response = self.db.query(query, (user_id,))
        return [Transaction(*row) for row in response]
    
    def get_incomes(self, user_id):
        """
        Retrieves all incomes from the database.
        Params: user_id: The ID of the user
        Returns: [Transaction] - (transaction_id, user_id, name, description, amount, category_id, 1, date)
        """
        query = """
        SELECT t.transaction_id, t.user_id, t.name, t.description, t.amount, c.name, t.type, t.date
        FROM transaction t
        INNER JOIN category c ON t.category_id = c.id
        WHERE t.type = 1 AND t.user_id = %s
        """
        reponse = self.db.query(query, (user_id,))
        return [Transaction(*row) for row in reponse]
    
    def get_transaction_by_category(self, user_id, category_id):
        """
        Retrieves all transactions of a specific category from the database.
        Params: user_id: The ID of the user, category_id: The ID of the category
        Returns: [Transaction] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = """
        SELECT t.transaction_id, t.user_id, t.name, t.description, t.amount, c.name, t.type, t.date
        FROM transaction t
        INNER JOIN category c ON t.category_id = c.id
        WHERE t.user_id = %s AND c.id = %s
        """
        response = self.db.query(query, (user_id, category_id))
        return [Transaction(*row) for row in response]
    
    def get_transaction_by_date(self, user_id, date):
        """
        Retrieves all transactions of a specific date from the database.
        Params: user_id: The ID of the user, date: The date of the transactions
        Returns: [Transaction] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = """
        SELECT t.transaction_id, t.user_id, t.name, t.description, t.amount, c.name, t.type, t.date
        FROM transaction t
        INNER JOIN category c ON t.category_id = c.id
        WHERE t.user_id = %s AND t.date = %s
        """
        response = self.db.query(query, (user_id, date))
        return [Transaction(*row) for row in response]
    
    def get_transaction_by_date_fork(self, user_id, start_date, end_date):
        """
        Retrieves all transactions between two dates from the database.
        Params: user_id: The ID of the user, start_date, end_date
        Returns: [Transaction] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = """
        SELECT t.transaction_id, t.user_id, t.name, t.description, t.amount, c.name, t.type, t.date
        FROM transaction t
        INNER JOIN category c ON t.category_id = c.id
        WHERE t.user_id = %s AND t.date BETWEEN %s AND %s
        """
        response = self.db.query(query, (user_id, start_date, end_date))
        return [Transaction(*row) for row in response]
    # Sorts
    def get_all_transactions_sorted_by_date(self, user_id, reverse=False):
        """
        Retrieves all transactions sorted by date from the database.
        Params: user_id: The ID of the user, reverse: True to sort descending
        Returns: [Transaction] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = """
        SELECT t.transaction_id, t.user_id, t.name, t.description, t.amount, c.name, t.type, t.date
        FROM transaction t
        INNER JOIN category c ON t.category_id = c.id
        WHERE t.user_id = %s
        ORDER BY t.date
        """
        if reverse:
            query += " DESC"
        response = self.db.query(query, (user_id,))
        return [Transaction(*row) for row in response]
    
    def get_all_transactions_sorted_by_amount(self, user_id, reverse=False):
        """
        Retrieves all transactions sorted by amount from the database.
        Params: user_id: The ID of the user, reverse: True to sort descending
        Returns: [Transaction] - (transaction_id, user_id, name, description, amount, category_id, type, date)
        """
        query = """
        SELECT t.transaction_id, t.user_id, t.name, t.description, t.amount, c.name, t.type, t.date
        FROM transaction t
        INNER JOIN category c ON t.category_id = c.id
        WHERE t.user_id = %s
        ORDER BY t.amount
        """
        if reverse:
            query += " DESC"
        response = self.db.query(query, (user_id,))
        return [Transaction(*row) for row in response]
    
    #=================LOGIC - OPERATIONS=======================#
    def calculate_balance(self, user_id):
        """
        Calculates the balance of a user.
        Params: user_id: The ID of the user
        Returns: float - The balance
        """
        query = "SELECT SUM(amount) FROM transaction WHERE user_id = %s"
        result = self.db.query(query, (user_id,))
        response = result[0][0]
        return response
    
    def calculate_balance_by_date(self, user_id, date):
        """
        Calculates the balance of a user at a specific date.
        Params: user_id: The ID of the user, date: The date
        Returns: float - The balance
        """
        query = "SELECT SUM(amount) FROM transaction WHERE user_id = %s AND date <= %s ORDER BY date DESC"
        result = self.db.query(query, (user_id, date))
        response = result[0][0]
        return response
    
    def calculate_income(self, user_id):
        """
        Calculates the income of a user.
        Params: user_id: The ID of the user
        Returns: float - The income
        """
        query = "SELECT SUM(amount) FROM transaction WHERE user_id = %s AND type = 1"
        result = self.db.query(query, (user_id,))
        response = result[0][0]
        return response
    
    def calculate_expense(self, user_id):
        """
        Calculates the expenses of a user.
        Params: user_id: The ID of the user
        Returns: float - The expenses
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