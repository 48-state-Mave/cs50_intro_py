# WEEK 0 - EXAMPLE 1

# Hello World
# 00:03:20
print("Hello World")
# Hello World

# Ask for name
# 00:27:00
name = input("What's your name? ").strip().title()
print(name)
# name (without extra spaces and title case)

# Split name
# 00:00:00
name = input("What's your name? ").strip().title()
first, last = name.split(" ")
print(name)
#

# Say hi
# 00:00:00
name = input("What's your name? ").strip().title()
first, last = name.split(" ")
print("Hello " + first)
#

# Use f code
# 00:00:00
name = input("What's your name? ").strip().title()
first, last = name.split(" ")
print(f"Hello, {first}")
#

# Default parameters (arguments when used)
# From docs:
# 00:00:00
# print(*objects, sep' ', end='\n', file=sys.stdout, flush=False)
#

# Make single line
# 00:00:00
name = input("Your name? ")
print("Hello, ", end="")
#

# Separate name into firstn and lastn
# 00:00:00
name = input("Your name? ")
print("Hello, ", name, sep="???")
#

# Make Hello into a function
# 01:27:00
def hello(to):
    print("hello, to")

name = input("Your name? ")
hello(name)
#

# Make Hello into a function
# 01:21:00
def hello(to):
    print("hello, to")

name = input("Your name? ")
hello(name)
#
