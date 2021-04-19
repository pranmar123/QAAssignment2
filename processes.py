def bmiCalculator(heightFeet, heightInch, weight):
    try:
        feet = int(heightFeet)
        inches = int(heightInch)
        pounds = int(weight)
    except Exception as ex:
        print("Invalid input was provided. Please see examples when providing input")
        print("\n \n")
        return -1
    
    if pounds <= 0 or feet < 0 or inches < 0:
        print("Invalid input was provided. Please see examples when providing input")
        return -1
    
    heightFeet = float(heightFeet)
    heightInch = float(heightInch)
    weight = float(weight)
    kilos = weight * 0.45
    hInch = heightInch + (heightFeet * 12)
    hInch = hInch * 0.025
    BMI = (kilos/ (hInch * hInch))
    BMI = round(BMI, 1)
    return BMI

def category(bmiValue):
    #get category based on bmiValue
    if ( 0 <= bmiValue < 18.5 ):
        category = "Underweight"

    elif (18.5 <= bmiValue <= 24.9):
        category = "Normal weight"

    elif (25 <= bmiValue <= 29.9):
        category = "Overweight"

    elif (bmiValue >= 30):
        category = "Obese"

    elif (bmiValue == -1):
        category = "-1"

    

    return category

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