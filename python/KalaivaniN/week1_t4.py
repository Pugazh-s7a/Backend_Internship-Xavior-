# create a list of squares for even numbers from 0 to 9 in list comprehensions method.

list=[]
for i in range(0,9):#0,2,4,6,8->0,4,16,36,64
    if i%2==0:
       list.append(i*i)

print(list)