def menu():
    print("Welcome to the BMI/Retirement Calculators")
    entry = ""
    while (entry != "q"):
        print("Enter 1 for the BMI calculator")
        print("Enter 2 for the Retirement calculator")
        print("Enter q to quit")
        entry = input("Input: ")
        if entry == "1":
            print("Welcome to the BMI calculator")
            height = input("Enter your height in feet with a space then inches: (ex 4 10)")
            weight = input("Enter your weight in pounds: ")
            value, category = bmiCalculator(height,weight)
            print("Your BMI is: ",value,category)
            print("\n \n")
        elif entry == "2":
            print("Welcome to the Savings calculator")
            age = int(input("Please enter your current age: "))
            annualSalary = int(input("Enter your annual salary (without commas): $"))
            percentSaved = int(input("Enter the percentage that you are saving: "))
            moneyNeeded = int(input("Enter the total amount you want saved (without commas): "))
            ageNeeded = retirementCalculator(age, annualSalary, percentSaved, moneyNeeded)
            
            print("\n \n")
        elif entry == "q":
            break
        else:
            print("This is an invalid input, please try again... \n \n")
    print("Thank you for using the program! Exiting...")


#take strings as input and return value as float and category as string
def bmiCalculator(height, weight):
    return 22.7, "Normal weight"


#Take age, annualSalary, percentSaved, moneyNeeded as strings and return age as int
def retirementCalculator(age, annualSalary, percentSaved, moneyNeeded):
    pass








if __name__ == '__main__':
    menu()
