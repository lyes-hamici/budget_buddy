import customtkinter as ctk
from customtkinter import CTkFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt
import numpy as np

class GraphicFrame(CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.account_balance = 0
        self.create_widgets()

    def create_widgets(self):
        
        frame_graph = CTkFrame(master=self, fg_color='white', border_width=0, corner_radius=0, width=1200)
        frame_graph.pack(expand=True, fill='both')

        # Expense and date data (for example)
        dates = self.master.get_axis_x_graph_list()
        expenses = self.master.get_axis_y_graph_list()

        fig, axis = plt.subplots()

        # Bars for expenses
        bars = axis.bar(dates, expenses, color=['red' if x < 0 else 'green' for x in expenses])

        # Add horizontal lines to mark the y-axis
        axis.axhline(0, color='gray', linewidth=0.5)

        # Axis labels
        axis.set_xlabel('Date')
        axis.set_ylabel('Amount')

        # Rotate dates for better readability
        plt.xticks(rotation=45, ha='right')

        # Add legend
        axis.legend(handles=[bars[0], bars[-1]], labels=['Negative Balance', 'Positive Balance'])

        canvas = FigureCanvasTkAgg(fig, master=frame_graph)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill='both', side='right', padx=105, pady=10)

        label_title = ctk.CTkLabel(master=frame_graph, text='Bank Account Expenses', font=('helvetica', 16))
        label_title.pack(pady=12)








