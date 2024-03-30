from datetime import datetime, timedelta

class Graph:
    def __init__(self,user, transaction_repository) -> None:
        self.user = user
        self.transaction_repository = transaction_repository
    
    def draw_graph(self, balance_list, date_list):
        pass
    
    def get_30_days_balance_list(self):
        balance_list = []
        for i in range(30):
            date = datetime.now() - timedelta(days=i)
            balance = self.transaction_repository.calculate_balance_by_date(self.user, date)
            balance_list.append(balance)
        balance_list.reverse()
        return balance_list
    
    def get_list_dates(self):
        date_list = []
        for i in range(30):
            date = datetime.now() - timedelta(days=i)
            date_list.append(date)
        date_list.reverse()
        return date_list
    
