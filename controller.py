from view import Window
from model import Model

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = Window()

    def main(self):
        self.view.mainloop()
    

    """
    Exemple of use of the controller : 
    
        def update_balance(self):
            # Logic
            balance = self.model.get_balance()
            # View update
            self.view.update_balance(balance)

    """
    
    
"""
Exemple of use : 

if __name__ == "__main__":
    model = Model  
    view = View()
    controller = Controller(model, view)
    controller.update_balance()  # Met à jour le solde affiché dans la vue
    view.mainloop()  # Lance l'interface graphique
    
"""