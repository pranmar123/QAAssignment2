def menu():
    print("Welcome to the BMI/Savings Program")
    entry = ""
    while (entry != "q"):
        print("Enter 1 for the BMI calculator")
        print("Enter 2 for the Savings calculator")
        print("Enter q to quit")
        entry = input("Input: ")
        if entry == "1":
            #call BMI handler
            pass
        elif entry == "2":
            #call savings handler
            pass
        elif entry == "q":
            break
        else:
            print("This is an invalid input, please try again... \n \n")
    print("Thank you for using the program! Exiting...")









if __name__ == '__main__':
    menu()
