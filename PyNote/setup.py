#PyNotes_v1.0
#Made by Prathamesh Vijay Kulkarni
#important = Run this setup once before start to use PyNote !
#this is only required for once at first time.
#this script creates and populates the basic files required for PyNote


import pickle
import sys
import os

titles=[]
path="Data"
intro="PyNote_v1.0\nMade by Prathamesh Vijay Kulkarni"
try:
    os.mkdir(path)
except OSError:
    print("Failed")
else:
    print("Created")

aboutme=open("Data/Readme","wb")
setthis=pickle.dump(intro,aboutme)
aboutme.close()
titles.append('Readme')
    
setup=open("Data/titles","wb")
first=pickle.dump(titles,setup)
setup.close()

password='1234'
pw=open("Data/temp","wb")
setpw=pickle.dump(password,pw)
pw.close()
