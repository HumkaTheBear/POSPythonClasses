from CoffeePOS.CoffeeShopClasses import CoffeeShop as csc

ApplicationTools = csc()
ItemList = ApplicationTools.loaditemsfromdatabase()
Current_Order = []


def checkout(Current_Order):
    total = 0
    for i in Current_Order:
        total += i[0].ItemPrice * i[1]

    print("Your total is ", total)
    input("Press enter to continue...")

def closeapp():
    ApplicationTools.updateinventory(ItemList)
    exit()

while True:
    print("Select your order")
    for i in ItemList:
        print(i)
    print("101 Check Out")
    print("102 Exit")
    selection = int(input()) - 1

    if selection == 100:
        checkout(Current_Order)
        Current_Order = []
    elif selection == 101:
        closeapp()
    else:
        qty = int(input("How many?"))
        ItemList[selection].QtyRemaining -= qty
        selectedItem = ItemList[selection]

        Current_Order.append([selectedItem, qty])