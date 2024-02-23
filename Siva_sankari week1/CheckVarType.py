data = ['1', 2, 3.0, 4, '5', 6]
def varData(varType):
      if isinstance(varType,int):
        return False
      elif isinstance(varType,str):
        return True
      elif isinstance(varType,float):
        return None

for varType in data:
    print(varData(varType))

# a = [i for i in range(0,10)]
# b = [i for i in range(10,20)]
# c = [i for i in range(20,30)]
# d="Index {0} value {0},{1},{2}"
# print(d.format(a,b,c))

