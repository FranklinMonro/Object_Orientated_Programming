class Stock:

    def __init__(self):
        self.stock = {}
       

    # Create a product and qty
    def create_product(self, product, product_qty):
        self.stock[product] = product_qty
        self.search_product(product)
        
    # Search for product
    def search_product(self, product):
        for key, value in self.stock.items():
            if product == key:
                print("\nProduct:",key, "Qty:",value,'\n')
            else:
                print("\nProduct is not in stock\n")
               
    # List all stock items
    def all_stock(self):
        for product, qty in self.stock.items():
            print("\nProduct:",product, "Qty:",qty,"\n")
                   
    # Issue product and deduct qty from stock
    def use_product(self, product, use_qty):
        self.stock[product] -= use_qty
        self.search_product(product)

    # Add qty to product
    def add_qty(self, product, add_qty):
        self.stock[product] += add_qty
        self.search_product(product)
    
