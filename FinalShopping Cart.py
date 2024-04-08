import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import messagebox

root=Tk()
root.title("Inventory App")
root.iconbitmap("C:\\Users\\gmadh\\Downloads\\cart_icon-icons.com_48341.ico")


# Created a database to store all the shop information
# conn=sqlite3.connect("Shop.db")
# c=conn.cursor()
# c.execute('''Create Table Inventory
#           (ProductName varchar(50),
#           Quantity int,
#           Price int)''')
# conn.commit()
# c.close()


# A layout to access database
# conn=sqlite3.connect("Shop.db")
# c=conn.cursor()


# conn.commit()
# c.close()

# Declared a variable sum to get total of all the items in the cart globally

#Created a list to store cart items
cartItems=[]

global sum
sum=0
def edit():
    global update
    update=Tk()
    update.title("Inventory App")
    update.iconbitmap("C:\\Users\\gmadh\\Downloads\\cart_icon-icons.com_48341.ico")
    global ProductName,Quantity,price,recordId
    
    recordIdLabel=Label(update,text="Enter Oid:")
    recordIdLabel.grid(row=0,column=0)
    recordId=Entry(update)
    recordId.grid(row=0,column=1)
    
    ProductNameLabel=Label(update,text="Enter Product Name:")
    ProductNameLabel.grid(row=1,column=0)
    ProductName=Entry(update)
    ProductName.grid(row=1,column=1)

    QuantityLabel=Label(update,text="Enter Quantity:")
    QuantityLabel.grid(row=2,column=0)
    Quantity=Entry(update)
    Quantity.grid(row=2,column=1)

    priceLabel=Label(update,text="Enter Price:")
    priceLabel.grid(row=3,column=0)
    price=Entry(update)
    price.grid(row=3,column=1)
    
    submitButton=Button(update,text="Submit",command=UpdateDatabase)
    submitButton.grid(row=4,column=1,columnspan=2)
    
def UpdateDatabase():
    #Creating a database or connecting to database
    conn=sqlite3.connect("Shop.db")
    # Creating a cursor
    c=conn.cursor()
    c.execute("""Update Inventory SET
              ProductName=:ProductName, 
              Quantity=:Quantity,
              Price=:Price
              WHERE Oid=:Oid
              """,{
                    "ProductName":ProductName.get(),
                    "Quantity":Quantity.get(),
                    "Price":price.get(),
                    "Oid":recordId.get()
              })

    conn.commit()

    #Disconnecting
    conn.close()
    
    update.destroy()


def showCart():
    cartWindow=Tk()
    cartWindow.title("Cart")
    cartWindow.iconbitmap("C:\\Users\\gmadh\\Downloads\\cart_icon-icons.com_48341.ico")
    allItems=""
    allQuantity=""
    allPrice=""
    for tupleCart in cartItems:
        allItems+=tupleCart[0]+"\n"
        allQuantity+=str(tupleCart[1])+"\n"
        allPrice+=str(items[tupleCart[0]]*tupleCart[1])+"\n"
    allItemsLabel=Label(cartWindow,text=allItems)
    allItemsLabel.grid(row=1,column=0)
    ItemsLabel=Label(cartWindow,text="Items",font=("Arial",15,"bold"))
    ItemsLabel.grid(row=0,column=0)

    quantityLabel=Label(cartWindow,text="Quantity",font=("Arial",15,"bold"))
    quantityLabel.grid(row=0,column=1)
    allQuantityLabel=Label(cartWindow,text=allQuantity)
    allQuantityLabel.grid(row=1,column=1)
    
    quantityLabel=Label(cartWindow,text="Price",font=("Arial",15,"bold"))
    quantityLabel.grid(row=0,column=2)
    allQuantityLabel=Label(cartWindow,text=allPrice)
    allQuantityLabel.grid(row=1,column=2)

