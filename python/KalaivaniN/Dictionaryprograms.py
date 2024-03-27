d1={1:'kalai',2:'vani',3:'siva'}

print("Length of d1",len(d1))#length of the dictionary

print("Keys",d1.keys())#keys 

print("Values",d1.values())#values

print("Items",d1.items())#items

print("Popped dict",d1.popitem())#pop items

d2={4:'ramya'}
d1.update(d2) #update function
print(d1)

d2.clear() #clear function

print(d2)
ndict=dict([('name','kalai'),('dpt','MCA')])
print(ndict)

k=dict.copy(ndict) 
print(k)

name=('kalai','siva','karan')
bgdict=dict.fromkeys(name)
print(bgdict)
print(d1.get(2)) #get function-get the value of the specified key
print(d1.pop(1)) #pop the value of the specified key
print(d1)