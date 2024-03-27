import customtkinter as ctk
from .LoginFrame import LoginFrame
from .RegisterFrame import RegisterFrame
from Home import Home
from Account import Account
from Dashboard import Dashboard

class Window(ctk.CTk):
    '''
    This class is the main window of the application. It is the parent of all the other frames. It is the main view of the application.
    '''
    def __init__(self):
        '''
        Constructor of the class. It initializes the main window of the application.
        '''
        super().__init__()
        self.title("Hess d'epargne")
        self.geometry("1280x720")
        self.minsize(1280, 720)
        self.maxsize(1280, 720)
        self.resizable(False, False)
        self.value_name = ctk.StringVar()
        self.value_password = ctk.StringVar()
        self.value_remember_me = ctk.BooleanVar()
        self.value_display_page = 1

    def set_value_display_page(self, value):
        '''
        This method sets the value of the display page.
        '''
        self.value_display_page = value

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
        self.forgetLoginPage()
        self.register_frame.pack(fill='both', expand=True)
    
    def forgetRegisterPage(self):
        '''
        this method hides the register page.
        '''
        self.register_frame.pack_forget()
        self.config(bg="cornsilk1")

    
    def main(self):
        self.mainloop()

    def display_home_page(self):
        self.home = Home(self)
        self.home.pack(expand=True, fill='both')
        self.main()


    def display_account_page(self):
        self.account = Account(self)
        self.account.pack(expand=True, fill='both')
        self.main()
    
    def display_dashboard(self):
        self.dashboard = Dashboard(self)
        self.dashboard.pack(expand= True, fill='both')
        self.main()

    
if __name__ == "__main__":
    app = Window()
    app.display_dashboard()