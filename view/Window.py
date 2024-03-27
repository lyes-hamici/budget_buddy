import customtkinter as ctk
from .LoginFrame import LoginFrame
from .RegisterFrame import RegisterFrame

class Window(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Tkinter MVC")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.config(bg="cornsilk1")
        self.display_login()

    
    def main(self):
        self.mainloop()

    def display_login(self):
        login_frame = LoginFrame(self)
        login_frame.pack(expand=True, fill='both')

    def displayRegisterPage(self):
        register_frame = RegisterFrame(self)
        LoginFrame(self).pack_forget()
        register_frame.pack(expand=True, fill='both')
   
    
if __name__ == "__main__":
    app = Window()
    app.main()