class canteen:
    items_prices={'tea':[10,100],'coffee':[20,100],'poha':[30,100],'samosa':[20,50]}
    def order():
        print("Menu")
        for i in canteen.items_prices:
            print(i,"-->","price :",canteen.items_prices[i][0]," ,quantity available :",canteen.items_prices[i][1])
        order=input("enter items ").split()
        quantity=list(map(int,input("enter quantity of items ").split()))
        for i,j in enumerate(order):
            price=canteen.items_prices[j][0]*quantity[i]
            canteen.items_prices[j][1]=canteen.items_prices[j][1]-quantity[i]
            print(" price of :",j,price," available :",canteen.items_prices[j][1])
canteen.order()