#Dental Office Check-in Sheet

print("Hello, Welcome to Soft Dental & Orthodontics")

def info():
    print()
    print ("Your name is",name,"AND Your doctor is Dr.",docname.upper())
    print ("Thank you for checking in, we will call you in shortly.")
    print ("Please have a seat.")


firstname = input("Please enter your first name: ").strip()
lastname = input("Please enter your last name: ").strip()
name = str(firstname.upper()) + " " + str(lastname.upper())
docname = input("Please enter your doctor's name (Dr. Namian or Dr. Borjian): Dr. ")


info()
