from collections.abc import Iterable
from typing import Any, Tuple
import customtkinter as ctk
from customtkinter import CTkFrame, CTkButton

class Dashboard(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
    
    def create_widgets(self):
        frame = CTkFrame(master=self, fg_color="red", bg_color='blue', width=300, corner_radius=0)
        frame.pack(expand=True, fill=ctk.Y, anchor=ctk.W)
        
        home_button = CTkButton(master=frame, text="Home", width=50,bg_color='white', fg_color='black', border_width=1)
        account_button = CTkButton(master=frame, text="Account", width=50)
        graphics_button = CTkButton(master=frame, text="Graphics",width=50)
        logout_button = CTkButton(master=frame, text="Logout",width=50)
        
        home_button.pack(fill=ctk.X, expand=True)
        account_button.pack(fill=ctk.X, expand=True)
        graphics_button.pack(fill=ctk.X, expand=True)
        logout_button.pack(fill=ctk.X, expand=True)