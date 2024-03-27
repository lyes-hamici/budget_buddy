from collections.abc import Iterable
from typing import Any, Tuple
import customtkinter as ctk
from customtkinter import CTkFrame, CTkButton

class Dashboard(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
    
    def create_widgets(self):
        frame = CTkFrame(master=self, fg_color="azure3", corner_radius=0)
        frame.pack(expand=True, fill=ctk.Y, anchor=ctk.W)
        
        home_button = CTkButton(master=frame, text="Home",fg_color="white",hover_color="mediumpurple1",border_color="black",text_color="black",border_width=2,corner_radius=30)
        account_button = CTkButton(master=frame, text="Account",fg_color="white",hover_color="mediumpurple1",border_color="black",text_color="black",border_width=2,corner_radius=30)
        graphics_button = CTkButton(master=frame, text="Graphics",fg_color="white",hover_color="mediumpurple1",border_color="black",text_color="black",border_width=2,corner_radius=30)
        logout_button = CTkButton(master=frame, text="Logout",fg_color="white",hover_color="mediumpurple1",border_color="black",text_color="black",border_width=2,corner_radius=30)
        
        home_button.pack(expand = True,padx = 5)
        account_button.pack(expand = True,padx = 5)
        graphics_button.pack(expand = True,padx = 5)
        logout_button.pack(expand = True,padx = 5)