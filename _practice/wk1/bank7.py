# 48-state-Mave CS50 Intro to Python Week 1
# Bank greeting

def main():
    g = input("Greeting? ").strip().lower()
    x = str(g[0:1]).strip()
    y = str(g[0:5]).strip()
    if y == "hello":
        r = 100
        print("$", r)
    elif x == "h":
        r = 20
        print("$", r)
    else:
        r = 0
        print("$", r)

main()
