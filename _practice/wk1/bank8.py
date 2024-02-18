# 48-state-Mave CS50 Intro to Python Week 1
# Bank greeting

def main():
    g = input("Greeting? ").strip().lower()
    x = str(g[0:1]).strip()
    y = str(g[0:5]).strip()
    if y == "hello":
        print("$100")
    elif x == "h":
        print("$20")
    else:
        print("$0")

main()
