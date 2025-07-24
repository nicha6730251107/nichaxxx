# Complete this ATM simulation
balance = 1000
pin = "1234"
 
entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
       
        choice = input("Choose option: ")
       
        # Complete the menu logic here
        # Your code here:
        if choice == "4":
            print("Thank you to use our ATM")
            break
 
        if choice == "1":
            print("Now, you have : ", balance)
 
        if choice == "2":
            Withdraw = float (input("Withdraw amount: "))
            balance = balance - Withdraw
            print("Now, you have : ", balance)
 
        if choice == "3":
                depsit = float(input("Depsit amount: "))
                balance = balance + depsit
                print("Now, you have : ", balance)    
       
else:
    print("Invalid PIN")