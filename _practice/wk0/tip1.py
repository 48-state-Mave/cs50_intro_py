# Tip Calculator

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # x = float(dollars_to_float, 1)(dollars)
    dollars_to_float = round(dollars_to_float, 1)
    return dollars

def percent_to_float(p):
    y = round(percent, 1)
    percent = y
    return percent

main()
