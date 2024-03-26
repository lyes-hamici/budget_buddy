import customtkinter as ctk
from Home import Home

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter MVC")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.config(bg="cornsilk1")

    
    def main(self):
        self.mainloop()

    def display_home_page(self):
        self.home = Home(self)
        self.home.pack(expand=True, fill='both')
        self.main()
   
    
if __name__ == "__main__":
    app = Window()
    app.display_home_page()