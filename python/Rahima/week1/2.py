#2. return python function as sum and multiply of the in two variables between numbers based on input?
def  calculate(a,b,op):
    result=[]
    if op == '+':
        for i in range(1,a+1):
            for j in range(1,b+1):
                result.append(i+j)
        print(f'The sum of {a} and {b} is',a+b)

    elif op == '*':
        for i in range(1,a+1):
            for j in range(1,b+1):
                result.append(i*j)
        print(f"Product of {a} and {b} is",a*b)
    return result

a=int(input("Enter the value for a: "))
b=int(input("Enter the value for b: "))
op=input("Enter operation (+ or *): ")

print(calculate(a,b,op))

