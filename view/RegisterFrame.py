import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton


class RegisterFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        
        self.running = True
        self.value_name = ctk.StringVar()
        self.value_firstname = ctk.StringVar()
        self.value_password = ctk.StringVar()
        self.value_mail = ctk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        frame = CTkFrame(master=self, width=1482, height=834, corner_radius=45)
        frame.pack(pady=40, padx=300, fill='both', expand=False, side="top", anchor="center")
        
        label = CTkLabel(master=frame, text='Inscription to Harmony', font=('helvetica', 30))
        label.pack(pady=12, padx=10)

        label1 = CTkLabel(master=frame, text="Name:", font=("Arial", 12))
        label1.pack(pady=12, padx=10)
        self.entry1 = CTkEntry(master=frame , textvariable=self.value_name)
        self.entry1.pack(pady=12, padx=10)

        label2 = CTkLabel(master=frame, text="Firstname:", font=("Arial", 12))
        label2.pack(pady=12, padx=10)
        self.entry2 = CTkEntry(master=frame, textvariable=self.value_firstname)
        self.entry2.pack(pady=12, padx=10)

        label3 = CTkLabel(master=frame, text="Password:", font=("Arial", 12))
        label3.pack(pady=12, padx=10)
        self.entry3 = CTkEntry(master=frame, textvariable=self.value_password, show="*")
        self.entry3.pack(pady=12, padx=10)

        label4 = CTkLabel(master=frame, text="Email:", font=("Arial", 12))
        label4.pack(pady=12, padx=10)
        self.entry4 = CTkEntry(master=frame, textvariable=self.value_mail)
        self.entry4.pack(pady=12, padx=10)

        validation_button = CTkButton(master=frame, text="Click to valid", command=self.on_click_validation)
        validation_button.pack(pady=12, padx=10)


        quit_button = CTkButton(master=frame, text="Go back", command=self.on_go_back)
        quit_button.pack(pady=12, padx=10)
        
    # to this point new methods

    def on_click_validation(self):
        self.master.register_new_user()
    
    def on_go_back(self):
        self.master.set_value_display_page(1)
