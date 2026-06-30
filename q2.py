stocks={"AAPL": 150, "GOOGL": 2500, "MSFT": 300,"meta":350}
stockname=input("Enter the stock name:")
quantity=int((input("Enter the quantity:")))
if stockname in stocks:
    price=stocks[stockname]
    total=price*quantity
    print("Total price is",total)
else:
    print("Stock not found.") 