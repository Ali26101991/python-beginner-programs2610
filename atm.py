balance=1000
withdraw=int(input("enter required amount :"))
if withdraw<=balance:
    balance -= withdraw
    print("withdrawl is successfull")
    print("Remaining balance is ",balance)

else:
    print("insufficient balance")