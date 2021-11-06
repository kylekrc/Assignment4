
def getFruitInput():
    pieces_apple = int(input("Enter the number of apples to be purchased: "))
    pieces_orange = int(input("Enter the number of oranges to be purchased: "))
    return pieces_apple, pieces_orange

def CalcApple():
    priceApple = pieces_apple * 20
    priceOrange = pieces_orange * 25
    total_purchase = priceApple + priceOrange
    return total_purchase

def display(total_purchase):
    print(f"The total amount is {total_purchase} pesos.")

pieces_apple, pieces_orange = getFruitInput()
total_purchase = CalcApple()
display(total_purchase)