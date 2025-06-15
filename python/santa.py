gift_list=[]
print("Welcome to santa sleigh....!!")
while(True):
    print("****************MENU***************")
    print("1. enter 1 to add the gift name")
    print("2. enter 2 to remove the duplicates")
    print("3. enter 3 to sort and display the final list")
    choice=int(input("enter your choice: "))
    if(choice>=1 and choice<=3):
        if(choice==1):
            name=input("enter the gift name: ")
            gift_list.append(name)
            print(name,"is added to the giftt list.....!")
        elif(choice==2):
            unique_list=[]
            for i in gift_list:
                if i not in unique_list:
                    unique_list.append(i)
            print("unique list: ",unique_list)
        elif(choice==3):
            unique_list.sort()
            #print("here are the finalized gift list.....!")                
            print(unique_list)
            break
    else:
        print("invalid choice please give correct choice from 1 to 3.....!")