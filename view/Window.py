import customtkinter as ctk
class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter MVC")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.geometry("1280x720")
        self.config(bg="cornsilk1")

    
    def main(self):
        self.mainloop()
   
    
if __name__ == "__main__":
    app = Window()
    app.main()