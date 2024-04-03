import customtkinter as ctk
from customtkinter import CTkFrame , CTkScrollableFrame
from .TransactionFrame import TransactionFrame

class Account(CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.transaction = TransactionFrame(self)
        self.create_widgets()

    def create_widgets(self):
        frame = CTkFrame(master=self, fg_color="mediumpurple1",  width=700,corner_radius=0)
        frame.pack(expand=False, side=ctk.TOP,fill = ctk.X)

        frame2 = CTkFrame(master=self, fg_color="azure3",  width=700,corner_radius=0)
        frame2.pack(expand=False, side=ctk.TOP,fill = ctk.X)

        button1 = ctk.CTkButton(master=frame2, text="amount", command=self.on_amount_button_click)
        button1.pack(side='left',padx=30, pady=5)

        button2 = ctk.CTkButton(master=frame2, text="date", command=self.on_date_button_click)
        button2.pack(side='left',padx=30, pady=5)


        self.frame3 = CTkScrollableFrame(master=self,fg_color="white",  width=7000,corner_radius=0)
        self.frame3.pack(expand=True, side=ctk.TOP,fill = 'both')

        label_sold = ctk.CTkLabel(master=frame, text=f'Available balance : {self.master.get_balance()} €', font=('helvetica', 30))#Replace self.account_balance with a the output of a function for get the sold of the account
        label_sold.pack(pady=12, padx=100)

        self.transaction.create_labels(self.frame3,self.master.get_transaction_list())

    def set_id_transaction(self,id_transaction):
        self.master.set_id_transaction(id_transaction)

    def update_labels(self):
        self.transaction.create_labels(self.frame3, self.master.get_transaction_list())
    
    def on_amount_button_click(self):
        self.master.set_sort_by_amount(True)
        """self.master.sort_reverse = not self.master.sort_reverse
        self.master.sort_type = "amount"
        self.update_labels()"""
    
    def on_date_button_click(self):

        self.master.reverse_list()
        self.pack_forget()
        self.master.update_account_page()
       

    def set_to_modify(self,id_transaction):
        self.master.set_to_modify(id_transaction)

    def get_to_modify(self):
        return self.master.get_to_modify()
    
    def store_transaction_data(self,  name, description, category, value, date):
        self.master.store_transaction(name, description, category, value, date)
    
    def set_validate_modification(self, value):
        self.master.set_validate_modification(value)
