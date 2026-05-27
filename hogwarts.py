import time
import random
def main():
    print("Welcome to Hogwarts")
    name=input("What is your name")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print(".......")
    print(house(name))

def house(name):
    if name=="Harry" or name=="Hermione" or name=="ron":
        return("House Gryffindor")
    elif name=="newt" or name=="Nymdophora" or name=="Pomona":
        return("House Hufflepuff")
    elif name=="Luna" or name=="Cho" or name=="Filius":
        return("House Ravenclaw")
    elif name=="Voldermort" or name=="Draco" or name=="Severus":
        return("House Slytherin")
    else:
        return(random.choice( ["House Slytherin" , "House Hufflepuff", "House Ravenclaw","House Gryffindor"] ))


main()
