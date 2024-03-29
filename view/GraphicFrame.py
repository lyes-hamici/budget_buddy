import customtkinter as ctk
from customtkinter import CTkFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt

class GraphicFrame(CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.account_balance = 0
        self.create_widgets()

    def create_widgets(self):
        
        frame_graph = CTkFrame(master=self,fg_color='white', border_width=0,corner_radius=0, width=7000)
        frame_graph.pack(expand=True,fill = 'both')

        month = [8, 9, 10, 11, 12]
        turnover = [1360, 818, 8900, 7730, 1825]

        fig, axis = plt.subplots()
        axis.bar(month, turnover, label='turnover')
        axis.legend()

        canvas = FigureCanvasTkAgg(fig, master=frame_graph)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True,fill = 'both',side = 'right')


        label_sold = ctk.CTkLabel(master=frame_graph, text=f'Graphic', font=('helvetica', 30))
        label_sold.pack(pady=12, padx=100)





