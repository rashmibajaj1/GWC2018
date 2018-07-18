def main():
    while(True):
        choice = input ("Press 1 for a poem, 2 for a joke, 3 for a better joke, 4 to generate a haiku, 5 to add 2 numbers, and 6 to exit." )
        if choice == "1":
            poem()
        elif choice == "2":
            joke()
        elif choice == "3":
            betterjoke()
        elif choice == "4":
            haiku()
        elif choice == "5":
            num1 = input("Enter num1")
            num2 = input("Enter num2")
            result=sum(int(num1),int(num2))
            print("Sum=",result)
        else:
            print("Bye!")
            exit()

def poem():
    print("Forever we remain oblivious to the future,")
    print("lost to the past and enduring our torture.")
    print("Forever we take chances to settle our scores,")
    print("losing some battle and winning some wars")

def joke():
    print("What do you call a pig who does karate?")
    print("A pork chop!")

def betterjoke():
    print("What did the baby corn ask the mama corn?")
    print("Where's Pop corn?")

def haiku():
    five_syllables = ["An old silent pond", "In the twilight rain", "I really like toast."]
    seven_syllables = ["The room was dark and somber", "death is inevitable", "Scorching sun rays, blazing winds"]
    five_syllables2 = ["Perfect summer day", "I sleep peacefully", "and I fall in love"]
    import random
    print(random.choice(five_syllables))
    print(random.choice(seven_syllables))
    print(random.choice(five_syllables2))

def sum(num1,num2):
    return num1+num2
main()
