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
        self.old_value_display_page = 0
        self.thread = threading.Thread(target=self.observer)
        self.thread.start()

    def set_old_value_display_page(self, value):
        self.old_value_display_page = value
        

    def observer(self):
        while True:
            if self.view.value_display_page != 0:
                self.forget_display()
                self.change_display()
            time.sleep(0.1)

    
   
    
    def change_display(self):
            if self.view.value_display_page == 1:
                self.view.displayLoginPage()
                self.set_old_value_display_page(1)
                self.view.set_value_display_page(0)
            if self.view.value_display_page == 2:
                self.view.displayRegisterPage()
                self.set_old_value_display_page(2)
                self.view.set_value_display_page(0)
            if self.view.value_display_page == 3:
                self.view.display_home_page()
                print("entry values from login page")
                print("value_name = ", self.view.value_name)
                print("value_password = ", self.view.value_password)
                self.set_old_value_display_page(3)
                self.view.set_value_display_page(0)
            if self.view.value_display_page == 4:
                self.view.display_account_page()
                self.set_old_value_display_page(4)
                self.view.set_value_display_page(0)

    def forget_display(self):
        if self.old_value_display_page == 1:
            self.get_entry_values_from_login_page()
            self.view.forgetLoginPage()
        elif self.old_value_display_page == 2:
            self.view.forgetRegisterPage()
        elif self.old_value_display_page == 3:
            self.view.home.pack_forget()
            self.view.dashboard.pack_forget()
        elif self.old_value_display_page == 4:
            self.view.account.pack_forget()
            self.view.dashboard.pack_forget()
        elif self.old_value_display_page == 5:
            self.view.graphics.pack_forget()
    
    #=================LOGIN METHODS=======================#

    def get_entry_values_from_login_page(self):
        print("tes methods entry values from login page")
        self.view.value_name = self.view.login_frame.user_entry.get()
        self.view.value_password = self.view.login_frame.user_pass.get()



    def main(self):
        self.view.mainloop()
