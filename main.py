from flask import render_template, url_for, redirect, request, abort, Flask, session
from processes import bmiCalculator, category, retirementCalculator

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def home():
    return render_template('home.html')

@app.route('/retire', methods=["POST","GET"])
def retire():
    
    if request.method == "POST":
        age = request.form["age"]
        annualSalary = request.form["annualSalary"]
        percentSaved = request.form["percentSaved"]
        moneyNeeded = request.form["moneyNeeded"]
        ageNeeded = retirementCalculator(age, annualSalary, percentSaved, moneyNeeded)
        if ageNeeded == -1:
            return render_template('retire.html')
        else:
            return redirect(url_for("r_results", res=ageNeeded))
    else:
        return render_template('retire.html')

@app.route('/<res>')
def r_results(res):
    return f"<h1>You will reach your savings goal at: {res} </h1>" + """  <p><a href="/"> Click here to go to menu</a> """

@app.route("/bmi", methods={"POST", "GET"})
def bmi():
    if request.method == "POST":
        hFeet = request.form["hFeet"]
        hInches = request.form["hInches"]
        pounds = request.form["pounds"]
        result = bmiCalculator(hFeet,hInches,pounds)
        if result == -1:
            return render_template('bmi.html')
        else:
            catg = category(result)  
            return redirect(url_for("bmi_results", res=result, cat = catg))
    else:
        return render_template('bmi.html')  
    
@app.route('/<res>,<cat>')
def bmi_results(res,cat):
    return f"<h1>Your BMI is {res} and your category is {cat} </h1>" + """  <p><a href="/"> Click here to go to menu</a> """ 

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)