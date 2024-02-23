import random
a=int(input("Start value = "))
b=int(input("End value = "))
secret_num=random.randrange(a,b)
guessllist=[]
def guessingGame(x,y):
  n=4
  for i in range(0,n):
    global Guess
    Guess = int(input())
    guessllist.append(Guess)
    if secret_num==Guess:
        print(f"You found the Secret number {secret_num} ")
        break
    else:
        print("Attempt Failed")
        continue

guessingGame(a,b)
newlist=[]
for i in guessllist:
  if(secret_num == i):
      pass
  else:
      newlist.append(i)
print(newlist)

