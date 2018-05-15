from POS import Inventory
from POS import Coffee
from POS import Bagel
import csv

def calculate(smth):
    total = 0
    for i in smth:
        total += i.price
    return total

Order = []
AllOrders = []
loop = True

var1 = input("Good Morning! How many sugar we have?")
var2 = input("How many cream we have?")
var3 = input("How many bagels we have?")
var4 = input("How many coffee we have?")

# invlist = []
# invlist.extend((var1, var2, var3, var4))
for i in file:
    file.write(var+i)

with open('database.csv','w') as file:
    file.write(var1, var2, var3, var4)
file.close()


with open('database.csv') as myCsv:
    readCSV = csv.reader(myCsv, delimiter=',')
    for i in readCSV:
        print(i, '\n')
# Inv = Inventory(var1,var2,var3,var4)
# while loop:
#     command = input("What's your order? (Coffee/Bagel or exit)/count ")
#     if command.lower() == "coffee":
#         temp = input("Hot or Ice?")
#         sugar = input("How many spoons of sugar do you want?")
#         cream = input("How much cream do you want?")
#         size = input("Large or Small?")
#         bagel = input("Do you want a Bagel?")
#         if bagel.lower() == "yes":
#             itm = input("How many bagels?")
#             Order.append(Coffee(temp, sugar, cream, size))
#             Order.append(Bagel(itm))
#             confirm = input("Your order is: {} cofee with {} spoons of sugar and {} of cream, with a {} size. With {} bagel(s)".format(temp.capitalize(), sugar, cream, size.capitalize(), itm))
#             AllOrders.append(temp+' coffee, '  + 'Sugar: ' + sugar + ' Cream: '+cream + ' Size: '+size + '. Bagel ' + itm)
#             Inv.sugar -= int(sugar)
#             Inv.cream -= int(cream)
#             Inv.bagel -= int(itm)
#             if size.lower() == 'large':
#                 Inv.coffee -= 2
#             elif size.lower() == 'small':
#                 Inv.coffee -= 1
#         else:
#             confirm = input("Your order is: {} cofee with {} spoons of sugar and {} of cream, with a {} size".format(temp.capitalize(), sugar, cream, size.capitalize()))
#             Order.append(Coffee(temp, sugar, cream, size))
#             AllOrders.append(temp+' coffee, '  + 'Sugar: ' + sugar + ' Cream: '+cream + ' Size: '+size)
#             Inv.sugar -= int(sugar)
#             Inv.cream -= int(cream)
#             if size.lower() == 'large':
#                 Inv.coffee -= 2
#             elif size.lower() == 'small':
#                 Inv.coffee -= 1
#
#     elif command.lower() == "bagel":
#         itm = input("How many bagels?")
#         Order.append(Bagel(itm))
#         confirm = input("Your order is: {} bagel(s)".format(itm))
#         Inv.bagel -= int(itm)
#         AllOrders.append('Bagel '+ itm)
#
#     elif command.lower() == "count":
#         print(calculate(Order))
#         print(Inv.sugar, Inv.cream, Inv.bagel, Inv.coffee)
#         Order = []
#
#     elif command.lower() == "exit":
#         print(AllOrders)
#         loop = False
#         break
