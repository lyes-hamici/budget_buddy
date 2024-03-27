import customtkinter as ctk
from Home import Home
from Account import Account
from Dashboard import Dashboard

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Hess d'epargne")
        self.geometry("1280x720")
        self.minsize(1280, 720)
        self.maxsize(1280, 720)
        self.resizable(False, False)
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