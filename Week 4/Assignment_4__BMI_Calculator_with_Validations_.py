#BMI Calculator

# Ask the user for their name, weight, height in feet, and remaining height in inches.
# Moved inputs under bmi_calculator.

def bmi_calculator(name, weight_lbs, height_ft, height_in):
    """Calculate BMI and return a weight category based on CDC standards and guidelines"""
    
    total_height = (height_ft * 12) + height_in
    
    # Parameter Validation
    if weight_lbs <= 0:
        raise ValueError("Weight must be greater than 0.")

    if height_ft < 0:
        raise ValueError("Height cannot be negative.")

    if height_in < 0:
        raise ValueError("Height cannot be negative.")

    if total_height <= 0:
        raise ValueError("Height must be greater than 0.")

    assert total_height > 0 #Assertion
    
    bmi = (weight_lbs * 703) / (total_height ** 2)
    # Display BMI rounded to first decimal place. 
    print("BMI: {:.1f}".format(bmi))
    
    # BMI category ranges according to the CDC Adult BMI guidelines.
    # Source link: https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html
    # Nested if statements
    if bmi < 18.5:
        return name + " is underweight"
    else:
       if bmi < 25: 
           return name + " is within range of healthy weight"
       else:
           return name + " is overweight"


# Turn inputs into a function to use try/except on the program. 
def main():
    name = input("Enter your name:")
    weight_lbs = int(input("Enter your weight in pounds:"))
    height_ft = int(input("Enter your height in feet:"))
    height_in = float(input("Enter your remaining height in inches:"))
    total_height = (height_ft * 12) + height_in

    # Range and Constraint Validation
    if weight_lbs <= 0:
        raise ValueError("Weight must be greater than 0.")

    if height_ft < 0:
        raise ValueError("Height cannot be negative.")

    if height_in < 0:
        raise ValueError("Height cannot be negative.")

    if total_height <= 0:
        raise ValueError("Height must be greater than 0.")

    #Call the BMI function and print the result
    result = bmi_calculator(name, weight_lbs, height_ft, height_in)
    print(result)

# Data type validation. Use try/except so the program doesn't crash if the user enters a bad input.
try:
    main()
except ValueError as e:
    print("Error:", e)