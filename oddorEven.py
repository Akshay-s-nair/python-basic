def OddorEven(a):
	if a==0:
		exit()
	else:
		if a%2==0:
			print("it is an EVEN number\n")
		else:
			print("it is an ODD number\n")
while True:
 print("-------------------\n""|   ODD or EVEN   |","\n-------------------")
 print("(ENTER '0' TO EXIT)")
 a=int(input("enter the number: "))
 OddorEven(a)

