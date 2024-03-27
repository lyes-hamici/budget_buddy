import customtkinter as ctk


class LoginFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.value_name = ctk.StringVar()
        self.value_password = ctk.StringVar()
        self.value_remember_me = """ctk.BooleanVar(value=self.master.get_remember_me_state())"""
        self.login_status = True
        self.is_button_clicked = False
        self.register_is_clicked = False
        self._create_widgets()

    def _create_widgets(self):
            frame = ctk.CTkFrame(master=self, width=1482, height=834, corner_radius=45)
            frame.pack(pady=40, padx=300, fill='both', expand=False, side="top", anchor="center")
            
            label = ctk.CTkLabel(master=frame, text='BUDGET BUDDY', font=('helvetica', 64))
            label.pack(pady=12, padx=10)

            self.user_entry = ctk.CTkEntry(master=frame, placeholder_text="Pseudo/mail", textvariable=self.value_name)
            self.user_entry.pack(pady=12, padx=10)

            self.user_pass = ctk.CTkEntry(master=frame, placeholder_text="mot de passe", textvariable=self.value_password , show="*")
            self.user_pass.pack(pady=12, padx=10)

            login_button = ctk.CTkButton(master=frame, text='Login', command=self.on_login_button_click)   
            login_button.pack(pady=12, padx=10)

            """self.remember_checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me', variable=self.value_remember_me, onvalue=True, offvalue=False)
            self.remember_checkbox.pack(pady=12, padx=10)"""

            register_button = ctk.CTkButton(master=frame, text='Register', command=self.on_click_register)
            register_button.pack(pady=12, padx=10)

    #new def until this point
            
    def on_login_button_click(self):
        self.master.login()
            
    #old def until this point need to see if it is still useful
        
    def get_register_is_clicked(self):
        return self.register_is_clicked
        

    def get_is_button_clicked(self):
        return self.is_button_clicked
    

    def on_click_register(self):
        print("Register button clicked")
        self.register_is_clicked = True

        # Handle further actions here


    def get_login_status(self):
        return self.login_status

    def set_login_status(self, status):
        self.login_status = status