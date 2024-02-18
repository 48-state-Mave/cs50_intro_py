# 48-state-Mave CS50 Intro to Python Week 1 - Problem 1.3
# File Extensions

def main():

    name = input("Filename? ").strip().lower()

    if name.endswith(".gif"):
        print("image/gif")
    elif name.endswith(".jpg"):
        print("image/jpeg")
    elif name.endswith(".jpeg"):
        print("image/jpeg")
    elif name.endswith(".png"):
        print("image/png")
    elif name.endswith(".pdf"):
        print("application/pdf")
    elif name.endswith(".txt"):
        print("text/plain")
    elif name.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()
