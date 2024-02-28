a = [i for i in range(0,10)]
b = [i for i in range(10,20)]
c = [i for i in range(20,30)]
# d="Index {0} value {0},{1},{2}"
# print(d.format(a,b,c))
for i in range(len(a)):
    print(f"Index {a[i]} value {a[i]}, {b[i]},{c[i]}")
    break