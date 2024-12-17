

while True:
    print("1.Add\n2.Subtract\n3.Exit")
    choice = int(input("Enter your choice: "))
    if choice >3:
        print("Enter a valid choice")
        

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    if choice == 1:
        print(num1+num2)
    elif choice == 2:
        
        print(num1-num2)
    elif choice == 3:
        break
    else:
        print("Enter a valid choice")