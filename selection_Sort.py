from tkinter.font import BOLD
from termcolor import cprint,colored
def sort(lst,s,n):
    for i in range(0,s-1):
        minPos=i
        for j in range(i,n):
            if lst[j]<lst[minPos]:
                minPos=j
        temp=lst[i]
        lst[i]=lst[minPos]
        lst[minPos]=temp
while(True):
    cprint('_____SELECTION SORT_____','cyan',attrs=[BOLD])
    lst=[]
    cprint('(enter 0 to exit)','red')
    s=int(input('enter the limit of list:'))
    if(s!=0): 
        cprint("enter the elements",'yellow')
        n=0
        for i in range(0,s):
            ele=int(input())
            lst.append(ele)
            n=n+1
        cprint('the given list is:','red',attrs=[BOLD])
        cprint(lst,'red')
        sort(lst,s,n)
        cprint('\nThe sorted list is:','green',attrs=[BOLD])
        cprint(lst,'green')
        print()
    else:
        cprint('~TERMINATED~','green')
        exit()