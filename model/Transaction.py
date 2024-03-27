class Transaction:
    def __init__(self, transaction_id, user_id, name, description, amount, category_id, type, date) -> None:
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.amount = amount
        self.category_id = category_id
        self.type = type
        self.date = date
    def __repr__(self) -> str:
        return f"{self.transaction_id}%{self.user_id}%{self.name}%{self.description}%{self.amount}%{self.category_id}%{self.type}%{self.date}"
    def return_list(self):
        return [self.transaction_id, self.user_id, self.name, self.description, self.amount, self.category_id, self.type, self.date]