# 48-state-Mave CS50 Intro to Python Week 1
# Bank greeting

def main():
    g = input("Greeting? ").strip().lower()
    x = g.startswith("hello")
    y = g.startswith("h")
    print(g)
    if x == True:
        print("$100")
    elif y == True:
        print("$20")
    else:
        print("$0")

main()
