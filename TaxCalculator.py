#basic Income tax calculator
#program by Prathamesh Vijay Kulkarni

import sys
import time
from decimal import Decimal

hour=time.strftime("%D\n%H:%M\n")
print("Welcome to Income Tax Calculator !\n")

def logbook1(): #logbook entry function for slab 2 income
    log.write("\n\nYou are eligible for "+str(slab2)+
              "% tax of your income !\n\nTax = $"+str(tax)+
              "\n\n+Health Education Cess = $"+str(hec)+
              "\n\nTax Liability : $"+str(totaltax))
    log.close()
    
def logbook2(): #logbook entry function for slab 3 income
    log.write("\n\nYou are eligible for "+str(slab3)+
              "% tax of your income !\n\nTax = $"+str(tax)+
              "\n\n+Health Education Cess = $"+str(hec)+
              "\n\nTax Liability : $"+str(totaltax))
    log.close()
    
def logbook3(): #logbook entry function for slab 4 income
    log.write("\n\nYou are eligible for "+str(slab4)+
              "% tax of your income !\n\nTax = $"+str(tax)+
              "\n\n+Surcharge = $"+str(surcharge)+
              "\n\n+Health Education Cess = $"+str(hec)+
              "\n\nTax Liability : $"+str(taxlb))
    log.close()
       
def main():
    name=input("Enter your name : ")
    global log,slab2,slab3,slab4,amount,tax,surcharge,hec,totaltax,taxlb
    log=open(name+".txt","a+") #creates a file for bill-type log
    log.write("\n\n"+hour+"\nName : "+name)
    print("Enter total amount of your income : ")
    amount=float(input())
    log.write("\n\nTotal income amount : $"+str(amount)) 
    slab2=5     # tax rate % slabs
    slab3=20    # for different levels of
    slab4=30    # income
    if amount>0 and amount<=250000:
        print("Tax : NILL")
        log.write("\n\nTax : NILL")
        log.close()
        keep()
    elif amount>250000 and amount<=500000:
        newamount=amount-250000
        tax=(newamount*slab2)/100
        hec=(tax*4)/100
        totaltax=tax+hec
        tax=Decimal(tax).quantize(Decimal('.01'))           # quantize the money
        hec=Decimal(hec).quantize(Decimal('.01'))           # upto 2 decimal points
        totaltax=Decimal(totaltax).quantize(Decimal('.01')) ##
        print("You are eligible for ",slab2,"% tax !\nTax = ",tax,"\n+Health Education Cess = ",hec,"\nTax Liability : ",totaltax)
        logbook1()
        keep()
    elif amount>500000 and amount<=1000000:
        newamount=amount-500000
        tax=12500+(newamount*slab3)/100
        hec=(tax*4)/100
        totaltax=tax+hec
        tax=Decimal(tax).quantize(Decimal('.01'))
        hec=Decimal(hec).quantize(Decimal('.01'))
        totaltax=Decimal(totaltax).quantize(Decimal('.01'))
        print("You are eligible for ",slab3,"% tax !\nTax : ",tax,"\n+Health Education Cess = ",hec,"\nTotal Liability : ",totaltax)
        logbook2()
        keep()
    elif amount>1000000 and amount<=5000000:
        newamount=amount-1000000
        tax=112500+(newamount*slab4)/100
        hec=(tax*4)/100
        totaltax=tax+hec
        tax=Decimal(tax).quantize(Decimal('.01'))
        hec=Decimal(hec).quantize(Decimal('.01'))
        totaltax=Decimal(totaltax).quantize(Decimal('.01'))
        print("You are eligible for ",slab4,"% tax !\nTax : ",tax,"\n+Health Education Cess = ",hec,"\nTotal Liability : ",totaltax)
        logbook2()
        keep()
    elif amount>5000000 and amount<=10000000:
        newamount=amount-1000000
        tax=112500+(newamount*slab4)/100
        surcharge=(tax*10)/100
        totaltax=tax+surcharge
        hec=(totaltax*4)/100
        taxlb=totaltax+hec
        tax=Decimal(tax).quantize(Decimal('.01'))
        surcharge=Decimal(surcharge).quantize(Decimal('.01'))
        totaltax=Decimal(totaltax).quantize(Decimal('.01'))
        hec=Decimal(hec).quantize(Decimal('.01'))
        taxlb=Decimal(taxlb).quantize(Decimal('.01'))
        print("You are eligible for ",slab4,"% tax !\nTax = ",tax,"\n+Surcharge = ",surcharge,"\n+Health Education Cess = ",hec,"\nTotal Liability : ",taxlb)
        logbook3()
        keep()
    elif amount>10000000 and amount<=20000000:
        newamount=amount-1000000
        tax=112500+(newamount*slab4)/100
        surcharge=(tax*15)/100
        totaltax=tax+surcharge
        hec=(totaltax*4)/100
        taxlb=totaltax+hec
        tax=Decimal(tax).quantize(Decimal('.01'))
        surcharge=Decimal(surcharge).quantize(Decimal('.01'))
        totaltax=Decimal(totaltax).quantize(Decimal('.01'))
        hec=Decimal(hec).quantize(Decimal('.01'))
        taxlb=Decimal(taxlb).quantize(Decimal('.01'))
        print("You are eligible for ",slab4,"% tax !\nTax = ",tax,"\n+Surcharge = ",surcharge,"\n+Health Education Cess = ",hec,"\nTotal Liability : ",taxlb)
        logbook3()
        keep()
    elif amount>20000000 and amount<=50000000:
        newamount=amount-1000000
        tax=112500+(newamount*slab4)/100
        surcharge=(tax*25)/100
        totaltax=tax+surcharge
        hec=(totaltax*4)/100
        taxlb=totaltax+hec
        tax=Decimal(tax).quantize(Decimal('.01'))
        surcharge=Decimal(surcharge).quantize(Decimal('.01'))
        totaltax=Decimal(totaltax).quantize(Decimal('.01'))
        hec=Decimal(hec).quantize(Decimal('.01'))
        taxlb=Decimal(taxlb).quantize(Decimal('.01'))
        print("You are eligible for ",slab4,"% tax !\nTax = ",tax,"\n+Surcharge = ",surcharge,"\n+Health Education Cess = ",hec,"\nTotal Liability : ",taxlb)
        logbook3()
        keep()
    elif amount>=50000000:
        newamount=amount-1000000
        tax=112500+(newamount*slab4)/100
        surcharge=(tax*37)/100
        totaltax=tax+surcharge
        hec=(totaltax*4)/100
        taxlb=totaltax+hec
        tax=Decimal(tax).quantize(Decimal('.01'))
        surcharge=Decimal(surcharge).quantize(Decimal('.01'))
        totaltax=Decimal(totaltax).quantize(Decimal('.01'))
        hec=Decimal(hec).quantize(Decimal('.01'))
        taxlb=Decimal(taxlb).quantize(Decimal('.01'))
        print("You are eligible for ",slab4,"% tax !\nTax = ",tax,"\n+Surcharge = ",surcharge,"\n+Health Education Cess = ",hec,"\nTotal Liability : ",taxlb)
        logbook3()
        keep()
    elif amount==0:
        print("You don't need to worry about tax..!")
        log.write("You don't need to worry about tax..!")
        log.close()
        keep()

def keep():
    a=input("Continue ? (y/n) : ")
    if a=='y':
        return main()
    else:
        return sys.exit()

if __name__=='__main__':
    main()
