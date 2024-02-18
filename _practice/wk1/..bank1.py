# Bank greeting

def main():
    g = input("Greeting? ").strip().lower()
    print(g)
    print("$", r)

def pay():
    g = input("Greeting? ").strip().lower()
    if g == "hello":
        r = 100
    elif g == "h":
        r = 20
    else:
        r = 0
    return(r)

main()
