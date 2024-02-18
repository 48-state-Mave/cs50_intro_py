# Tip Calculator

# nevermind doesnt work
meal = input("Meal price? ")
price = int(''.join(filter(str.isdigit, meal)))
print("Meal price is:", price)
floated = float(price)
print("Also ", floated)


"""
# works with sign
meal = input("Meal price? ")
price = int(''.join(filter(str.isdigit, meal)))
print("Meal price is:", price)
floated = float(price)
print("Also ", floated)

# this one works w/o sign
meal2 = float(input("Meal2 price? "))
print("Meal2 price is:", meal2)
floated22 = float(meal2)
print("Also ", floated22)

ppp = input("What p tip? ")
x = int(ppp)
print("x is:", x)
floated2 = float(x)
print("Also ", floated2)
"""

"""
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(dollars):
    # x = float(dollars_to_float, 1)(dollars)
    float(dollars, 1)
    return dollars

def percent_to_float():
    y = round(percent, 1)
    percent = y
    return percent

main()
"""
