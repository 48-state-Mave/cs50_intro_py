# 48-state-Mave CS50 Intro to Python Week 1
# Math Interpreter

def main():
    x = input("Math problem: ")
    xs1, xs2, xs3 = x.split()

    n1 = float(xs1)
    n2 = float(xs3)
    y = xs2

    if y == "*":
        print(n1*n2)
    elif y == "/":
        yy = n1/n2
        print(f{yy:.1f})
    elif y == "+":
        print(n1+n2)
    elif y == "-":
        print(n1-n2)

main()
