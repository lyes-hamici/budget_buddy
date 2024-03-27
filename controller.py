from view import Window
from model import Transaction_repository, User_repository
from services import Db

class Controller:
    def __init__(self):
        self.db = Db()
        self.Transaction_repository = Transaction_repository(self.db)
        self.User_repository = User_repository()
        self.view = Window()

    def main(self):
        self.view.mainloop()
