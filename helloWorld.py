#This program says hello, asks for my name and password.

print ("Hello!")
print ("What is you name?")
myName = input()

if myName == 'Dale':
    print ("Welcome back, " + myName + ".")
    print ("What is your password? ")
    myPassword = input()
    if myPassword == "riskybusiness":
        print("Access granted.")
    else:
        print("Wrong password. Bye stranger!")
else:
    print("Hello, stranger")

