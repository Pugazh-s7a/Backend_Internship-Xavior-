#1. How to convert a list into a string using list comprehension & normal way need 2 ways ansers?
#list1 = ['hi', 'welcome', 20, 'hello'], list2=['I', 'and', 'fine']
list1 = ['hi', 'welcome', 20, 'hello']

listToStr = ' '.join([str(elem) for elem in list1])
 
print(listToStr)

list2 = ['I', 'and', 'fine']
for i in list2:
  print(i,end=" ")

print()

#2. How to convert a list into a tuple?

list=[1,2]
print(tuple(list))

#3.i) How to convert a list into a set? and ii) Python Program to Convert Integer to String

list=[1,2,3]
print(set(list))

num=123
ans=str(num)
print(type(ans))

#4. string Slice a="hello how are you"? ans: w a
a="hello how are you"
print(a[8:11])

#5. list slice a=[1,2,3,4,5,6,7,8] ans: [5,6]

a=[1,2,3,4,5,6,7,8]
print(a[4:6])

#6. pattern program ans like:
""" 1
	22
	333
	4444"""

for i in range(1,5):
  for j in range(1,5):
    if i>=j:
      print(i,end=" ")
  print()


#8. Python program to check Lowercase or Uppercase?
  
str='KALAIVANI'
if str.isupper():
  print("Uppercase")
else:
  print("Lowercase")

#9. Python program to find Positive or Negative number negative number?
  
num=-234
if num>0:
  print("Positive Number")
elif num<0:
  print("Negative Number")

# 10. Simple Calculator program and Using Functions is main?
"""
def calculator(num1,num2):
  choice=input("+ - * /")
  if choice=='+':
    ans=num1+num2
  elif choice=='-':
    ans=num1-num2
  elif choice=='*':
    ans=num*num2
  elif choice=='/':
    ans=num1/num2
  return ans"""

"""def calculator(choice,num1,num2):
  switch={
      '+':num1+num2,
      '-':num1-num2,
      '*':num1*num2,
      '/':num1/num2,
      
      }
  return switch.get(choice,"Invalid input")
  
num1=int(input("enter first num"))
num2=int(input("enter second num"))
choice=input("+ - * /")
print(calculator(choice,num1,num2))"""

#11. Python Program to Merge Two Dictionaries 2 ways?

dict1={1:'kalai',2:'ramu',3:'paru',4:'Natu'}
dict2={5:'siva',6:'rahi'}
dict1.update(dict2) #method1
print(dict1) 
mdict={**dict1,**dict2} #method2
print(mdict)
mdicts=dict1|dict2 #method3
print(mdicts)

#12. File Read and Write
string='kalai'
open("demo.txt",'w').write(string)       #read&write
r=open("demo.txt",'r').read()
print(r)

#13. Python Program to Concatenate Two Lists? use 2 differend ways.
list1=['kalai','vani']
list2=['rama','laksh']
for i in list2:
  list1.append(i)
print(list1)

list3=['siva','sank']
list4=['asiya','rahi']
print(list3+list4)

#14. Python Program to Convert Two Lists Into a Dictionary?
listk=['paru','ramu','natu']
listv=['kalai','siva','rami']
res=listk+listv

dict={}
for i in range(0,6):
  dict[i]=res[i]
print(dict)
  
details=['name','age','gender']
info=['kalai','21','female']
dict={}
for i in range(0,3):
  for j in range(0,3):
    if i==j:
      dict[details[i]]=info[j]
print(dict)

#15. Python Program to Remove Duplicate Element From a List?

list1 = [1, 5, 3, 6, 3, 5, 6, 1,8]
res = [i for n, i in enumerate(list1) if i not in list1[:n]]
print( res)

"""tlist=[1,2,3,2,1]
kalai=set(tlist)
print(kalai)
print(list(kalai))    run it in removedup.py"""

#17. python if else program using (and,or,in,==,!=,>,<) using all single program?

city=['tnvl','pettai']
info=input("Enter your city")
if info in city:
  age=int(input("enter your age"))

  if age>18 or age==18:
    print("Eligible to vote")
  elif age<18 and age>10:
    print("Not eligible and teenagers")
  elif age<10:
    print("children")

else:
  print("Your from another city")


