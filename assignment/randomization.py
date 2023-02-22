from random import random, randint

lst = []
for i in range(10):
    new = randint(200,5000)
    if new in lst:
        continue
    else:
       lst.append(new)
print(lst)
