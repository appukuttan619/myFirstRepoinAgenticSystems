age = int(input("Please enter your nage:"))
has_id = True if input("Do you have id ") == "True" else False
if age>=18 and has_id: 
    print("Entry allowed")
else:
    print("Entry not allowed")