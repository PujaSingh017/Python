                                            #My First Calculator#    

first=input("enter first number:")
operator=input("+,-,*,/,%")
second=input("enter second number:")
first=int(first)
second=int(second)

 # Operations Are Below:

if operator=="+":
    print(first+second)

elif operator=="-":
    print (first-second)

elif operator=="*" :
    print(first*second)

elif operator=="/":
    print(first)/(second)

elif operator=="%":
    print(first%second)


else:
     print("invaild operation")

# Done