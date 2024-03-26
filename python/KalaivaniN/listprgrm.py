import random
from collections import OrderedDict

#2: Python List length check?
l1=[1,2,3,4,5]
k=len(l1)
print(k)
sum=0   #3: Python Program to find Sum of Elements in a List?
for i in range(0,k):
    sum=sum+l1[i]
print(sum)
print(l1[::-1]) # 4. Python Program to Print List Items in Reverse Order?

#6. Write a Python program to find the items starts with specific character from a given list.?

l= ['abcd', 'abcf', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
character=input("Enter the Character")
result_list=[]
for i in l:
    if i.startswith(character):
        result_list.append(i)
print(result_list)
        
#7. Python program to check Digit or Not?
k=['1','k','3']
for i in k:
    if i.isdigit():
        print(i,"Is Digit")
    else:
        print(i,"Not a Digit")
  
  


#7. using Shuffle and print a specified list? random?
lr=['a','b','c']
random.shuffle(lr)
print(lr)

      
#8. Write a Python program to get the smallest number and longest from a list?
l=[1,2,14,15,9,7,111,421,91]
l.sort(reverse=True)
print(l)
n=len(l)
print(l[0],"The smallest Number")
print(l[n-1],"The Largest Number")

#9. list using enumerate in python?
l=[10,20,30,40,50]
for i,j in enumerate(l):
    print(i,"Index")
    print(j,"Values")
    


#1. Python Program to Remove an Item from Tuple?
tup1=(1,2,3,4)
#tup1=tuple()
print(tup1)
tlist=list(tup1)
tlist.remove(tlist[2])
print(tlist)



tupk = (1, 3, 5, 2, 3, 5, 1, 1, 3)
res = tuple(OrderedDict.fromkeys(tupk))

print(res)
