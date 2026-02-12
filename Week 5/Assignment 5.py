#BMI Calculator

def bmi_calculator(name, weight_lbs, height_ft, height_in):
    """Calculate BMI and return a weight category based on CDC standards and guidelines"""
    
    total_height = (height_ft * 12) + height_in
    
    bmi = (weight_lbs * 703) / (total_height ** 2)
    
    # BMI category ranges according to the CDC Adult BMI guidelines.
    # Source link: https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html
    if bmi < 18.5:
        category = name + " is underweight"
    elif bmi >= 18.5 and bmi < 25: 
        category = name + " is within range of healthy weight"
    elif bmi >= 25:
        category = name + " is overweight"
    return bmi, category

# Repeat the program as long as the user wants to.
r = input("Do you want to run the BMI calculator (yes or no)?")
while r == "yes": 
    # Ask the user for their name, weight, height in feet, and remaining height in inches.
    name = input("Enter your name:")

    weight_lbs = int(input("Enter your weight in pounds:"))
    while weight_lbs <= 0:
        print("Weight must be greater than 0.")
        weight_lbs = int(input("Enter your weight in pounds:"))

    height_ft = int(input("Enter your height in feet:"))
    while height_ft < 0:
        print("Height cannot be negative.")
        height_ft = int(input("Enter your height in feet:"))

    height_in = float(input("Enter your remaining height in inches:"))
    while height_in < 0:
        print("Height cannot be negative.")
        height_in = int(input("Enter your remaining height in inches:"))

    bmi_value, result = bmi_calculator(name, weight_lbs, height_ft, height_in)

    # Display BMI rounded to first decimal place. 
    print("BMI: {:.1f}".format(bmi_value))
    print(result)
    r = input("Do you want to run the BMI calculator (yes or no)?")

# BMI Table
print("        ", end="\t")      #spacing for height
for height in range(58, 77, 2):
    print(height,"in", end="\t")
print()

for weight in range(100, 251, 10):
    print(weight,"lbs:", end="\t") #spacing for weight
    
    for height in range(58, 77, 2):
         bmi_value, result = bmi_calculator("", weight, 0, height)
         print("{:.1f}".format(bmi_value), end="\t")
    print()