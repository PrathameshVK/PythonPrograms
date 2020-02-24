#PyNotes_v1.0
#Made by Prathamesh Vijay Kulkarni


import pickle
import time
import sys
import os
from pandas import DataFrame as df

date=time.strftime("%D")
datentime=time.strftime("%D\n%H:%M")
titles=[] ##########################list to contain the title names of previous articles
gettitles=open("Data/titles","rb") #title names are stored in this binary file
titles=pickle.load(gettitles) ######titles names from file are pickled into current list
gettitles.close()

print("Welcome       "+date)


def new():
    print("================================================================================")                  
    title=str(input("Enter the title for new entry : "))
    if title in titles: #if the title name is already present in titles list i.e. if the same name is used previously
        print("That tile name already exists ! Please enter a new title name !\n")
        print("================================================================================")             
        new()
    else:
        titles.append(title) ###############
        settitle=open("Data/titles","wb")###new title name is appended in the titles list and also stored in binary file of titles
        pickle.dump(titles,settitle)########
        settitle.close()
        temp=open("Data/stp","w") #this is for the workaround method to store the entry data
        print("You may now write your entry\nPress ENTER twice to stop writing !\n")
        print("================================================================================")             
        while True:
            getentry=input()
            if getentry:
                temp.write(getentry) #new data is first written in temp file
                temp.write("\n") 
            else:
                temp.close()
                break
        temp=open("Data/stp","r") #temporary data is loaded
        save=temp.read()
        temp.close()
        newentry=open("Data/"+title,"wb") #new file is created with given title name
        pickle.dump(datentime,newentry) ###and the data stored in temporary file is dumped
        pickle.dump(save,newentry) ########in this actual file
        newentry.close()
        print("================================================================================")                  
        cont=str(input("Entry is added successfully !\nEnter C to create new entry\nEnter M to go to main menu\nEnter E to exit\n"))
        if cont=='c' or cont=='C':
            new()
        elif cont=='m' or cont=='M':
            mainmenu()
        elif cont=='e' or cont=='E':
            confirm()
    
    
def view():
    print("================================================================================")                  
    #print(str(titles)) #prints the list of available titles to read
    new=df(titles,columns=['Titles'])
    print(new)
    title=str(input("Enter the title of entry you want to view : "))
    if title in titles: ###################if the title name is present in the titles list
        gettitle=open("Data/"+title,"rb") #then use the name to open the file of that title name
        print("================================================================================")                  
        try:
            while True: #################### unpickling will unpickle one object ate a time
                read=pickle.load(gettitle) # so, use it while there are objects in the file
                print(read) ################ and print them
        except EOFError: ################### when the objects are over, this error will be thrown
            pass
        gettitle.close()
        print("================================================================================")                  
        cont()
        
    else:
        print("That entry doesn't exist !") 
        mainmenu()

def delent():
    print("================================================================================")                  
    new=df(titles,columns=['Titles'])
    print(new)
    getname=str(input("Enter the title of entry that you want to delete or C to cancel : ")) #get the name of the title you want to delete
    if getname=='c' or getname=='C':
        mainmenu()
    else:
        pass
    if getname in titles: # if that name exists in the titles list i.e. checks if there is a previous entry of that name
        conf=str(input("Confirm delete ? (y/n) : "))
        if conf=='y' or conf=='Y':
            try:
                os.remove("Data/"+getname) #remove the file of that name
            except OSError: #if the is no file i.e. file is moved or deleted while out of program, this error will be thrown
                print("No such file !")
            else:
                print("Entry deleted successfully !")
                titles.remove(getname) #remove the same name from titles list
                settitles=open("Data/titles","wb") #
                pickle.dump(titles,settitles) ######update the titles data from binary file
                settitles.close() ##################
                menu=input("Press any key to go back")
                mainmenu()
        else:
            delent()
    else:
        print("That entry doesn't exist !") 
        delent()
    
def changepw():
    getpass=open("Data/temp","rb") #get the original password from temp binary file
    password=pickle.load(getpass) ####
    getpass.close() 
    print("================================================================================")                  
    old=str(input("Enter your old password : "))
    if old==password: #if the current password is correct match,
        new=str(input("Enter your new password : ")) #ask for new password
        setpass=open("Data/temp","wb") ## and save the new password
        newpass=pickle.dump(new,setpass)# in the temp file
        setpass.close()
        print("Password changed successfully !\nYour new password is => "+new)
        mainmenu()

    else:
        print("That's not a correct password !")
        again=str(input("Enter A to try again or enter M to return to main menu :\n"))
        if again=='a' or again=='A':
            changepw()
        else:
            mainmenu()
        
def cont():
    opt=str(input("Enter M to return to main menu\nEnter V to view another entry\nEnter E to exit :\n"))
    if opt=='m' or opt=='M':
        mainmenu()
    elif opt=='v' or opt=='V':
        view()
    elif opt=='e' or opt=='E':
        confirm()

    
def confirm():
    opt=str(input("Confirm exit ? (y/n) : "))
    if opt=='y':
        print("================================================================================")                  
        sys.exit()
    else:
        print("Returning to main menu..")
        print("================================================================================")                  
        mainmenu()
        
def mainmenu():
    print("================================================================================")                  
    print("Main Menu")
    print("================================================================================")                  
    option=str(input("1.New Entry\n2.View previous entries\n3.Delete entries\n4.Change password\n5.Exit\nEnter your choice : "))

    if option=='1':
        new()

    elif option=='2':
        view()
        
    elif option=='3':
        delent()
        
    elif option=='4':
        changepw()

    elif option=='5':
        confirm()

    else:
        print("Please enter correct choice number !")
        mainmenu()
        
def main():
    getpass=open("Data/temp","rb") #this loads the password string
    password=pickle.load(getpass) ##from the binary file
    getpass.close() 
    print("================================================================================")                  
    print("Enter password : ")
    getpassword=str(input())

    if getpassword==password: #checks if the entered string matches with string loaded from binary file
        mainmenu()
    else:
        print("================================================================================")                  
        print("Wrong Password !")
        main()

if __name__=="__main__":
    main()
