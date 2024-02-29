#5. swapping keys and values in a dictionary 
swapping_dict= {'a': 1, 'b': 2, 'c': 3}
result = {value: key for key, value in swapping_dict.items()}
print(result)
