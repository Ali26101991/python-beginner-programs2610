pin = input("Enter PIN: ")

if pin == "1234":
    balance = 1000
    withdraw = int(input("Enter required amount: "))

    if withdraw <= balance:
        balance -= withdraw
        print("Withdrawal successful")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid PIN")