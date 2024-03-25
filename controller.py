import view
import model

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

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