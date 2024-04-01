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
        entry_name = CTkEntry(master=frame2, fg_color="white", width=20,placeholder_text="name")
        entry_description = CTkEntry(master=frame2, fg_color="white", width=20,placeholder_text="Description")
        entry_category = CTkEntry(master=frame2, fg_color="white", width=20,placeholder_text="Category")
        entry_value = CTkEntry(master=frame2, fg_color="white", width=20,placeholder_text="Values")
        entry_date = CTkEntry(master=frame2, fg_color="white", width=20,placeholder_text="Date")
        

        # Right side - Button widgets
        button1 = CTkButton(master=frame2, text="Add Transaction", command=self.on_add_transaction_button_click)

        button1.pack(pady=10, padx=50)

        entry_name.pack(pady=10, padx=10,fill = ctk.X)
        entry_description.pack(pady=10, padx=10,fill = ctk.X)
        entry_category.pack(pady=10, padx=10,fill = ctk.X)
        entry_value.pack(pady=10, padx=10,fill = ctk.X)
        entry_date.pack(pady=10, padx=10,fill = ctk.X)

        # Getter methods for entry widgets
        self.entry_name = entry_name
        self.entry_description = entry_description
        self.entry_category = entry_category
        self.entry_value = entry_value
        self.entry_date = entry_date
   

    # Getter methods to retrieve the content of each entry
    def get_entry_name_text(self):
        return self.entry_name.get()

    def get_entry_description_text(self):
        return self.entry_description.get()

    def get_entry_category_text(self):
        return self.entry_category.get()
    
    def get_entry_value_text(self):
        return self.entry_value.get()

    def get_entry_date_text(self):
        return self.entry_date.get()

    def on_add_transaction_button_click(self):
        self.master.set_add_transaction(True)
        """
        self.entry_name.delete(0, ctk.END)
        self.entry_description.delete(0, ctk.END)
        self.entry_category.delete(0, ctk.END)
        self.entry_value.delete(0, ctk.END)
        self.entry_date.delete(0, ctk.END)
        """