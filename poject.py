
def main():
    x = int(input("Enter First Number:"))
    y = int(input("Enter Second Number:"))
    z = 1
    if(x==y):
        print("Both the Numbers are equal")
    if(x>y):
        y+=1
        if(x==y):
            print("No Numbers between Them")
    while(x>y):
        print("(",z,")Number is:",y)
        y+=1
        z+=1

    if(y>x):
        x+=1
        if(y==x):
            print("No Numbers between Them")
    while(y>x):
        print("(",z,")Number is:",x)
        x+=1
        z+=1
    
    restart= input("Do you want to restart Y/N: ").upper()

    if restart == "Y":
        
        main()
    else :
        exit()

main()
