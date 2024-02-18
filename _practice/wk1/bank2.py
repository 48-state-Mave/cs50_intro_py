# Bank greeting

def main():
    g = input("Greeting? ").strip().lower()
    print(g)
    r = 1
    if g == "hello":
        r = 100
    elif g == "h":
        r = 20
    else:
        r = 0
    print("$", r)

main()
