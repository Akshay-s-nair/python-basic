from tkinter.font import BOLD
from termcolor import colored,cprint 
def signup(h):
    f=open('logfile.txt','a')
    f.write(h+'\n')
    f.close()
    cprint('\tsigned up successfully...','cyan')

def login(h):
    f=open('logfile.txt','r')
    f.seek(0)
    if h in f.read():
        cprint('\tlogged in','green')
    else:
        cprint('\tNo Data found! please signup...!','red')
    f.close()

def view():
    f=open('logfile.txt','r')
    f.seek(0)
    pass1=2001
    pass2=int(input('Enter the password to view the content:'))
    if pass1==pass2:
        cprint('\tACCESS GRANTED..','cyan')
        cprint('\tEMAIL\t   PASSWORD','yellow')
        for i in f.readlines():
            cprint('\t'+i,'green')
    else:
        cprint('ACCESS DENIED..WRONG PASSWORD!','red')

def deleter():
    temp=0
    pass1=2001
    pass2=int(input('Enter the password to delete the content:'))    
    if pass1==pass2:
        cprint('\tACCESS GRANTED..','cyan')        
        c=input("\nEnter the given email:")
        h=input("Enter the given  password:")
        ch=c+' '+h
        with open('logfile.txt','r') as f:
            lines=f.readlines()
        with open('logfile.txt','w') as f:
            for line in lines:
                if line.strip()!=ch:
                    f.write(line)
                elif line.strip()==ch:
                    cprint('DELETED SUCCESSFULLY...','green')
                    temp=1
        f.close()
        if temp==0:
            cprint('No such data found in record!','red')        
    else:
        cprint('ACCESS DENIED..WRONG PASSWORD','red')


while(True):
    cprint('\n\n\t__________________\n________|login interface |________\n\t|________________|','cyan',attrs=[BOLD])
    cprint("1 to signup\n2 to login\n3 to view records\n4 to delete record\n0 to exit",'yellow')
    ch=int(input('choice: '))
    if(ch==1):
        e=input('\nEnter your email: ')
        m=input('Enter your password: ')
        em=e+' '+m
        signup(em)
    elif(ch==2):
        c=input("\nEnter the given email:")
        h=input("Enter the given  password:")
        ch=c+' '+h
        login(ch)
    elif(ch==3):
        view()
    elif ch==4:
      deleter()
    elif ch==0:
        cprint('TERMINATED.......\n','red',attrs=[BOLD])
        exit()
    else:
        cprint('\tENTER A VALIED CHOICE!','red')