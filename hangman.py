print("Let's play hangman!")
#print("__ __ __ __ __ __")

#list = ["__", "__", "__", "__", "__", "__"]
word=input("Enter word:")
list=[]
for i in range(len(word)):
    list.append('_')
print("My List:",list)
lives=8
while lives != 0:
    letter = input ("Guess a letter!")
    if letter in word:
        guessLetterIndex=word.index(letter)
        list[guessLetterIndex]=letter
        print(list)
    if '_' not in list and lives<7:
        print("Congratulations")
        exit()
    lives= lives - 1


    '''
    if(answer == "r"):
        list.pop(0)
        list.insert(0,"r")
        print(list)
    elif (answer == "h"):
        list.pop(1)
        list.pop(4)
        list.insert(1,"h")
        list.insert(4, "h")
        print(list)
    elif (answer == "y"):
        list.pop(2)
        list.insert(2,"y")
        print(list)
    elif (answer == "t"):
        list.pop(3)
        list.insert(3,"t")
        print(list)
    elif (answer == "m"):
        list.pop(5)
        list.insert(5,"m")
        print(list)
    elif (answer != "r" or "h" or "y" or "t" or "m"):
        print("Sorry, that is incorrect.")
    elif (answer== "r" and "h" and "y" and "t" and "m"):
        print ("Congratulations")
    '''
