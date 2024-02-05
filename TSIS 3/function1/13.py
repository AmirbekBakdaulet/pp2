import random
def g_number(name):
    secret_num = random.randint(1,20)
    attempts=0
    while True:
        attempts+=1
        num=int(input("Take a guess."))
        if num>secret_num:
            print("Your guess is too high.")
        elif num==secret_num:
            print(f"Good job,{name}! You guessed my number in {attempts} guesses!")
            break
        else:
            print("Your guess is too low.")
            
name=input("Hello! What is your name?")
print(f"Well,{name}, I am thinking of a number between 1 and 20.")
g_number(name)