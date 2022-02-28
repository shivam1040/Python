import random
def game(co, pl):
    if(co==pl):
        return "Tie"
    elif(co=="s"):
        if(pl=="w"):
            return "Lose"
        elif(pl=="g"):
            return "Win"
    elif(co=="w"):
        if(pl=="g"):
            return "Lose"
        elif(pl=="s"):
            return "Win"
    elif(co=="g"):
        if(pl=="s"):
            return "Lose"
        elif(pl=="w"):
            return "Win" 
rand=random.randint(1,3) #random number from 1 to 3
c=""
if(rand==1):
    c="s"
elif(rand==2):
    c="w"
else:
    c="g"
p=input("Enter your choice; s, g or w: ")
print("Comp chose: "+c)
print(game(c,p))
