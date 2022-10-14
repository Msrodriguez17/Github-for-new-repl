from random import randint
  # random
  # Python comes with a built in random library. There are a lot of functions included in this random library, so we will only 
  #show you two useful functions for now.
print("random")
dice1 = randint(1,7)
print(f"dice1 : {dice1}")
dice2 = randint(1,7)
print(f"dice2 : {dice2}")
rolled_doubles = dice1 == dice2
if rolled_doubles:
  print("you rolled doubles")
else: print("not doubles")