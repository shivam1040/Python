import random
rand=random.randint(1, 100)
randguess=None
guess=0

while(randguess!=rand):
    randguess=int(input("Enter number: "))
    if(randguess==rand):
        print("right")
    else:
        if(randguess>rand):
            print("wrong, enter small")
        else:
            print("wromg, enter large")
    guess+=1

print("guessed in: ", guess)