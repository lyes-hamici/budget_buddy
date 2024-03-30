import customtkinter as ctk
from customtkinter import CTkFrame , CTkButton , CTkEntry , CTkLabel

class TrasactionPage(CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.running = True
        self.create_widgets()



    def create_widgets(self):
        frame = CTkFrame(master=self, fg_color="mediumpurple1", width=700, corner_radius=0)
        frame.pack(expand=False, side=ctk.TOP, fill=ctk.X)

        balance_sold = CTkLabel(master=frame, text=f'Available balance : {self.master.get_balance()} €', font=('helvetica', 30))
        balance_sold.pack(pady=12, padx=100)

        frame2 = CTkFrame(master=self, fg_color="white", width=700, corner_radius=0)
        frame2.pack(expand=True, side=ctk.TOP, fill='both')

        # Left side - Entry widgets
        entry1 = CTkEntry(master=frame2, fg_color="white", width=20,placeholder_text="name")
        entry2 = CTkEntry(master=frame2, fg_color="white", width=20,placeholder_text="Description")
        entry3 = CTkEntry(master=frame2, fg_color="white", width=20,placeholder_text="Category")
        entry4 = CTkEntry(master=frame2, fg_color="white", width=20,placeholder_text="Values")
        entry5 = CTkEntry(master=frame2, fg_color="white", width=20,placeholder_text="Date")
        

        # Right side - Button widgets
        button1 = CTkButton(master=frame2, text="Add Transaction")

        button1.pack(pady=10, padx=50)

        entry1.pack(pady=10, padx=10,fill = ctk.X)
        entry2.pack(pady=10, padx=10,fill = ctk.X)
        entry3.pack(pady=10, padx=10,fill = ctk.X)
        entry4.pack(pady=10, padx=10,fill = ctk.X)
        entry5.pack(pady=10, padx=10,fill = ctk.X)

        # Getter methods for entry widgets
        self.entry1 = entry1
        self.entry2 = entry2
        self.entry3 = entry3
        self.entry4 = entry4
        self.entry5 = entry5
   

    # Getter methods to retrieve the content of each entry
    def get_entry1_text(self):
        return self.entry1.get()

    def get_entry2_text(self):
        return self.entry2.get()

    def get_entry3_text(self):
        return self.entry3.get()
    

    def get_entry4_text(self):
        return self.entry4.get()

    def get_entry5_text(self):
        return self.entry5.get()
