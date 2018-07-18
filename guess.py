answer = input("Pick a number 0 to 10")
answer = int(answer)

while (answer < 8):
  print("Try again! Guess higher")
while (answer > 8):
  print("Try again! Guess lower")
while (answer == 8):
  print("Congratulations")
