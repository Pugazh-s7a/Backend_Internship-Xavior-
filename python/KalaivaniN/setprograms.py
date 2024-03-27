set1={1,2,3,4,5}
set2={3,4,6,7}
set1.difference_update(set2)#difference
print(set1)
print(set1-set2)
print(set2-set1)


set1.discard(3) #discard
print(set1)

set1={1,2,3,4,5}
set2={2,3}
print(set1.issuperset(set2)) #issuperset()  return True

print(set2.issuperset(set1)) #return Fase

print(set1.issubset(set2)) #issubset() return False

print(set2.issubset(set1)) #issubset() return True

print(set1.isdisjoint(set2)) #disjoin() return False
set3={6,7}
print(set1.isdisjoint(set3)) #disjoin() return True


print(set1.union(set2)) #union function

print(set1.intersection(set2)) #Intersection 