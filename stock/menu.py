import sys
from stock import Stock

class Menu:
    # Display menu to user and receive choice to exucute

    def __init__(self):
        # Initialize class stock and create dictionary with choices
        self.stock = Stock()
        self.choices = { "1" : self.create_item,
                         "2" : self.search_item,
                         "3" : self.list_all,
                         "4" : self.use_item,
                         "5" : self.add_qty,
                         "6" : self.exit_stock
                         }
        
    def display_menu(self):
        # Display of options to user
        print('Stock Menu\n'
              '1. Create new item\n'
              '2. Search item\n'
              '3. List all items\n'
              '4. Issue item\n'
              '5. Add stock to existing item\n'
              '6. Exit program')
        
    def run(self):
        # Run the display menu for user
        choice = ''
        while choice != 6:
            self.display_menu()
            choice = input("Enter option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{} is not a valid choice".format(choice))

    def create_item(self):
        # Get new item with qty and pass into create_product
        product = input("Enter product: ")
        product_qty = int(input("Enter qty of product: "))
        self.stock.create_product(product, product_qty)

    def search_item(self):
        # Search item and display item and qty
        product = input("Search for product: ")
        self.stock.search_product(product)

    def list_all(self):
        # Display all products with qty
        self.stock.all_stock()

    def use_item(self):
        # Remove qty from item in stock
        product = input("Product to issue: ")
        use_qty = int(input("Qty to issue: "))
        self.stock.use_product(product, use_qty)

        
    def add_qty(self):
        # Add qty to item in stok
        product = input("Product to issue: ")
        add_qty = int(input("Qty to issue: "))
        self.stock.add_qty(product, add_qty)

    def exit_stock(self):
        print("Good Bye")
        sys.exit()
    
    



if __name__== "__main__":
    Menu().run()
                     
        

