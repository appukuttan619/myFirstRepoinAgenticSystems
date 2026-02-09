balance = int(input("Enter the bank balance"))
withdraw_amount = int(input("Enter the balance which you want to withdraw"))
is_verified  = True if input("Do you have id ") == "True" else False
if balance >= withdraw_amount and is_verified:
    print("Withdrawal successful")
else:
    print("Transaction denied")