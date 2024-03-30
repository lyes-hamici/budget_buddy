class Transaction:
    """Class that represents a transaction in the database."""
    def __init__(self, transaction_id, user_id, name, description, amount, category, type, date) -> None:
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.amount = amount
        self.category = category
        self.type = type
        self.date = date
        
    def __repr__(self) -> str:
        return f"{self.transaction_id}%{self.user_id}%{self.name}%{self.description}%{self.amount}%{self.category}%{self.type}%{self.date}"
    def return_list(self):
        """
        This method returns the transaction as a list.
        Returns: [list] - The transaction as a list
        indexes: 0 - transaction_id, 1 - user_id, 2 - name, 3 - description, 4 - amount, 5 - category_id, 6 - type, 7 - date
        """
        return [self.transaction_id, self.user_id, self.name, self.description, self.amount, self.category, self.type, self.date]