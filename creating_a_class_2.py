class flower:
    def __init__(self, name, price, blue):
        self.name = name
        self.price = price
        self.blue = blue
        
        self.shop_name = "Lovely Bouquets"

    def count_price(self):
        if (self.name == "Tulip" and self.price >= 200):
            self.price  -= 25
            print("--------------")
            print(self.name)
            print(self.price)
        elif (self.name == "Rose" and self.blue == True):
            self.price += 200
            print("--------------")
            print(self.name)
            print(self.price)
        else:
            print("--------------")
            print(self.name)
            print(self.price)

        

rose = flower("Rose", 200, False) 
rose_blue = flower("Rose", 200, True) 
tulip_cheap = flower("Tulip", 150, False)
tulip_expensive = flower("Tulip", 250, False)
    
rose.count_price()
rose_blue.count_price()
tulip_cheap.count_price()
tulip_expensive.count_price()