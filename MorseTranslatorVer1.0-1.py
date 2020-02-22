import sys
import time
import datetime

today=datetime.date.today()
hour=time.strftime("%D\n%H:%M\n")

intro="Welcome to Morse Translator\n"
print("================================================================================")
for letter in intro:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.1)
print("================================================================================")                  
print("================================================================================")

#morse code dictionary
morse_dict={'A':'.-', 'B':'-...', 

                    'C':'-.-.', 'D':'-..', 'E':'.', 

                    'F':'..-.', 'G':'--.', 'H':'....', 

                    'I':'..', 'J':'.---', 'K':'-.-', 

                    'L':'.-..', 'M':'--', 'N':'-.', 

                    'O':'---', 'P':'.--.', 'Q':'--.-', 

                    'R':'.-.', 'S':'...', 'T':'-', 

                    'U':'..-', 'V':'...-', 'W':'.--', 

                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 

                    '1':'.----', '2':'..---', '3':'...--', 

                    '4':'....-', '5':'.....', '6':'-....', 

                    '7':'--...', '8':'---..', '9':'----.', 

                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 

                    '?':'..--..', '/':'-..-.', '-':'-....-', 

                    '(':'-.--.', ')':'-.--.-'}

#function to convert the string according to morse code dictionary
def encrypt(message):
    cipher=''
    for letter in message:
        if letter != ' ':
            cipher += morse_dict[letter]+' '
        else:
            cipher += ' '
    return cipher

def encode():
    message=input("Enter the message to encode :\n")
    result=encrypt(message.upper())
    print("\nEncoded message is as follows :\n")
    for letter in result:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.1)
    print("\n")
    log=open("log","a+")
    log.write("================================================================================\n"
              +hour+"\n"+message+"\n"+result+
              "\n================================================================================")
    log.close()
    keep()

#function to convert the morse code in english string using morse dictionary
def decrypt(message):
    decipher=''
    message += ' '
    citext=''
    for letter in message:
        if letter!=' ':
            i=0
            citext += letter
        else:
            i+=1
            if i==2:
                decipher+=' '
            else:
                decipher+=list(morse_dict.keys())[list(morse_dict.values()).index(citext)]
                citext=''
    return decipher

def decode():
    message=input("Enter the morse code to decode :\n")
    result=decrypt(message)
    print("\nDecoded message is as follows :\n")
    for letter in result:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.1)
    print("\n")
    log=open("log","a+")
    log.write("================================================================================\n"
              +hour+"\n"+message+"\n"+result+
              "\n================================================================================")
    log.close()
    keep()

def check():
    log=open("log","r")
    showlog=log.read()
    print("\n",showlog)
    log.close()
    keep()

def keep():
    answer=input("Continue ? (y/n) :")
    if answer=='y':
        print("\n================================================================================\n")
        return main()
    else:
        print("================================================================================")
        return sys.exit()

def main():
    choice=input("1.Encode the message into morse code\n2.Decode the message from morse code\n3.View Log\n4.About\n5.Exit\nEnter your choice :")
    if choice=='1':
        encode()
    elif choice=='2':
        decode()
    elif choice=='3':
        check()
    elif choice=='4':
        print("Morse Translator v1.0\nMade by Prathamesh Vijay Kulkarni\nprathameshkulkarni55@gmail.com")
    elif choice=='5':
        print("================================================================================")
        print("Log has been updated successfully")
        print("================================================================================")
        sys.exit()
    else:
        print("Enter correct choice !")

if __name__=='__main__':
    main()
    keep()
