def menu():
    print("Welcome to the BMI/Savings Program")
    entry = ""
    while (entry != "q"):
        print("Enter 1 for the BMI calculator")
        print("Enter 2 for the Savings calculator")
        print("Enter q to quit")
        entry = input("Input: ")
        if entry == "1":
            bmiHandler()
            print("\n \n")
        elif entry == "2":
            savingsHandler()
            print("\n \n")
        elif entry == "q":
            break
        else:
            print("This is an invalid input, please try again... \n \n")
    print("Thank you for using the program! Exiting...")

#this handler will deal with calling the bmi functions
def bmiHandler():
    print("Welcome to the")


#handler for dealing with the savings
def savingsHandler():
    print("Savings handler")








if __name__ == '__main__':
    menu()
