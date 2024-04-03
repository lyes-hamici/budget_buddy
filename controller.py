from view import Window
from model import Transaction_repository, User_repository
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
            
            if self.view.logout_request == True:
                self.user = None
                self.view.logout_request = False
                self.view.set_value_display_page(1)
                
            if self.view.to_modify:
                self.store_transaction_data()
                self.view.account.pack_forget()
                self.view.update_account_page()
                id_transaction = self.view.to_modify
                self.view.to_modify = None
                
            if self.view.validate_modification == True:
                self.store_new_transaction_data()
                self.Transaction_repository.update_transaction (

                    id_transaction,
                    self.user.user_id,
                    self.testing_entry_values()[0],
                    self.testing_entry_values()[1],
                    self.testing_entry_values()[2],
                    self.testing_entry_values()[3],
                    self.testing_entry_values()[4]

                )
                self.view.set_value_display_page(4)
                self.view.validate_modification = None
            elif self.view.validate_modification == False:
                self.view.set_value_display_page(4)
                self.view.validate_modification = None

            if self.view.id_transaction:
                self.remove_transaction(self.view.id_transaction)
                self.view.id_transaction = None
                self.get_all_transactions()
                self.flush_variables()
                self.view.account.pack_forget()
                self.get_all_transactions()
                self.view.update_account_page()
                self.get_graph()
                
            if self.view.sort_type == "amount":
                self.view.account.pack_forget()
                if self.view.sort_reverse == True:
                    self.get_all_transactions_by_amount(True)
                else:
                    self.get_all_transactions_by_amount()
                self.view.update_account_page()
            elif self.view.sort_type == "date":
                self.view.account.pack_forget()
                if self.view.sort_reverse == True:
                    self.get_all_transactions_by_date(True)
                else:
                    self.get_all_transactions_by_date()
                self.flush_variables()
                self.view.update_account_page()
                
            if self.view.search_request == True:
                self.view.search_request = False
                category = self.view.get_search_category()
                date = self.view.get_search_date()
                type = self.view.get_search_type()
                self.search_transaction(category, date, type)
                self.view.update_search_page()
                self.view.research_list = []
                
            if self.view.add_transaction == True:
                self.add_transaction(   
                                        self.view.transaction.get_entry_name_text(),
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
                    self.get_graph()
                self.forget_display()
                self.change_display()
            time.sleep(0.1)
        
    def set_overdraft(self):
        if self.user.overdraft != self.User_repository.get_overdraft(self.user.user_id):
            self.user.overdraft = self.User_repository.get_overdraft(self.user.user_id)
        self.view.set_overdraft(self.user.overdraft)
        
    def change_display(self):
            if self.view.value_display_page == 1:

                if self.view.asking_for_creation:
                    if self.check_user_creation():
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
                        self.get_graph()
                    self.view.display_home_page()
                    self.set_old_value_display_page(3)
                    self.view.set_value_display_page(0)
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
            
            if self.view.value_display_page == 7:
                self.view.display_search_page()
                self.set_old_value_display_page(7)
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
        elif self.old_value_display_page == 7:
            self.view.dashboard.pack_forget()
            self.view.search_frame.pack_forget()
    
    #=================LOGIN METHODS=======================#

    def get_entry_values_from_login_page(self):
        self.view.value_mail = self.view.login_frame.user_entry.get()
        self.view.value_password = self.view.login_frame.user_pass.get()

    def login(self):
        self.get_entry_values_from_login_page()
        self.user = self.User_repository.connect_user(self.view.value_mail, self.view.value_password)
        if self.user:
            return True
        else:
            return False

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
        self.set_transaction_list(transaction_list)
        
    def get_all_transactions_by_date(self, reverse = False):
        transaction_list = self.Transaction_repository.get_all_transactions_sorted_by_date(self.user.user_id, reverse)
        self.set_transaction_list(transaction_list)
    
    def get_all_transactions_by_amount(self, reverse = False):
        transaction_list = self.Transaction_repository.get_all_transactions_sorted_by_amount(self.user.user_id, reverse)
        self.set_transaction_list(transaction_list)
    
    

    def three_last_transaction(self):
        transaction_list = self.Transaction_repository.get_last_three_transactions(self.user.user_id)
        for transaction in transaction_list:
            self.view.transaction_list.append(transaction.return_list())
        self.view.transaction_list.reverse()

    def add_transaction(self, name, description, amount, category, date):
        self.Transaction_repository.create_transaction(self.user.user_id, name, description, amount, category, date)

    def remove_transaction(self, id_transaction):
        self.Transaction_repository.delete_transaction(id_transaction)
    
    def set_transaction_list(self,transaction_list):
        self.view.transaction_list = []
        for transaction in transaction_list:
            self.view.transaction_list.append(transaction.return_list())
        self.view.transaction_list.reverse()
    
    def search_transaction(self, category, date, type):
        if category == "None" or category == "" or category == " " or category == "Category":
            category = None
        if date == "" or date == " " or date == "None" or date == "Date":
            date = None
        if type == "" or type == " " or type == "None" or type == "Type":
            type = None
        elif type == "Income":
            type = 1
        elif type == "Expense":
            type = 0
        transaction_list = self.Transaction_repository.search_transaction(self.user.user_id, category, date, type)
        for transaction in transaction_list:
            self.view.research_list.append(transaction.return_list())
        self.view.research_list.reverse()           

    def modify_transaction(self, id_transaction, name, description, amount, category, date):
        self.Transaction_repository.update_transaction(id_transaction, name, description, amount, category, date)

    def store_transaction_data(self):
        self.default = {
            "name": self.view.transaction_name,
            "description": self.view.transaction_description,
            "amount": self.view.transaction_amount,
            "date": self.view.transaction_date,
            "category": self.view.transaction_category
        }

    def store_new_transaction_data(self):
        self.new = {
            "name": self.view.transaction_name,
            "description": self.view.transaction_description,
            "amount": self.view.transaction_amount,
            "date": self.view.transaction_date,
            "category": self.view.transaction_category
        }

    def testing_entry_values(self):
        for key in self.new:
            if self.new[key] == "" or self.new[key] == " ":
                self.new[key] = self.default[key]
        
        return self.new["name"], self.new["description"], self.new["amount"], self.new["category"], self.new["date"]

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
        self.view.overdraft = 0
        self.view.asking_for_creation = False
        self.view.transaction_list = []
        self.view.axis_x_graph_list = []
        self.view.axis_y_graph_list = []    