#swapping keys and values in a dictionary 
swapping_dict= {'a': 1, 'b': 2, 'c': 3}
k=swapping_dict.keys()
v=swapping_dict.values()
newdict=dict(zip(v,k))
print(newdict)



