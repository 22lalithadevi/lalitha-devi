guest_list=[]
print("Welcom to party....!!")
while(True):
    print("****************MENU***************")
    print("1. enter 1 to add the guest")
    print("2. enter 2 to remove the guest who cancles")
    print("3. enter 3 to check if a friend is attending party or not")
    print("4. enter 4 to sort and print the final guest list")
    print("5. enter 5 to exit")
    choice=int(input("enter your choice: "))
    if(choice>=1 and choice<=5):
        if(choice==1):
            name=input("enter the guest name: ")
            guest_list.append(name)
            print(name,"is added to the guest list.....!")
        elif(choice==2):
            cancelled_name=input("enter the name which you want to cancel: ")
            if cancelled_name in guest_list:
                guest_list.remove(cancelled_name)
                print(cancelled_name,"is removed from guest list.....!")
            else:
                print(cancelled_name,'is not present in guest list.....!')
        elif(choice==3):
            check_guest=input("enter the guest name: ")
            if check_guest in guest_list:
                print(check_guest,'is attending the party....!')
            else:
                print(check_guest,'is not attending the party.....!')
        elif(choice==4):
            guest_list.sort()
            print("here are the finalized guest list who are attending the party.....!")
            print(guest_list)
        elif(choice==5):
            print("Enjoy the party.....!")
            break
    else:
        print("invalid choice please give correct choice from 1 to 5.....!")