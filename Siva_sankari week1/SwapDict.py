swapping_dict = {'a': 1, 'b': 2, 'c': 3}
swapped_dict={}
for key,value in swapping_dict.items():
    swapped_dict[value]=key
print(swapped_dict)