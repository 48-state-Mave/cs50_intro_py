# 48-state-Mave CS50 Intro to Python Week 0 - Problem 0.5
# Tip calculator

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    x = d.replace("$", "")
    return float(x)

def percent_to_float(p):
    y = p.replace("%", "")
    z = float(y)
    n = z / 100
    return n

main()