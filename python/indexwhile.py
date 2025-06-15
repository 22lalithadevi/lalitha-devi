IPL=['CSK','RCB','MI','GT','SRH','PBKS']
print("Accessing elements without index:")
for i in IPL:
    print(i)
print("Accessing elements with index:")
for i in range(len(IPL)):
    print(IPL [i])
print("Accessing elements with indexusing while:")
i=0
while(i<len(IPL)):
    print(IPL[i])
    i+=1