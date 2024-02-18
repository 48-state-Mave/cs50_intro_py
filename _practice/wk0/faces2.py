# Functions that replace emojis

def main():
    emotion = input("Are you happy or sad? ").replace(":)", "🙂").replace(":(", "🙁")
    convert(emotion)

def convert(emotion):
    print(emotion)

main()
