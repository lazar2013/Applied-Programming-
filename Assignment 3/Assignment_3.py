#BMI Calculator

# Ask the user for their name, weight, height in feet, and remaining height in inches.
name = input("Enter your name:")
weight_lbs = int(input("Enter your weight in pounds:"))
height_ft = int(input("Enter your height in feet:"))
height_in = float(input("Enter your remaining height in inches:"))

def bmi_calculator(name, weight_lbs, height_ft, height_in):
    """Calculate BMI and return a weight category based on CDC standards and guidelines"""
    total_height = (height_ft * 12) + height_in
    bmi = (weight_lbs * 703) / (total_height ** 2)
    # Display BMI rounded to first decimal place. 
    print("BMI: {:.1f}".format(bmi))
    
    # BMI category ranges according to the CDC Adult BMI guidelines.
    # Source link: https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html
    if bmi < 18.5:
        return name + " is underweight"
    elif bmi >= 18.5 and bmi < 25: 
        return name + " is within range of healthy weight"
    elif bmi >= 25:
        return name + " is overweight"

result = bmi_calculator(name, weight_lbs, height_ft, height_in)
print(result)