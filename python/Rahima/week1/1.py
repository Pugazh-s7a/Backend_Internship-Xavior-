#1. return the variable checking str format return True, int format return False and Float format will return None
data = ['1',2,3.0,4,'5',6]
def variable(a):
    if type(a)== str:
        return True
    if type(a)== int:
        return False
    else:
        return  False

for a in data:
    print(variable(a))

