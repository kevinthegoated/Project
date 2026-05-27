import random
secret=random.randint(1,100)



def linear_search():
    global secret
    attempt=0
    print(f"The secret number is: {secret}")
    for guess in range(1,101):

        guess=random.randint(1,100)
        attempt=attempt+1
        if guess==secret:
            print (f"bot found secret number {secret}")
            print(f"attempts:{attempt}")
#linear_search()

def bi_search():
    low=1
    high=100
    found=False
    guess=random.randint(1,100)
    attempt=0
    while found== False:
        attempt=attempt+1
        mid=(low+high)//2
        if mid == guess:
            found = True
        elif mid < guess:
            low = mid + 1
        else:
            high = mid - 1
    print(f"The secret number is: {secret}")
    print(f"found in {attempt} attempts")

bi_search()
