def game():
    cnt = 0
    required = 13
    print("Hello! What is your name?")
    name = input()
    print(f"Well,{name}, I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    num = int(input())

    while(num):
        cnt+=1
        if num < required:
            print("Your guess is too low.")
            print("Take a guess.")
            num = int(input())
        elif num > required:
            print("Your guess is too high.")
            print("Take a guess.")
            num = int(input())
        elif num == required:
            print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
            break
        

game()