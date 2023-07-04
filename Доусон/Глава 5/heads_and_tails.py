import random
heads = 0
tails = 0
while heads + tails < 100:
    guess = random.randint(1, 2)
    if guess == 1:
        heads += 1
    else:
        tails += 1
print("орлов выпало: ", heads, "решек выпало: ", tails)