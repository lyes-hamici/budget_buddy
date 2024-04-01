from view import Window
from model import Transaction_repository, User_repository, User
from services import Db, Graph

import threading
import time

class Controller:
    def __init__(self):
        self.db = Db()
        self.Transaction_repository = Transaction_repository(self.db)
        self.User_repository = User_repository(self.db)
        self.view = Window()
        self.old_value_display_page = 0
        self.thread_running = True
        self.user = None
        self.thread = threading.Thread(target=self.observer)
        self.thread.start()
        

    def set_old_value_display_page(self, value):
        self.old_value_display_page = value
        

    def observer(self):
        while self.thread_running:
            if self.view.id_transaction:
                self.remove_transaction(self.view.id_transaction)
                self.view.id_transaction = None
                self.get_all_transactions()
                """self.view.account.update_labels()"""
                self.flush_variables()
                self.view.account.pack_forget()
                self.get_all_transactions()
                self.view.update_account_page()
                self.get_graph()
            if self.view.add_transaction == True:
                self.add_transaction(   self.view.transaction.get_entry_name_text(),
                                        self.view.transaction.get_entry_description_text(),
                                        self.view.transaction.get_entry_value_text(), 
                                        self.view.transaction.get_entry_category_text(), 
                                        self.view.transaction.get_entry_date_text()
                                    )
                self.view.add_transaction = False
                self.get_all_transactions()
                self.get_graph()
            if self.view.value_display_page != 0:
                self.flush_variables()
                if self.user is not None:
                    self.view.set_balance(self.Transaction_repository.calculate_balance(self.user.user_id))
                    self.get_all_transactions()
                    print(" from view transaction list = ", self.view.transaction_list)
                    self.get_graph()
                self.forget_display()
                self.change_display()
            time.sleep(0.1)
            """if self.user is not None:  
                self.view.set_balance(self.Transaction_repository.calculate_balance(self.user.user_id))
                self.get_all_transactions()
                print("transaction list = ", self.view.transaction_list)"""
    
    def set_overdraft(self):
        if self.user.overdraft != self.User_repository.get_overdraft(self.user.user_id):
            self.user.overdraft = self.User_repository.get_overdraft(self.user.user_id)
        self.view.set_overdraft(self.user.overdraft)
        
    def change_display(self):
            if self.view.value_display_page == 1:

                if self.view.asking_for_creation:
                    if self.check_user_creation():
                        print("user created")
                        self.view.displayLoginPage()
                        self.set_old_value_display_page(1)
                        self.view.set_value_display_page(0)
                        self.view.asking_for_creation = False
                    else:
                        self.view.displayRegisterPage()
                        self.set_old_value_display_page(2)
                        self.view.set_value_display_page(0)
                        self.view.asking_for_creation = False
                else:
                    self.view.displayLoginPage()
                    self.set_old_value_display_page(1)
                    self.view.set_value_display_page(0)

            if self.view.value_display_page == 2:
                self.view.displayRegisterPage()
                self.set_old_value_display_page(2)
                self.view.set_value_display_page(0)
            if self.view.value_display_page == 3:
                if self.login():
                    if self.user is not None:  
                        self.view.set_balance(self.Transaction_repository.calculate_balance(self.user.user_id))
                        self.set_overdraft()
                        self.get_all_transactions()
                        print(" from view transaction list = ", self.view.transaction_list)
                        self.get_graph()
                    self.view.display_home_page()
                    self.set_old_value_display_page(3)
                    self.view.set_value_display_page(0)
                    print("entry values from login page")
                    print("value_name = ", self.view.value_mail)
                    print("value_password = ", self.view.value_password)
                else:
                    self.view.displayLoginPage()
                    self.set_old_value_display_page(1)
                    self.view.set_value_display_page(0)
                    
            if self.view.value_display_page == 4:
                self.view.display_account_page()
                self.set_old_value_display_page(4)
                self.view.set_value_display_page(0)

            if self.view.value_display_page == 5:
                self.view.display_graphic_page()
                self.set_old_value_display_page(5)
                self.view.set_value_display_page(0)

            if self.view.value_display_page == 6:
                self.view.display_transaction_page()
                self.set_old_value_display_page(6)
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
            self.view.dashboard.pack_forget()
            self.view.graphics.pack_forget()
        elif self.old_value_display_page == 6:
            self.view.dashboard.pack_forget()
            self.view.transaction.pack_forget()
    
    #=================LOGIN METHODS=======================#

    def get_entry_values_from_login_page(self):
        print("tes methods entry values from login page")
        self.view.value_mail = self.view.login_frame.user_entry.get()
        self.view.value_password = self.view.login_frame.user_pass.get()

    def login(self):
        self.get_entry_values_from_login_page()
        self.user = self.User_repository.connect_user(self.view.value_mail, self.view.value_password)
        if self.user:
            return True
        else:
            return False
        
        """if self.User_repository.verify_if_exist(self.view.value_mail):
            if self.User_repository.verify_if_correct(self.view.value_mail, self.view.value_password):
                self.user = self.User_repository.get_user(self.view.value_mail)
                return True
            else:
                print("wrong password")
                return False"""

    #=================REGISTER METHODS=======================#
    def get_entry_values_from_register_page(self):
        self.view.value_name = self.view.register_frame.entry1.get()
        self.view.value_firstname = self.view.register_frame.entry2.get()
        self.view.value_password = self.view.register_frame.entry3.get()
        self.view.value_password_confirm = self.view.register_frame.entry31.get()
        self.view.value_mail = self.view.register_frame.entry4.get()
        self.view.value_mail_confirm = self.view.register_frame.entry41.get()

    def check_user_creation(self):
        self.get_entry_values_from_register_page()
        if self.view.value_password == self.view.value_password_confirm and self.view.value_mail == self.view.value_mail_confirm:
            print("test input values passed")
            if self.User_repository.create_user(self.view.value_name, self.view.value_firstname, self.view.value_mail, self.view.value_password):
                return True
            else:
                return False
        else:
            return False

    def main(self):
        self.view.mainloop()

    def stop_thread(self):
        self.thread_running = False
        self.thread.join()

    #=================TRANSACTION METHODS=======================#
    def get_all_transactions(self):
        transaction_list = self.Transaction_repository.get_all_transactions_of_user(self.user.user_id)
        print ("transaction_list = ", transaction_list)
        for transaction in transaction_list:
            self.view.transaction_list.append(transaction.return_list())
        self.view.transaction_list.reverse()

    def three_last_transaction(self):
        transaction_list = self.Transaction_repository.get_last_three_transactions(self.user.user_id)
        for transaction in transaction_list:
            self.view.transaction_list.append(transaction.return_list())
        self.view.transaction_list.reverse()

    def add_transaction(self, name, description, amount, category, date):
        self.Transaction_repository.create_transaction(self.user.user_id, name, description, amount, category, date)

    def remove_transaction(self, id_transaction):
        print("remove transaction", id_transaction)
        self.Transaction_repository.delete_transaction(id_transaction)

    #=================GRAPHIC METHODS=======================#
    def get_graph(self):
        self.graph = Graph(self.user.user_id, self.Transaction_repository)
        self.view.axis_y_graph_list = self.graph.get_30_days_balance_list()
        self.view.axis_x_graph_list = self.graph.get_list_dates()

    #=================FLUSH VARIABLES=======================#
    def flush_variables(self):
        self.view.value_name = ""
        self.view.value_firstname = ""
        self.view.value_mail = ""
        self.view.value_mail_confirm = ""
        self.view.value_password = ""
        self.view.value_password_confirm = ""
        self.view.balance = 0
        self.view.asking_for_creation = False
        self.view.transaction_list = []
        self.view.axis_x_graph_list = []
        self.view.axis_y_graph_list = []    
        
# transaction_list = self.Transaction_repository.get_all_transactions_of_user(1)
# for transaction in transaction_list:
#     self.view.transaction_list.append(transaction.return_list())
