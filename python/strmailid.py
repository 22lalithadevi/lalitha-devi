str=input("enter email id: ")
if '@' in str:
    name,a=str.split('@')
    if '.' in str:
        organisationname=a.split('.')[0]
        print("name is: ",name)
        print("organisation name is: ",organisationname)
