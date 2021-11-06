
def getPurchaseInput():
    amount_money = int(input("Enter the amount of money you have on hand: "))
    apple_price = int(input("Enter the price for each apple: "))
    return amount_money, apple_price

def CompPurchase():
    pieces_apple = money // applePrice
    change = money % applePrice 
    return pieces_apple, change

def display(pieces_apple, change):
    print(f"You can buy {pieces_apple} apples and your change is {change} pesos.")

money, applePrice = getPurchaseInput()
pieces_apple, change = CompPurchase()
display(pieces_apple, change)