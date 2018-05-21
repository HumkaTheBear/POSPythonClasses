import sqlite3

class CoffeeShop:

    def __init__(self):
        pass

    class Item:
        def __init__(self, row):
            self.ID = row[0]
            self.ItemName = row[1]
            self.ItemPrice = row[2]
            self.QtyRemaining = row[3]

        def __repr__(self):
            return str(self.ID) + " " + self.ItemName


    def loaditemsfromdatabase(self):
        conn = sqlite3.connect('mydatabase')
        c = conn.cursor()
        c.execute('pragma foreign_keys=ON')

        c.execute('SELECT ID, ItemName, ItemPrice, QtyRemaining FROM ItemList')

        itemList = []
        for row in c.fetchall():
            itemList.append(CoffeeShop.Item(row))

        return itemList