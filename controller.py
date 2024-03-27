import threading
from view import Window
from model import Transaction_repository, User_repository
from services import Db

import threading
import time

class Controller:
    def __init__(self):
        self.db = Db()
        self.Transaction_repository = Transaction_repository(self.db)
        self.User_repository = User_repository()
        self.view = Window()
        self.thread = threading.Thread(target=self.observer)
        self.thread.start()

    def observer(self):
        while True:
            if self.view.value_display_page != 0:
                self.change_display()
            time.sleep(0.1)

    
   
    
    def change_display(self):
            if self.view.value_display_page == 1:
                self.view.displayLoginPage()
                self.view.set_value_display_page(0)
            if self.view.value_display_page == 2:
                self.view.displayRegisterPage()
                self.view.set_value_display_page(0)


    def main(self):
        controller_thread = threading.Thread(target=self.controller_loop)
        controller_thread.start()
        self.view.mainloop()
    
    def controller_loop(self):
        pass
        
if __name__ == "__main__":
    controller = Controller()
    controller.main()
