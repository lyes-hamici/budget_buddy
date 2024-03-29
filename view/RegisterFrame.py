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
        frame = CTkFrame(master=self, width=400, height=834, corner_radius=45)
        frame.pack(pady=40, padx=300, fill='both', expand=True, side="left", anchor="center")
        
        label = CTkLabel(master=frame, text='Inscription', font=('helvetica', 30))
        label.pack(pady=12, padx=10)
        self.entry1 = CTkEntry(master=frame ,placeholder_text="Name")
        self.entry1.pack(pady=12, padx=10, anchor='nw')

        self.entry2 = CTkEntry(master=frame, placeholder_text="Firstname")
        self.entry2.pack(pady=12, padx=10, side='top', anchor='ne')

        self.entry3 = CTkEntry(master=frame, placeholder_text="Password", show="*")
        self.entry3.pack(pady=12, padx=10, anchor='w')

        self.entry31 = CTkEntry(master=frame, placeholder_text="Confirm Password", show="*")
        self.entry31.pack(pady=12, padx=10, anchor='e')

        self.entry4 = CTkEntry(master=frame, placeholder_text="Email")
        self.entry4.pack(pady=12, padx=10, anchor='sw')

        self.entry41 = CTkEntry(master=frame, placeholder_text="Confirm Email")
        self.entry41.pack(pady=12, padx=10, anchor='se')

        validation_button = CTkButton(master=frame, text="Click to valid", command=self.on_click_validation)
        validation_button.pack(pady=12, padx=10, anchor='s')


        quit_button = CTkButton(master=frame, text="Go back", command=self.on_go_back)
        quit_button.pack(pady=12, padx=10, anchor='s')
        
    # to this point new methods

    def on_click_validation(self):
        self.master.register_new_user()
    
    def on_go_back(self):
        self.master.set_value_display_page(1)
