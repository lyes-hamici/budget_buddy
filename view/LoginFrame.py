import customtkinter as ctk


class LoginFrame(ctk.CTkFrame):
    '''
    This class is the login frame of the application. It is the first frame displayed to the user when he launches the application.
    '''
    def __init__(self, master):
        super().__init__(master)
        self._create_widgets()

    def _create_widgets(self):
            '''
            This method creates the widgets of the login frame.
            It creates a frame, a label, an entry for the user, an entry for the password, a login button, a checkbox for remember me and a register button.
            '''
            frame = ctk.CTkFrame(master=self, width=1482, height=834, corner_radius=45)
            frame.pack(pady=40, padx=300, fill='both', expand=False, side="top", anchor="center")
            
            label = ctk.CTkLabel(master=frame, text='BUDGET BUDDY', font=('helvetica', 64))
            label.pack(pady=12, padx=10)

            self.user_entry = ctk.CTkEntry(master=frame, placeholder_text="Pseudo/mail", text_color='white')
            self.user_entry.pack(pady=12, padx=10)

            self.user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
            self.user_pass.pack(pady=12, padx=10)

            login_button = ctk.CTkButton(master=frame, text='Login', command=self.on_login_button_click)   
            login_button.pack(pady=12, padx=10)

            self.remember_checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me', variable=self.master.value_remember_me, onvalue=True, offvalue=False)
            self.remember_checkbox.pack(pady=12, padx=10)

            register_button = ctk.CTkButton(master=frame, text='Register', command=self.on_register_button_click)
            register_button.pack(pady=12, padx=10)

    #new def until this point
            
    def on_login_button_click(self):
        self.master.set_value_display_page(3)
    
    def on_register_button_click(self):
        self.master.set_value_display_page(2)