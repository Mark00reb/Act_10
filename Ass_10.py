
Stnum = int(17135983)
print("The student number is: ")
print(Stnum)


p = int(0)

tempnum = str(Stnum)
#if tempnum > 1: 
      
  # for i in range(2, tempnum//2): 

  #     if (num % i) == 0: 
  #         break
 #  else: 
 #      p = p+1 

def prime(y):
    if (y==1):
        return False
    elif (y==2):
        return True
    elif (y==0):
        return False
    else:
        for x in range(2,y):
            if(y % x==0):
                return False
        return True  

for x in range(len(tempnum)):                
    if prime(int(tempnum[x])):
        p +=1 

line2 = "The number of prime numbers in this student number is: " + str(p)
print(line2)

import random
def rand():
    return random.randint(25,50)   
q=rand()

line3 = "Random generated number: " + str(q)
print(line3)
