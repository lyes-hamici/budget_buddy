import customtkinter as ctk
from .LoginFrame import LoginFrame
from .RegisterFrame import RegisterFrame
from .Home import Home
from .Account import Account
from .Dashboard import Dashboard

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
        self.value_name = ctk.StringVar()
        self.value_password = ctk.StringVar()
        self.value_remember_me = ctk.BooleanVar()
        self.balance = ctk.DoubleVar()
        self.value_display_page = 1

    #=================GETTERS & SETTERS=======================#
    #=================GETTERS=======================#
    def get_value_name(self):
        '''
        This method returns the value of the name.
        '''
        return self.value_name
    
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
    
    #=================SETTERS=======================#
    def set_value_name(self, value):
        '''
        This method sets the value of the name.
        '''
        self.value_name = value

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
        self.balance = value

    def set_value_display_page(self, value):
        '''
        This method sets the value of the display page.
        '''
        self.value_display_page = value
    
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
        self.config(bg="cornsilk1")

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
    
    def display_dashboard(self):
        '''
        This method displays the dashboard.
        '''
        self.dashboard = Dashboard(self)
        self.dashboard.pack(side='left', expand= True, fill='both')

    def main(self):
        '''
        This method is the main loop of the application.
        '''
        self.mainloop()
    
if __name__ == "__main__":
    app = Window()
    app.mainloop()