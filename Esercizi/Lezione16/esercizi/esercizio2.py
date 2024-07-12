'''
Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione di ricette e i loro ingredienti.
Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.
    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.
    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    - list_recipes(): Elenca tutte le ricette esistenti.
    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
'''

class RecipeManager:
    def __init__(self):
        self.recipes = {}

    def create_recipe(self, name, ingredients):
        if name in self.recipes:
            return "La ricetta esiste già."
        else:
            self.recipes[name] = ingredients
            return {name: ingredients}

    def add_ingredient(self, recipe_name, ingredient):
        if recipe_name not in self.recipes:
            return "La ricetta non esiste."
        elif ingredient in self.recipes[recipe_name]:
            return "L'ingrediente esiste già."
        else:
            self.recipes[recipe_name].append(ingredient)
            return {recipe_name: self.recipes[recipe_name]}

    def remove_ingredient(self, recipe_name, ingredient):
        if recipe_name not in self.recipes:
            return "La ricetta non esiste."
        elif ingredient not in self.recipes[recipe_name]:
            return "L'ingrediente non è presente."
        else:
            self.recipes[recipe_name].remove(ingredient)
            return {recipe_name: self.recipes[recipe_name]}

    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        if recipe_name not in self.recipes:
            return "La ricetta non esiste."
        elif old_ingredient not in self.recipes[recipe_name]:
            return "L'ingrediente non è presente."
        else:
            index = self.recipes[recipe_name].index(old_ingredient)
            self.recipes[recipe_name][index] = new_ingredient
            return {recipe_name: self.recipes[recipe_name]}

    def list_recipes(self):
        return list(self.recipes.keys())

    def list_ingredients(self, recipe_name):
        if recipe_name not in self.recipes:
            return "La ricetta non esiste."
        else:
            return self.recipes[recipe_name]

    def search_recipe_by_ingredient(self, ingredient):
        result = {}
        for recipe, ingredients in self.recipes.items():
            if ingredient in ingredients:
                result[recipe] = ingredients
        if result:
            return result
        else:
            return "Nessuna ricetta contiene l'ingrediente."


# Test

manager = RecipeManager()
print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"]))
print(manager.add_ingredient("Torta di mele", "Zucchero"))
print(manager.list_recipes()) # ['Torta di mele']
print(manager.list_ingredients("Torta di mele"))
print(manager.search_recipe_by_ingredient("Uova"))

# Output:
# {'Torta di mele': ['Farina', 'Uova', 'Mele']}
# {'Torta di mele': ['Farina', 'Uova', 'Mele', 'Zucchero']}
# ['Torta di mele']
# ['Farina', 'Uova', 'Mele', 'Zucchero']
# {'Torta di mele': ['Farina', 'Uova', 'Mele', 'Zucchero']}


manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))

# Output:
# {'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella']}
# {'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella', 'Basilico']}
# {'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
# {'Pizza Margherita': ['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
# ['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']


manager = RecipeManager()
print(manager.create_recipe("Spaghetti alla Carbonara", ["Spaghetti", "Uova", "Guanciale", "Pecorino Romano", "Pepe"]))
print(manager.search_recipe_by_ingredient("Uova"))

# Output:
# {'Spaghetti alla Carbonara': ['Spaghetti', 'Uova', 'Guanciale', 'Pecorino Romano', 'Pepe']}
# {'Spaghetti alla Carbonara': ['Spaghetti', 'Uova', 'Guanciale', 'Pecorino Romano', 'Pepe']}