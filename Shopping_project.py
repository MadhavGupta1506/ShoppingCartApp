#shoping program
a={'shirt':500,"pant":1000,"t-shirt":300, "jacket":1500,"lower":300,"top":500,"bedsheet":1000,"towel":100,"cafre":250,"underwear":120,"handkrchief":120,"socks":50,"undergarments":80,"handglubs":250,"cap":150,"scarp":50,"leggie":250,"kurta":900,"pajama":300,"inner":250,"purse":350,"trowsers":900,"blazer":2000,"sherwani":1700,"jeans":1300,"tie":120}
print(a)
cart=[]
total=[]
def menu():
    print("------"*7)
    print("HELLO! SIR/MAM PRESS:")
    print	("1.TO ADD ITEM")
    print	("2.REMOVE ITEM")
    print("3.view basket")
    print	("4.Done")
    print("------"*7)
def cashier():
    user=input("Hello!Sir/Mam what do you wish to purchase today?").lower()
    while user!="quit":
         if user in a.keys():
            cart.append(user)
            user=input("Alright Sir/Mam your item is added on your basket anything else you wish to add?(Type quit to end)").lower()
         else:
            user=input("sorry!but we don't have that in our store. Anything else do you wanna purchase?(Type quit to end").lower()
menu()
c=int(input("enter a option:"))
while c!=0:
    if c==1:
        cashier()
        print("These are the items in your shopping basket:",cart)          
        adding_more=input("Do you wish to add something more?(Type yes or no):")
        if adding_more=="yes":
            cashier()
            print("These are the items that you have added in your cart:",cart)
            for item in cart:
                total.append(a[item])
                amount=sum(total)
            print("Here is the total of your items purchased in your basket:", amount)
        elif adding_more=="no":
            for item in cart:
                total.append(a[item])
                amount=sum(total)
            print("Here is the total of your items purchased in your basket:", amount)
   
        key=int(input("Enter 1 to go back to main menu:"))
        for k in range (2):
            if key!=1:
                while key!=1:
                    key=int(input("Enter 1 to go back to main menu: "))
                    while key!=1:
                        if key!=1:
                            print("Please! Enter a  valid key " )
                            break
                        elif key==1:
                            c=int(input("enter a option:: "))  
                            break
                        else:  
                            break
            else:
              menu()
              c=int(input("enter a option:"))           
    elif c==2:
        item=input("Enter the item you want to remove:")
        d=total.remove(a[item])
        r=cart.remove(item)
        amount=sum(total)
        print("These are the items that you have added in your cart:",cart)
        print("Here is the total of your items purchased in your basket:", amount)       
        key=int(input("Enter 1 to go back to main menu:"))
        for k in range (2):
            if key!=1:
                while key!=1:
                    key=int(input("Enter 1 to go back to main menu: "))
                    while key!=1:
                        if key!=1:
                            print("Please! Enter a  valid key: " )
                            break
                        elif key==1:
                            c=int(input("enter a option:"))  
                            break
                        else:  
                            break
            else:
              menu()
              c=int(input("enter a option:"))
    elif c==3:
            print(cart)
            key=int(input("Enter 1 to go back to main menu:"))
            for k in range (2):
                if key!=1:
                    while key!=1:
                        key=int(input("Enter 1 to go back to main menu:"))
                        while key!=1:
                            if key!=1:
                                print("Please! Enter a  valid key :" )
                                break
                            elif key==1:
                                c=int(input("enter a option: "))  
                                break
                            else:  
                                break
                else:
                  menu()
                  c=int(input("enter a option:"))

    elif c==4:
        amount=sum(total)
        print("This the bill of your shopping",amount,"Have a nice!please come come again " )
        break
	
