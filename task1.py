contacts={
    ("James",42)
    ("Amy",24)
    ("John",31)
    ("Amanda",63)
    ("Bob",18)
}

name=str(input("enter your name:"))
if name=="James":
    print(contacts["James"])

elif name=="Amy":
    print(contacts["Amy"]) 

elif  name=="John":
    print(contacts["John"])

elif   name=="Amanda":
    print(contacts["Amanda"])

elif  name=="Bob":
    print(contacts["Bob"])

else:
    print("not found")
    
