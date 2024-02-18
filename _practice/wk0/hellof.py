# Make Hello into a function
# 01:35:00
def hello(to="World"):
    print("hello,", to)

name = input("Your name? ")
hello(name)
#

# Make into a main function
# 01:37:00
def main():
    name = input("Your name again? ")
    hello(name)

def hello(to="world"):
    print("hello again,", to)

main()
#

