import random

#🐢 The Tortoise
#🐇 The Hare
def race():

    finish_line = 50  #Finish Line
    tortoise_pos = 0  #Starting Position
    hare_pos = 0		 #Starting Position
    is_hare_asleep = False #Hare starts Awake
    tortoise_wins = 0
    hare_wins = 0search
    snail_wins=0
    for i in range(100000):
        # Reset positions for EVERY new race
        tortoise_pos = 0
        snail_pos=0
        hare_pos = 0
        finish_line = 50
        while tortoise_pos < finish_line and hare_pos < finish_line and snail_pos < finish_line:

    # Tortoise always moves a short distance between 1 - 3 meters at random
            meter=random.randint(1,3)
            tortoise_pos=tortoise_pos+meter

            snail_pos =snail_pos+1
            if random.random() < 0.20:
                snail_pos = hare_pos

    # Hare has a 30% chance of falling a sleep for a turn
            asleep_number=random.randint(1,100)
            if asleep_number<=80:
                is_hare_asleep=True
            else:
                is_hare_asleep=False
    # If Hare is awake, it will move 1 - 10 meters at random
            if is_hare_asleep==False:
                hare=random.randint(1,10)
                hare_pos=hare_pos+hare
            else:
                hare_pos=hare_pos
    # Print the positions of the Hare and Tortoise after each round



        if tortoise_pos >= finish_line:
                tortoise_wins += 1
        elif hare_pos >= finish_line:
                hare_wins += 1
        else:
            snail_wins += 1

    print("Tortoise wins:", tortoise_wins)
    print("Hare wins:", hare_wins)
    print("Snail wins:", snail_wins)
race()
