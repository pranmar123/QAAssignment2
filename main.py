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
            height = input("Enter your height in feet,inches (ex 4,10): ")
            weight = input("Enter your weight in pounds (ex 180): ")
            print("\n \n")
            value, category = bmiCalculator(height,weight)
            if value == -1:
                continue
            else:
                print("Your BMI is: ",value,category)
                print("\n \n")
        elif entry == "2":
            print("Welcome to the Savings calculator")
            age = int(input("Please enter your current age: "))
            annualSalary = int(input("Enter your annual salary (without commas): $"))
            percentSaved = int(input("Enter the percentage that you are saving: "))
            moneyNeeded = int(input("Enter the total amount you want saved (without commas): "))
            print("\n \n")
            ageNeeded = retirementCalculator(age, annualSalary, percentSaved, moneyNeeded)
            
            print("\n \n")
        elif entry == "q":
            break
        else:
            print("This is an invalid input, please try again... \n \n")
    print("Thank you for using the program! Exiting...")


#take strings as input and return value as float and category as string
def bmiCalculator(height, weight):
    #validate input else return -1
    #break height input into a comma-separated list and convert the strings to ints
    heightList = height.split(",")
    try:
        feet = int(heightList[0])
        inches = int(heightList[1])
        pounds = int(weight)
    except Exception as ex:
        print("Invalid input was provided. Please see examples when providing input")
        print("\n \n")
        return -1,"-1"
    
    #convert lbs to kilos
    kilos = round((pounds * 0.45),2)

    #convert the feet to heights
    inches = inches + (feet * 12)

    #convert inches to meters
    meters = round((inches * 0.025),3)

    #square the meters 
    metersSquared = round((meters * meters),6)

    #calculate BMI
    bmiValue = round((kilos / metersSquared),1)

    #get category based on bmiValue
    if (bmiValue < 18.5):
        category = "Underweight"

    elif (18.5 <= bmiValue <= 24.9):
        category = "Normal weight"

    elif (25 <= bmiValue <= 29.9):
        category = "Overweight"

    elif (bmiValue >= 30):
        category = "Obese"

    return bmiValue, category


#Take age, annualSalary, percentSaved, moneyNeeded as strings and return age as int
def retirementCalculator(age, annualSalary, percentSaved, moneyNeeded):
    pass








if __name__ == '__main__':
    menu()
