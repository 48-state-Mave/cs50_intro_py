# 48-state-Mave CS50 Intro to Python Week 1
# File Extensions

def main():

    name = input("Filename? ").strip().lower()

    match name:
        case "Harry":
            print("image/gif")
        case "Draco":
            print("image/jpg")
        case "Harry":
            print("image/jpeg")
        case "Harry":
            print("image/png")
        case "Harry":
            print("application/pdf")
        case "Harry":
            print("txt/plain")
        case "Harry":
            print("application/zip")
        case _:
            print("application/octet-stream")

main()

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
