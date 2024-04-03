from datetime import datetime, timedelta

class Graph:
    def __init__(self,user, transaction_repository) -> None:
        self.user = user
        self.transaction_repository = transaction_repository
    
    def get_30_days_balance_list(self):
        """Returns the balance of the user for the last 30 days."""
        balance_list = []
        for i in range(30):
            date = datetime.now() - timedelta(days=i)
            balance = self.transaction_repository.calculate_balance_by_date(self.user, date)
            balance_list.append(balance)
        balance_list.reverse()
        return balance_list
    
    def get_list_dates(self):
        """Returns a list of the last 30 days."""
        date_list = []
        for i in range(30):
            date = datetime.now() - timedelta(days=i)
            date_list.append(date)
        date_list.reverse()
        return date_list
    
