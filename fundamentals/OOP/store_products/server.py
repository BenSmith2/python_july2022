class Store:
    def __init__(self, name):
        self.name = name
        self.products=[]

    def add_product(self, new_product):
        self.products.append(new_product)

    def view_products(self):
        print(self.products)
    
    def inflation(self, percentage_increase):
        for product in self.products:
            product.update_price(percentage_increase, True)
    
    def clearance(self,item_name, percentage_decrease):
        for product in self.products:
            if product == item_name:
                product.update_price(percentage_decrease, False)


class Product:
    def __init__(self, name, price, category):
        self.name=name
        self.price=price
        self.category=category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price*percent_change
            return self.price
        if is_increased == False:
            self.price -= self.price*percent_change
            return self.price

    def print_info(self):
        print(f'{self.name} {self.price}')

    def __str__(self):
        return(f'{self.name} {self.price}')
    
    def __repr__(self):
        return f'{(self.name.capitalize())} ${self.price}'


vons= Store("Vons")
cheerios = Product("cheerios", 6, "food")
fruitloops = Product("Fruit Loops", 7, "food")
vons.add_product(cheerios)
vons.add_product(fruitloops)
vons.view_products()
vons.inflation(.1)
vons.view_products()
vons.clearance(fruitloops, .5)
vons.view_products()