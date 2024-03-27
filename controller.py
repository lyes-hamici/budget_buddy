from model import Transaction_repository, User_repository
from view import Window
from services import Db

class Controller:
    def __init__(self):
        self.db = Db()
        self.Transaction_repository = Transaction_repository(self.db)
        self.User_repository = User_repository()
        self.view = Window()
    
    def update_transaction_list(self,user_id):
        transaction_list = self.Transaction_repository.get_all_transactions_of_user(user_id)
        for transaction in transaction_list:
            print(transaction.return_list())

if __name__ == "__main__":
    controller = Controller()
    controller.update_transaction_list(1)