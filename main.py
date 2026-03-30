# THE OMNI STORE

class Products:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
    
    def get_details(self):
        return f"{self.name} cost {self.price} and it remains {self.stock_quantity}"    

class Digital_Products(Products):
    def __init__(self, name, price, stock_quantity, file_size):
        super().__init__(name, price, stock_quantity)
        self.file_size = file_size

    def get_details(self):
        return f"{self.name} ({self.file_size}MB) costs {self.price}."

item1 = Products("Shirt", 1500, 20)
item2 = Products("Shoes", 5000, 10)
item3 = Digital_Products("E-book", 2500, 100, 20)

inventory = [item1, item2, item3]
available_items = [x for x in inventory if x.stock_quantity > 0]


def process_purchase(cart):
    grand_total = 0
    for x in cart:
        found = False
        for product in inventory:
            if x.lower() == product.name.lower() and product.stock_quantity > 0:
                product.stock_quantity -= 1
                grand_total += product.price
                print(f"Purchased {product.name} for {product.price}")
                found = True
                break
        if not found:
            print(f"Sorry, {x} is not in stock or doesn't exist.")
            
    print(f"Total Purchase is: {grand_total}")

while True:
    action = input("\nWhat would you like to do? (view / buy / exit): ").lower()

    if action == "view":
        for things in inventory:
            print(things.get_details())
        

    elif action == "buy":
            user_cart = [] # Start with an empty basket
            
            while True:
                item = input("Enter item name (or type 'done' to checkout): ").lower()
                if item == "done":
                    break
                user_cart.append(item) # Add the item to the basket
            
            # Now process the WHOLE basket at once
            process_purchase(user_cart)

    elif action == "exit":
        print("Closing the Omni Store. Goodbye!")
        break 

    else:
        print("Invalid command. Please try again.")
