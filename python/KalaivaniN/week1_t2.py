# return python function as sum and multiply of the in two variables between numbers based on input?
def sums(num1,num2):
    sum=0
    for i in range(num1,num2+1):
        sum=sum+i  
    print(f"sum of the range between these {num1} and {num2} is {sum}")  
   
        
def multiply(num1,num2):
    mul=1
    for i in range(num1,num2+1):
        mul=mul*i

    print(f"multiply of the range between these {num1} and {num2} is {mul}")
      

num1=int(input())
num2=int(input())

sums(num1,num2)
multiply(num1,num2)
    



