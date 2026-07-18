# Importing Packages --- 2. import library
import random 
r = random.random()
print(r)
if (r > 0.5) :
    print("Heads")
else :
    print("Tails") 
del r
print()
r = random.randrange(0,2)
print(r)
if(r==1) :
    print("Heads")
else :
    print("Tails") 
print()  
r1 = random.randrange(1,7)
r2 = random.randrange(1,7)
print(" 1st Dice :",r1,"\n","2nd Dice :",r2,"\n","Sum :",r1+r2)
