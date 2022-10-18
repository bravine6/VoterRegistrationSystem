print("***************************************************************")
print("Welcome to the Python Voter Registration Application.")
# Start of infinite loop
while 1:
    # Asking the user if they want to continue.
    choice = input("Do you want to continue with Voter Registration?\n").lower()
    # If the user enters yes.
    if choice == "yes":
        # Ask for user's first name.
        fName = input("What is your first name?\n")
    # if the user does not want to continue with the program.
    else:
        break
    # Ask the user if they want to continue.
    choice = input("Do you want to continue with Voter Registration?\n").lower()
    # If the user enters yes
    if choice == "yes":
        # Ask for the user's last name.
        lname = input("What is your last name?\n")
    # If the user does not want to continue with the program.
    else:
        break
    # Asking the user if they want to continue.
    choice = input("Do you want to continue with Voter Registration?\n").lower()
    # If the user enters yes
    if choice == "yes":
        # Validating age. Should be between 18 and 120
        while 1:
            try:
                age = int(input("What is your age?\n"))
                if 18 < age < 120:
                    break
                    # if user entered invalid age print,
                else:
                    print("Age should be above 18 years and below 120 years")
            # If there is any exception continue and ask again
            except:
                continue
    # If the user don't want to continue exit from the program
    else:
        break
    # Ask if the user wants to continue
    choice = input("Do you want to continue with Voter Registration?\n").lower()
    # If the user enters yes in the requirement
    if choice == "yes":
        # Ask for citizenship
        citizen = input("Are you a U.S Citizen?\n")
        # If the user does not want to continue exit the program
    else:
        break
    # Ask if the user wants to continue
    choice = input("Do you want to continue with the Voter Registration?\n").lower()
    # If the user entered yes ask the requirement
    # Check the state entered by user contains two letters
    if choice == "yes":
        while 1:
            try:
                usState = input("What state do you live in?\n")
                if len(usState) == 2:
                    break
                else:
                    print("Please enter the two letters of your state\n")
            except:
                continue
    else:
        break
    # Asking if the user wants to continue
    choice = input("Do you want to continue with Voter Registration?\n").lower()
    # If the user entered yes ask the following requirement
    if choice == "yes":
        # Ask for the Zip code
        zipCode = input("What is your zipcode?\n")
        # Print the details provided
        print("\nThank you for registering to vote. Here is the information that was received.")
        print("Name (FirstName LastName): {} {}".format(fName, lname))
        print("Your Age: {}".format(age))
        print("U.S. Citizen: {}".format(citizen))
        print("State: {}".format(usState))
        print("Zipcode: {}".format(zipCode))
        print("Thanks for trying the Voter Registration Application.\
        Your voter registration card should be shipped within 3 weeks.")
        print("***********************")
    # Break the infinite loop
    # if the user doesn't want to continue, exit the program
    else:
        break
    break
