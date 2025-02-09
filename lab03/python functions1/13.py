import random
def game():
    cnt = 0
   
    print("Hello! What is your name?")
    name = input()
    print(f"Well,{name}, I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    num = int(input())
    
    guess = random.randint(1,20)
    while num:
        cnt+=1
        if num < guess:
            print("Your guess is too low.")
            print("Take a guess.")
            num = int(input())
        elif num > guess:
            print("Your guess is too high.")
            print("Take a guess.")
            num = int(input())
        else:
            print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
            break
        

game()