def removeCart(item):
    global sum
    quantity=deleteClicked.get()
    deleteSum=quantity*items[item]
    for i in range(len(cartItems)):
        if(cartItems[i][0]==item):
            cartItems[i][1]-=quantity
            cartItems[i][2]-=deleteSum
    sum-=deleteSum
    print(sum)
    deleteWindow.destroy()
    deleteFunction()
    
def deleteItem(quantity,row,column,item):
    global deleteClicked
    deleteClicked=IntVar()
    deleteClicked.set(1)
    
    drop=OptionMenu(deleteWindow,deleteClicked,*range(1,quantity+1))
    drop.grid(row=row+1,column=column)
    deleteButton=Button(deleteWindow,text="Delete",command=lambda item=item:removeCart(item))
    deleteButton.grid(row=row+1,column=column+1)

    
def deleteFunction():
    global deleteWindow
    deleteWindow=Tk()
    deleteWindow.title("Delete items")
    deleteWindow.iconbitmap("C:\\Users\\gmadh\\Downloads\\cart_icon-icons.com_48341.ico")

    count=0
    row_count=0
    column_count=0
    for i in  range(len(cartItems)):
        if(column_count%18==0):
            column_count=0
            row_count+=2
        itemButton=Button(deleteWindow,text=cartItems[i][0]+"\n"+str(cartItems[i][2]),fg="#F0F8FF",background="#0066b2",height=2,width=12,padx=10,pady=10,command=lambda quantity=cartItems[i][1],item=cartItems[i][0],row=row_count,column=column_count:deleteItem(quantity,row,column,item))
        itemButton.grid(row=row_count,column=column_count,padx=10,pady=20,columnspan=3)
        column_count+=3
        count+=1
        
#  Created this function to get the final price of the cart
def submitButton():
    
    conn=sqlite3.connect("Shop.db")
    c=conn.cursor()

    

    conn.commit()
    c.close()
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
            allItems=""
            allQuantity=""
            allPrice=""
            totalPrice=""
            #If there are items in the cart this loop label them on the toplevel with their total
            for tupleCart in cartItems:
                allItems+=tupleCart[0]+"\n"
                allQuantity+=str(tupleCart[1])+"\n"
                allPrice+=str(items[tupleCart[0]])+"\n"
                totalPrice+=str(items[tupleCart[0]]*tupleCart[1])+"\n"
            allItemsLabel=Label(top,text=allItems,bg="#72A0C1")
            allItemsLabel.grid(row=1,column=0)
            ItemsLabel=Label(top,text="Items",font=("Arial",15,"bold"),bg="#72A0C1")
            ItemsLabel.grid(row=0,column=0)

            quantityLabel=Label(top,text="Quantity",font=("Arial",15,"bold"),bg="#72A0C1")
            quantityLabel.grid(row=0,column=1)
            allQuantityLabel=Label(top,text=allQuantity,bg="#72A0C1")
            allQuantityLabel.grid(row=1,column=1)
            
            quantityLabel=Label(top,text="Price",font=("Arial",15,"bold"),bg="#72A0C1")
            quantityLabel.grid(row=0,column=2)
            allQuantityLabel=Label(top,text=allPrice,bg="#72A0C1")
            allQuantityLabel.grid(row=1,column=2)
            
            totalPriceLabel=Label(top,text="Total Price",font=("Arial",15,"bold"),bg="#72A0C1")
            totalPriceLabel.grid(row=0,column=3)
            allTotalLabel=Label(top,text=totalPrice,bg="#72A0C1")
            allTotalLabel.grid(row=1,column=3)
            
            totalPriceLabel=Label(top,text="Total Bill",font=("Arial",15,"bold"),bg="#72A0C1")
            totalPriceLabel.grid(row=2,column=2)
            totalLabel=Label(top,text=sum,font=("Comic Sans MS", 25, "bold"),width=10,height=5,bd=5,bg="#72A0C1")
            totalLabel.grid(row=2,column=3)

