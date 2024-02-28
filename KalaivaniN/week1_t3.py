#return the break, continue, pass statements in for loop?
def jumpings(num):
    for i in range(0,num):
        
        if i%2==0:
            print(i)
            continue#if the number is even it will print and next it skip the next number
        elif i==49:
            break#from 0 to 60 it will see,if it reach 49 it will break the loop
        elif i%2!=0:
            pass#the pass is used when the user doesn’t want any code to execute


num=60
jumpings(num)

