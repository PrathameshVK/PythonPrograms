#Caffe Billing v1.0
#By Prathamesh Vijay Kulkarni

import sys
import time
import pandas as pd
import pickle

menu={}
getdata=open("caffemenu","rb") ###
menu=pickle.load(getdata)      #loads the menu data from file
getdata.close()                ###
print("================================================================================")                  
print("Welcome to Caffe Manager\n")
print(time.strftime("%D"))


global get
def bill():
    total={} #to store item names and prices for final bill
    checkbill=[] #to add and store item names in bill
    checkprice=[] #to get price for an item from main menu database
    columns=['Item Name','Item Price'] 
    itemno=int(input("Enter the number of items : "))
    print("Enter item names : ")
    for i in range(itemno):
        items=str(input()) #Takes the item names
        if items not in menu:
            print("Not available")
            itemno-=1
        else:
            checkbill.append(items) #adds items in temporary list named checkbill
    for item in checkbill: #for every item in checkbill list
        price=menu[item] #takes prices for entered items from prices dictionary
        checkprice.append(price) #adds prices into temporary checkprice list
        total.update({str(item):int(price)}) #adds both item names and its price into temporary dictionary named as total
    show=pd.DataFrame(total,index=['Prices'])
    print("================================================================================")
    print(show.T)
    print("Total Items : "+str(itemno)+"\nTotal amount : $"+str(sum(checkprice)))
    print("================================================================================")
    return main()

def check(): #Function for menu list
    show=pd.DataFrame(menu,index=['Price $'])
    print("================================================================================")                  
    print("Menu")
    print("================================================================================")                  

    print(show.T)
    return main()
    
def checkifpresent(unit,get):
    if unit in menu: #checks if item is already present in menu database
        error=str(input("\nItem is already present in the menu !\nDo you want to edit the existing item ? (y/n) :"))
        if error=='y':
            return newprice() #go to set new price
        else:
            print("Please enter the different item !")
            
    else:
        pass
    
def newitem(get):
    unit=str(input("Enter item name : "))
    checkifpresent(unit,get)
    price=float(input("Enter item price : "))
    menu.update({unit:price})
            
def newprice():
    item=str(input("Enter the name of the item to change the price : "))
    if item in menu:
        price=float(input("Enter the new price : "))
        menu[item]=price
        print("Price is changed successfully !")
        edit()
    else:
        print("There is no such item in menu !")
        newprice()
    
def edit():
    print("================================================================================")
    print("Edit Menu")
    print("================================================================================")
    print("1.Add items\n2.Remove items\n3.Change price\n4.Main menu\nEnter your choice : ")
    get=str(input())
    if get=='1':
        items=int(input("Enter the number of items you want to add : "))
        for i in range(0,items):
            newitem(get)
        print("All items are added successfully !")
        edit()
        
    if get=='2':
        show=pd.Series(menu)      #loads the current
        print(show)               # menu 
        item=str(input("Enter the name of the item you want to remove : "))
        if item in menu: #if item is present in menu
            del menu[item] #delete the item
            new=pd.Series(menu) #update list
            print(new) #show updated list
            getout=open("caffemenu","wb") ###
            pickle.dump(menu,getout)      #Updates the menu data from database file
            getout.close()                ###
            edit()
        else:
            print("No such item in the menu !")
        edit()
        
    if get=='3':
        newprice()
        edit()
            
    if get=='4':
        return main()
    
def keep():
    print("================================================================================")
    decide=str(input("Confirm exit ? (y/n) : "))
    if decide=='y':
        print("================================================================================")
        sys.exit()
    else:
        print("================================================================================")
        return main()
    
def main():
    print("================================================================================")
    print("Main Menu         ",time.strftime("%H:%M"))
    print("================================================================================")
    choice=str(input("1.Create the bill\n2.Check the menu\n3.Edit menu\n4.Exit\nEnter your choice : "))
    if choice=='1':
        bill()
        
    elif choice=='2':
        check()
        
    elif choice=='3':
        edit()

    elif choice=='4':
        keep()

    else:
        print("Enter correct choice !")
        main()

if __name__=='__main__':
    main()