# This function adds new item to the database
def addClicked():
    conn=sqlite3.connect("Shop.db")
    c=conn.cursor()

    
    c.execute("Insert into Inventory values(:ProductName,:Quantity,:Price)",
        {
            
        "ProductName":nameEntry.get(),"Quantity":quantityEntry.get(),"Price":priceEntry.get()
         }
    )
    # Query to access the table
    # c.execute("select * from inventory")
    # records=c.fetchall()
    # printRecords=""
    # for record in records:
    #     printRecords+=str(record[0])
    # print(printRecords)
    
    
    conn.commit()
    c.close()
    nameEntry.delete(0,END)
    quantityEntry.delete(0,END)
    priceEntry.delete(0,END)

# This is used to Show all the items present in Inventory
def Query():
    queryTop=Toplevel()
    conn=sqlite3.connect("Shop.db")
    c=conn.cursor()
    c.execute("select *,oid from inventory")
    records=c.fetchall()
    
    allName=""
    allQuantity=""
    allPrice=""
    allOid=""
    for record in records:
        allOid+=f"{str(record[3])}\n"
        allQuantity+=f"{str(record[1])}\n"
        allPrice+=f"{str(record[2])}\n"
        allName+=f"{str(record[0])}\n"
    allNameLabel=Label(queryTop,text=allName)
    allQuantityLabel=Label(queryTop,text=allQuantity)
    allPriceLabel=Label(queryTop,text=allPrice)
    allOidLabel=Label(queryTop,text=allOid)

    Label(queryTop,text="Oid\t".center(15),font=("Arial",15)).grid(row=0,column=1)
    Label(queryTop,text="Product Name\t".center(25),font=("Arial",15)).grid(row=0,column=2)
    Label(queryTop,text="Quantity\t",font=("Arial",15)).grid(row=0,column=3)
    Label(queryTop,text="Price\t".center(18),font=("Arial",15)).grid(row=0,column=4)
    allOidLabel.grid(row=1,column=1)
    allNameLabel.grid(row=1,column=2)
    allPriceLabel.grid(row=1,column=4)
    allQuantityLabel.grid(row=1,column=3) 
    conn.commit()
    c.close()

# This function adds items to the cart 
def add(item,row,column,quantity):
    global clicked,drop
    
    clicked=IntVar()
    clicked.set(1)
    
    global addButton
    # This creates a dropdown menu for the quantity
    drop=OptionMenu(bill,clicked,*range(1,quantity+1))
    drop.grid(row=row+1,column=column)
    addButton=Button(bill,text="Add",command=lambda:addCart(item,row,column))
    addButton.grid(row=row+1,column=column+1)


global cartItemsList
cartItemList=[]
def addCart(item,row,column):
    global sum
    global cartItems
    Quantity=clicked.get()
    price=items[item]
    if(item in cartItemList):
        for i in range(len(cartItems)):
            if(item in cartItems[i]):
                sum-=cartItems[i][1]*price
                sum+=price*Quantity
                cartItems.remove(cartItems[i])
                cartItems.append([item,Quantity,price])        
    else:        
        sum+=price*Quantity
        cartItemList.append(item)
        cartItems.append([item,Quantity,price*Quantity]) 
    addButton=Button(bill,text="Add",command=lambda:addCart(item),state=DISABLED)
    addButton.grid(row=row+1,column=column+1)
    print(sum)
    print(price*Quantity)
    
    
