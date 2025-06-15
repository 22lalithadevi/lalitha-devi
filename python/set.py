set={'python','c','c++','java','sql','javascript','angular js','node js'}
print(set)
print(type(set))
#accessing set elements
print('sql' in set)
#adding elements(only single element)
set.add('dbms')
set.add('express ja')
print(set)
#update(adding multiple elements)
set.update(['ds','R'])
print(set)

# removing elements
set.remove('javascript')
print(set)
#pop(to remove and print arbitary element)
set.pop()
print(set)
#discard(remove specific element) 
set.discard('angular js')
print(set)
#clear the all set
set.clear()
print(set)
#union
set1={1,2,3,4}
set2={3,2}
print(set1 | set2)
#intersection
print(set1&set2)
#difference
set3=set1.difference(set2)
print(set3)
#subset(if all num is there then it print true)
isub=set1.issubset(set2)
print(isub)
#superset
isup=set1.issuperset(set2)
print(isup)