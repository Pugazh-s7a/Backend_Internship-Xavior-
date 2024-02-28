#return the variable checking str format return true,int format retrun False and Float will return None
#data=['1,2,3.0,4,'5',6]

def t1(data):
    for i in range(0,len(data)):
        if type(data[i]) == str:
            print("True")
        elif type(data[i]) == int:
            print("False")
        elif type(data[i]) == float:
            print("None")

data = ['1', 2, 4.5, 4, '5', 6]
t1(data)