def billWindow():    
    root.destroy()
    global bill
    bill=Tk()
    bill.title("Create Bill")
    bill.iconbitmap("C:\\Users\\gmadh\\Downloads\\cart_icon-icons.com_48341.ico")
    global row_count, column_count
    row_count=0
    column_count=0
    conn=sqlite3.connect("Shop.db")
    c=conn.cursor()
    c.execute("select *,oid from inventory")
    records=c.fetchall()
    conn.commit()
    c.close()
    
    global items, itemList, itemPrice, itemQuantity
    itemList=[]
    itemPrice=[]
    itemQuantity=[]
    count=0

    items={}
    
    
    for record in records:
        if(column_count%18==0):
            column_count=0
            row_count+=2
        itemButton=Button(text=record[0],fg="#F0F8FF",background="#0066b2",height=2,width=12,padx=10,pady=10,font=("Comic Sans MS", 12, ),activebackground="green",command=lambda itemName=record[0],row=row_count,column=column_count,itemQuantity=record[1]:add(itemName,row,column,itemQuantity))
        itemButton.grid(row=row_count,column=column_count,padx=10,pady=20,columnspan=3)

        column_count+=3
        count+=1
        
        itemList+=record[0]
        itemPrice.append(record[2])    
        itemQuantity.append(record[1])
        
        items[record[0]]=record[2]
        

        
    # This button submit the cart to the final billing
    submit=Button(text="Submit",bg="green",bd=4,activebackground="#4F7942",command=submitButton)
    submit.grid(row=len(itemList),column=17,columnspan=3,padx=10,pady=10,ipadx=30,ipady=20)


    #This shows all the items present in the cart
    itemsInCart=Button(text="Show Cart",command=showCart,bd=4,background="#ec9d0d",activebackground="#b78f0d")
    itemsInCart.grid(row=len(itemList),column=9,columnspan=3,padx=10,pady=10,ipadx=30,ipady=20)


    delete=Button(text="Delete Item",command=deleteFunction,bd=4,background="#ba0f30",activebackground="#880808")
    delete.grid(row=len(itemList),column=0,columnspan=3,padx=10,pady=10,ipadx=30,ipady=20)

    
    
# This creates a new window to remove a item
def removeButton():
    top=Toplevel()
    global deleteEntry
    
    deleteLabel=Label(top,text="Enter Name of product")
    deleteLabel.grid(row=0,column=0)

    deleteEntry=Entry(top)
    deleteEntry.grid(row=0,column=1)
    remove=Button(top,text="Remove",command=removeClicked)
    remove.grid(row=1,column=1)

# This function removes data from the database
def removeClicked():
    conn=sqlite3.connect("Shop.db")
    c=conn.cursor()
    c.execute(f"Delete from Inventory WHERE oid={deleteEntry.get()}")


    conn.commit()
    c.close()
   
# This Function Creates a new window to add details about the new product
def addItems():
    top=Toplevel()
    global nameEntry,quantityEntry,priceEntry
    nameEntry=Entry(top)
    nameEntry.grid(row=1,column=1)
    quantityEntry=Entry(top)
    quantityEntry.grid(row=2,column=1)
    priceEntry=Entry(top)
    priceEntry.grid(row=3,column=1)

    nameLabel=Label(top,text="Enter Name")
    quantityLabel=Label(top,text="Enter Quantity")
    priceLabel=Label(top,text="Enter Price")
    nameLabel.grid(row=1,column=0)
    quantityLabel.grid(row=2,column=0)
    priceLabel.grid(row=3,column=0)
    
    # This Button adds items in the inventory
    addButton=Button(top,text="Add",command=addClicked)
    addButton.grid(row=4,column=1)
    
    nameEntry.delete(0,END)
    quantityEntry.delete(0,END)
    priceEntry.delete(0,END)
    
    
# This Button add items to the inventory
addItemsButton=Button(root,text="Add",font=("Arial",11),command=addItems)
addItemsButton.grid(row=0,column=0,padx=2)

# This Button remove items from the inventory
removeItemsButton=Button(text="remove",font=("Arial",11),command=removeButton)
removeItemsButton.grid(row=0,column=1,padx=2)

# This Button shows all items of the inventory
showItemsButton=Button(root,text="Show Stock",font=("Arial",11),command=Query)
showItemsButton.grid(row=0,column=3,padx=2)

buyButton=Button(root,text="Create Bill",font=("Arial",25),command=billWindow)
buyButton.grid(row=1,column=0,padx=2,pady=50,columnspan=5,ipadx=20)


updateButton=Button(root,text="Update",font=("Arial",11),command=edit)
updateButton.grid(row=0,column=4)


root.mainloop()