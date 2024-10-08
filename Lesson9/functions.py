
def calculate_bmi(weight, height):
    calculation = weight / (height * height)
    return calculation

def show_results(weight, height):
    calculate = calculate_bmi(weight, height)
    if calculate <= 18.5:
        print("Underweight")
    elif calculate > 18.5 and calculate <= 25:
        print("Normal BMI")
    else:
        print("Overweight")