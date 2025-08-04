import random
print("Welcome to Guessing Game!\nYou have 7 chances to guess a number.")
low=int(input("Enter the lower bound: "))
high=int(input("Enter the upper bound:"))
count=0
ch=7
num=random.randint(low,high)
while count<=7:
    count+=1
    guess=int(input("Guess a number: "))
    if guess==num:
        print("You guessed right!")
        break
    elif guess>num:
        print("The number is a little lower than the number you guessed")
    elif guess<num:
        print("The number is a little higher than the number you guessed")
    elif count>=ch and guess!=num:
        print(f"The number you entered does not match\n the number {num}")
