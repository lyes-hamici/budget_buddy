import customtkinter as ctk
from .LoginFrame import LoginFrame
from .RegisterFrame import RegisterFrame
from .Home import Home
from .Account import Account
from .Dashboard import Dashboard
from .GraphicFrame import GraphicFrame
from .TransactionPage import TrasactionPage
from .SearchPage import SearchPage

class Window(ctk.CTk):
    '''
    This class is the main window of the application. It is the parent of all the other frames. It is the main view of the application.
    '''
    def __init__(self):
        '''
        Constructor of the class. It initializes the main window of the application.
        '''
        super().__init__()
        self.title("Tkinter MVC")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.config(bg="black")
        self.protocol("WM_DELETE_WINDOW", self.quit)
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        self.value_display_page = 1
        # Variables for the login page & register page
        self.value_name = ctk.StringVar()
        self.value_firstname = ctk.StringVar()
        self.value_mail = ctk.StringVar()
        self.value_mail_confirm = ctk.StringVar()
        self.value_password = ctk.StringVar()
        self.value_password_confirm = ctk.StringVar()
        self.value_remember_me = ctk.BooleanVar()
        self.balance = ctk.DoubleVar()
        self.overdraft = ctk.DoubleVar()
        self.asking_for_creation = False
        self.add_transaction = False
        # Variables for the account page
        self.transaction_list = []
        self.id_transaction = None
        self.sort_reverse = False
        self.sort_by_amount = False
        
        self.to_modify = None
        self.validate_modification = None

        self.transaction_name = ""
        self.transaction_description = ""
        self.transaction_amount = ""
        self.transaction_date = ""
        self.transaction_type = ""
        self.transaction_category = ""
        # Variables for the graphic page
        self.axis_x_graph_list = []
        self.axis_y_graph_list = []
        # Variables for the dashboard
        self.logout_request = False
        # Variables for the search page
        self.research_list = []
        self.search_request = False
        self.search_category = ''
        self.search_date = ''
        self.search_type = ''

        
        

    #=================GETTERS & SETTERS=======================#
    #=================GETTERS=======================#
    def get_value_mail(self):
        '''
        This method returns the value of the name.
        '''
        return self.value_mail
    
    def get_value_password(self):
        '''
        This method returns the value of the password.
        '''
        return self.value_password
    
    def get_value_remember_me(self):
        '''
        This method returns the value of the remember me.
        '''
        return self.value_remember_me
    
    def get_balance(self):
        '''
        This method returns the value of the balance.
        '''
        return self.balance
    
    def get_transaction_list(self):
        '''
        This method returns the transaction list.
        '''
        return self.transaction_list
    
    def get_axis_x_graph_list(self):
        '''
        This method returns the x axis graph list.
        '''
        return self.axis_x_graph_list
    
    def get_axis_y_graph_list(self):
        '''
        This method returns the y axis graph list.
        '''
        return self.axis_y_graph_list
    
    def get_overdraft(self):
        '''
        This method returns the overdraft.
        '''
        return self.overdraft
    
    def get_to_modify(self):
        '''
        This method returns the to modify.
        '''
        return self.to_modify
    
    def get_search_request(self):     
        '''
        This method returns the search request.
        '''
        return self.search_request
    
    def get_search_category(self):
        '''
        This method returns the search category.
        '''
        return self.search_category
    
    def get_search_date(self):
        '''
        This method returns the search date.
        '''
        return self.search_date
    
    def get_research_list(self):
        '''
        This method returns the research list.
        '''
        return self.research_list
    
    def get_search_type(self):
        '''
        This method returns the research list.
        '''
        return self.search_type
    #=================SETTERS=======================#
    def set_value_mail(self, value):
        '''
        This method sets the value of the name.
        '''
        self.value_mail = value

    def set_value_password(self, value):
        '''
        This method sets the value of the password.
        '''
        self.value_password = value

    def set_value_remember_me(self, value):
        '''
        This method sets the value of the remember me.
        '''
        self.value_remember_me = value
    
    def set_balance(self, value):
        '''
        This method sets the value of the balance.
        '''
        self.balance = format(value, '.2f')

    def set_value_display_page(self, value):
        '''
        This method sets the value of the display page.
        '''
        self.value_display_page = value

    def set_value_asking_for_creation(self, value):
        '''
        This method sets the value of the asking for creation.
        '''
        self.asking_for_creation = value

    def set_add_transaction(self, value):
        '''
        This method sets the value of the add transaction.
        '''
        self.add_transaction = value

    def set_id_transaction(self, id_transaction):
        '''
        This method sets the id of the transaction.

        args:
            id_transaction : [int] - The id of the transaction.
        '''
        self.id_transaction = id_transaction
    
    def set_overdraft(self, value):
        '''
        This method sets the value of the overdraft.
        '''
        self.overdraft = value

    def set_logout_request(self, value):
        '''
        This method sets the value of the logout request.
        '''
        self.logout_request = value
    
    def set_to_modify(self, value):
        '''
        This method sets the value of the to modify.
        '''
        self.to_modify = value

    def set_validate_modification(self, value):
        '''
        This method validates the modification.

        args:
            value : [bool] - The value to validate.
        '''
        self.validate_modification = value

    def store_transaction(self, name, description, category, value, date):
        '''
        This method stores the transaction.

        args:
            name : [str] - The name of the transaction.
            description : [str] - The description of the transaction.
            category : [str] - The category of the transaction.
            value : [float] - The value of the transaction.
            date : [str] - The date of the transaction.
        '''
        self.transaction_name = name
        self.transaction_description = description
        self.transaction_category = category
        self.transaction_amount = value
        self.transaction_date = date
    def set_search_request(self, value):
        '''
        This method sets the value of the search request.
        '''
        self.search_request = value
    
    def set_search_category(self, value):
        '''
        This method sets the value of the search category.
        '''
        self.search_category = value
    
    def set_search_date(self, value):
        '''
        This method sets the value of the search date.
        '''
        self.search_date = value
    
    def set_search_type(self, value):
        '''
        This method sets the value of the search type.
        '''
        self.search_type = value

    def set_sort_by_amount(self, value):
        '''
        This method sets the value of the sort by amount.
        '''
        self.sort_by_amount = value

    #=================DISPLAY METHODS=======================#

    def displayLoginPage(self):
        '''
        this method displays the login page.
        '''
        self.login_frame = LoginFrame(self)
        self.login_frame.pack(fill='both', expand=True)

    def forgetLoginPage(self):
        '''
        This method hides the login page.
        '''
        self.login_frame.pack_forget()


    def displayRegisterPage(self):
        '''
        this method displays the register page.
        '''
        self.register_frame = RegisterFrame(self)
        self.register_frame.pack(fill='both', expand=True)
    
    def forgetRegisterPage(self):
        '''
        this method hides the register page.
        '''
        self.register_frame.pack_forget()

    def display_home_page(self):
        '''
        This method displays the home page.
        '''
        self.home = Home(self)
        self.display_dashboard()
        self.home.pack(side='left', expand=True, fill='both')


    def display_account_page(self):
        '''
        This method displays the account page.
        '''
        self.display_dashboard()
        self.account = Account(self)
        self.account.pack(side='left', expand=True, fill='both')

    def update_account_page(self):
        '''
        This method updates the account page.
        '''
        self.account = Account(self)
        self.account.pack(side='left', expand=True, fill='both')

    def display_graphic_page(self):
        self.display_dashboard()
        self.graphics = GraphicFrame(self)
        self.graphics.pack(side='left', expand=True, fill='both')


    def display_transaction_page(self):
        self.display_dashboard()
        self.transaction = TrasactionPage(self)
        self.transaction.pack(side='left', expand=True, fill='both')
    
    def display_dashboard(self):
        '''
        This method displays the dashboard.
        '''
        self.dashboard = Dashboard(self)
        self.dashboard.pack(side='left', expand= False, fill='both')
    
    def display_search_page(self):
        '''
        this method displays the register page.
        '''
        self.display_dashboard()
        self.search_frame = SearchPage(self)
        self.search_frame.pack(fill='both', expand=True)
    
    def update_search_page(self):
        '''
        This method updates the search page.
        '''
        self.search_frame.pack_forget()
        self.search_frame = SearchPage(self)
        self.search_frame.pack(fill='both', expand=True)

    def reverse_list(self):
        '''
        This method reverses the list.
        '''
        self.transaction_list = sorted(self.transaction_list, key=lambda x: x[7], reverse=True)
        print("transaction_list reversed")
        print("=====================================")
        print("=====================================")
    

    def main(self):
        '''
        This method is the main loop of the application.
        '''
        self.mainloop()
    
if __name__ == "__main__":
    app = Window()
    app.mainloop()