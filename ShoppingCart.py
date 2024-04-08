from tkinter import *
from tkinter import messagebox


root=Tk()
root.title("Shopping Cart")
root.iconbitmap("C:\\Users\\gmadh\\Downloads\\cart_icon-icons.com_48341.ico")

root.minsize(height=750,width=1030)
# root.maxsize(height=750, width=1030)
root.configure(bg="#72A0C1")

global f2
f2=LabelFrame().grid(row=0,column=0)

# This is dictionary of items in the store available
items={'Shirt':500,"Pant":1000,"T-Shirt":300, "Jacket":1500,"Lower":300,"Top":500,"Bedsheet":1000,"Towel":100,"Capri":250,"Underwear":120,"Handkerchief":30,"Socks":50,"Handglows":250,"Cap":150,"Scarp":50,"Leggy":250,"Kurta":900,"Pajama":300,"Inner":250,"Purse":350,"Trousers":900,"Blazer":2000,"Sherwani":1700,"Jeans":1300,"Tie":120}

# This is used to extract information from the dictionary and store them as a list
itemList=list(items)
itemsPriceList=list(items.values())


# Declared a variable sum to get total of all the items in the cart globally
global sum
sum=0

#Created a list to store cart items
cartItems=[]


# Created this function to add items to cart using buttons
def addCart(index):
    global sum
    global cartItems

    sum+=itemsPriceList[index]
    cartItems.append(itemList[index]) 


#Created a list to delete items
deleteCart=[]

def deleteConfirm():
    global sum
    for i in deleteCart:
        
        try:
            (cartItems.remove(f"{i[0]}"))
            sum-=i[1]
        except:
            continue    
        
    deleteWindow.destroy()


# This function update the value of sum
def deleteFunction(index):
    global deleteCart
    deleteCart.append((cartItems[index],items[cartItems[index]]))

#This is used to create a window of all the items present in the cart and to remove items from cart 
def removeItem():
    row_count=0
    column_count=0
    count=0
    global deleteWindow
    deleteWindow=Toplevel()
    deleteCancel=Button(deleteWindow,text="Cancel",command=CancelButton,bd=4)
    delete=Button(deleteWindow,text="Delete",bd=4,background="#ba0f30",activebackground="#880808",command=deleteConfirm)
    delete.grid(row=len(itemList)%9,column=0,sticky=N,padx=10,pady=10,ipadx=30,ipady=20)
    deleteCancel.grid(row=len(itemList)%9,column=1,sticky=N,padx=10,pady=10,ipadx=30,ipady=20)
    while(count!=len(cartItems)):
        if(column_count%6==0):
            row_count+=1
            column_count=0
        
        button=Button(deleteWindow,text=f"{cartItems[count]}\n {items[cartItems[count]]}",background="#ba0f30",height=2,width=12,padx=10,pady=10,command=lambda count=count:deleteFunction(count),activebackground="#880808")
        
        button.grid(row=row_count,column=column_count,padx=10,pady=20)
        
        column_count+=1
        count+=1

def CancelButton():
    deleteWindow.destroy()
    
        
        
#  Created this function to get the final price of the cart
def submitButton():
    
    response=messagebox.askokcancel("Submit","Do you wish to submit")
    if(response==True):
        top=Toplevel()
        top.title("Bill")
        top.iconbitmap("C:\\Users\\gmadh\\Downloads\\cart_icon-icons.com_48341.ico")
        top.configure(bg="#72A0C1")
    
        
        # This checks for the cart items, if 0 it label 0 to screen
        if(len(cartItems)==0):
            totalLabel=Label(top,bg="#72A0C1",text=sum,width=100,height=20,bd=5)
            totalLabel.pack()
        else:
            #If there are items in the cart this loop label them on the toplevel with their total
            for i in range(len(cartItems)):
                itemLabel=Label(top,text=f"{cartItems[i]}",font= ("Courier New",15,"bold"),bg="#72A0C1",padx=30,width=5)
                itemPrice=Label(top,text=f"{cartItems[i]}",bg="#72A0C1",font=("Courier New",15,"bold"))
                itemLabel.grid(row=i,column=0,padx=30)
                itemPrice.grid(row=i,column=1,padx=30)
            totalLabel=Label(top,text=sum,font=("Comic Sans MS", 25, "bold"),width=10,height=5,bd=5,bg="#72A0C1")
            totalLabel.grid(row=len(cartItems),column=1)

cartDisplay = None

#Creating a display cart function
def showCart():
    global cartDisplay
    itemNames=""
    if(cartDisplay):
        cartDisplay.destroy()
    cartDisplay=Label()
    
    for i in range(len(cartItems)):
        if(i%6==0):
            itemNames+="\n"    
        itemNames+=f"{cartItems[i]}\t"
    cartDisplay=Label(text=itemNames,padx=4,background="#72A0C1")
    cartDisplay.grid(row=8,column=0,pady=10,columnspan=6)
    root.minsize(height=850,width=1030)
    
# Created these variables to get values for the grid row and column
row_count=0
column_count=0
count=0

# This loop make the grid of buttons.
while(count!=len(items)):
    if(column_count%6==0):
        row_count+=1
        column_count=0
    
    button=Button(f2,text=f"{itemList[count]}\n {itemsPriceList[count]}",fg="#F0F8FF",background="#0066b2",height=2,width=12,padx=10,pady=10,command=lambda count=count:addCart(count),font=("Comic Sans MS", 12, ),activebackground="green")
 
    button.grid(row=row_count,column=column_count,padx=10,pady=20)
    
    column_count+=1
    count+=1

 
   
# This button submit the cart to the final billing
submit=Button(text="Submit",bg="green",bd=4,activebackground="#4F7942",command=submitButton)
submit.grid(row=len(itemList)%9,column=5,padx=10,pady=10,ipadx=30,ipady=20)


#This shows all the items present in the cart
itemsInCart=Button(text="Show Cart",command=showCart,bd=4,background="#ec9d0d",activebackground="#b78f0d")
itemsInCart.grid(row=len(itemList)%9,column=3,sticky=N,padx=10,pady=10,ipadx=30,ipady=20)


delete=Button(text="Delete Item",command=removeItem,bd=4,background="#ba0f30",activebackground="#880808")
delete.grid(row=len(itemList)%9,column=0,sticky=N,padx=10,pady=10,ipadx=30,ipady=20)





root.mainloop()