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
            print("\nWelcome to the Savings calculator")
            age = (input("Please enter your current age (ex 19): "))
            annualSalary = (input("Enter your annual salary (ex 51,200 or 51200): "))
            percentSaved = (input("Enter the percentage that you are saving (ex 12): "))
            moneyNeeded = (input("Enter the total amount you want saved (ex 2,220,022 or 2220022): "))
            ageNeeded = retirementCalculator(age, annualSalary, percentSaved, moneyNeeded)
            if ageNeeded == -1:
                continue
            else:
                print("You will reach your savings goal at: ",ageNeeded)
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
    
    if pounds <= 0 or feet < 0 or inches < 0:
        print("Invalid input was provided. Please see examples when providing input")
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
def retirementCalculator(currentAge, annualSalary, percentSaved, moneyNeeded):
    #strip annualSalary and moneyNeeded if they have commas in them
    annualSalary = annualSalary.replace(',','')
    moneyNeeded = moneyNeeded.replace(',','')
    #validate input else return -1
    try:
        currentAge = int(currentAge)
        annualSalary = int(annualSalary)
        percentSaved = float(percentSaved)
        moneyNeeded = int(moneyNeeded)
    except Exception as ex:
        print("Invalid input was provided. Please see examples when providing input \n")
        return -1
    
    if currentAge < 0 or currentAge >= 100 or annualSalary < 0 or percentSaved < 0 or percentSaved > 100 or moneyNeeded < 0:
        print("Invalid input was provided. Please see examples when providing input \n")
        return -1

    #initalize savings
    savings = 0.00
    for i in range(currentAge,100):
        thisYearSavings = annualSalary * (percentSaved/100)
        #employer match
        employerMatch = thisYearSavings * (.35)
        thisYearSavings = thisYearSavings + employerMatch
        savings = savings + thisYearSavings
        if (savings >= moneyNeeded):
            return i
        
    print("You will not meet your savings goal before you die. \n")
    return -1







if __name__ == '__main__':
    menu()
