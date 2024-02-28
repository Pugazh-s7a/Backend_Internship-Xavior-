#3. return the break, continue, pass statements in for loop?
def loop(a):
    for i in range(1,a+1):
        if i ==2:
            print(i)
            print("continue statemnet at no 2")
            continue
        if i== 4:
            print("pass statement at no 4")
            pass
        if i== 5:
            print("Break statement at no 5")
            break
    return i
a= int(input("Enter the value of a: "))
loop(a)


