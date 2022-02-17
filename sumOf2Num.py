#sum_intro of def,color
import sys
from tkinter.font import BOLD, ITALIC
from termcolor import colored,cprint

def asn(a,b):
    s=a+b
    print("sum is",+s)
   

while(True):
    info2=lambda x: cprint(x,'red')
    cprint("\n\t\tSUM",'cyan', attrs=[BOLD])
    info2("ENTER '-0' AS BOTH INPUT TO EXIT")
    x=int(input("enter the 1st num:"))
    y=int(input("enter the 2nd num:"))
    if x==-0 and y==-0:
        cprint("SUCCESSFULLY TERMINATED\n",'green')
        exit()
    else:
        asn(x,y)