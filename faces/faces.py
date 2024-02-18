# 48-state-Mave CS50 Intro to Python Week 0 - Problem 0.3
# Functions that replace emojis

def main():
    emotion = input("Are you happy or sad? ").replace(":)", "🙂").replace(":(", "🙁")
    convert(emotion)

def convert(emotion):
    print(emotion)

main()
