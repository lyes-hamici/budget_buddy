import customtkinter as ctk
from customtkinter import CTkFrame , CTkButton , CTkEntry , CTkLabel

class TrasactionPage(CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.running = True
        self.create_widgets()



    def create_widgets(self):
        frame = CTkFrame(master=self, fg_color="mediumpurple1", width=700, corner_radius=0)
        frame.pack(expand=False, side=ctk.TOP, fill=ctk.X, pady=0)

        balance_sold = CTkLabel(master=frame, text=f'Available balance : {self.master.get_balance()} €', font=('helvetica', 30))
        balance_sold.pack(pady=12, padx=100)

        frame2 = CTkFrame(master=self, fg_color="white", width=700, corner_radius=0)
        frame2.pack(expand=True, side=ctk.TOP, fill='both')

        frame3 = CTkFrame(master=frame2, fg_color="white", border_color="#565B5E", border_width=2) 

        # Left side - Entry widgets
        entry_name = CTkEntry(master=frame2, fg_color="white", width=20,placeholder_text="name",placeholder_text_color="black",text_color="black")
        entry_description = CTkEntry(master=frame2, fg_color="white", width=20,placeholder_text="Description",placeholder_text_color="black",text_color="black")
        
        label_category = CTkLabel(master=frame3, text=f'Choose a category : ', text_color='black')
        
        combobox_category = ctk.CTkComboBox(master=frame3, values=["Food", "Health", "Leisure", "Transport", "Lodging", "Tax", "Daily expenses", "Salary", "Other"],
                                            command="""combobox_callback""")
        combobox_category.set("None")

        entry_value = CTkEntry(master=frame2, fg_color="white", width=20,placeholder_text="Values",placeholder_text_color="black",text_color="black")
        entry_date = CTkEntry(master=frame2, fg_color="white", width=20,placeholder_text="Date",placeholder_text_color="black",text_color="black")
        

        # Right side - Button widgets
        button1 = CTkButton(master=frame2, text="Add Transaction", command=self.on_add_transaction_button_click)

        button1.pack(pady=10, padx=50)

        entry_name.pack(pady=10, padx=200,fill = ctk.X)
        entry_description.pack(pady=10, padx=200,fill = ctk.X)
        frame3.pack(pady=10, padx=200,fill = ctk.X)
        label_category.pack(pady=10, padx=100, fill = ctk.X, side=ctk.LEFT, anchor=ctk.W)
        combobox_category.pack(pady=10, padx=100, fill = ctk.X, side=ctk.LEFT)
        entry_value.pack(pady=10, padx=200,fill = ctk.X)
        entry_date.pack(pady=10, padx=200,fill = ctk.X)

        # Getter methods for entry widgets
        self.entry_name = entry_name
        self.entry_description = entry_description
        self.entry_category = combobox_category
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