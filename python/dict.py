jobrole={101:'front-end',102:'back-end',103:'sql administrator',104:'software developer'}
print(jobrole)
print(type(jobrole))
print(jobrole[101])
print(jobrole[102])
print(jobrole[103])
#modiication
jobrole[101]='ui/ux developer'
print(jobrole)
# adding element
jobrole[105]='data engineer'
jobrole[106]='python developer'
jobrole[107]='data analysis'
print(jobrole)
#deleting
jobrole.pop(101)
del jobrole[104]
print(jobrole)
#length
print(len(jobrole))
#keys
print(jobrole.keys())
#values
print(jobrole.values())
#items(used to print list and tuple)
print(jobrole.items())
#update
a={108:'sql'}
jobrole.update(a)
print(jobrole)
#fromkeys
key={109,110}
value='data structure'
print(jobrole.fromkeys(key,value))                             