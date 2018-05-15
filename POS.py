class Inventory:

    def __init__(self, sugar, cream, bagels, coffee):


        myFile = open("database.csv", "r+", encoding="utf-8")

        self.sugar = sugar
        self.cream = cream
        self.bagel = bagels
        self.coffee = coffee

    def Left():
        print(self.sugar, self.cream, self.bagel, self.coffee)

class Coffee:

    def __init__(self, Hotorice, sugar, cream, size):
        self.Hotorice = Hotorice
        self.size = size
        self.sugar = sugar
        self.cream = cream



        if size.lower() == "large":
            self.price = 6500+(int(sugar)*200)+(int(cream)*300)
        elif size.lower() == "small":
            self.price = 5500+(int(sugar)*200)+(int(cream)*300)


class Bagel:

    def __init__(self, itm):
        self.price = int(itm)*4000
