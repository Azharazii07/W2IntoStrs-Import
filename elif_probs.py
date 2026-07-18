ch = int(input('Enter Choice\n'))
if(ch == 1):
    n = int(input("Enter a number\n"))
    if(n%2==0):
        print("Even")
    else :
        print("Odd")
    del n 
elif(ch == 2) :
    n = int(input("Enter a number\n"))
    if(n%5==0):
        if(n%10==0) :
            print("0")
        else :
            print("5")
    else :
        print("Other")
    del n
elif(ch == 3) :
    n = int(input("Enter num\n"))
    k = n % 10
    if (k == 5) :
        print(5)
    elif (k == 0) :
        print(0)
    else :
        print('Other')
    del n
elif(ch == 4) :
    m = int(input("Enter Marks\n"))
    if((m>=90)and(m<=100)):
        print('A')
    elif((m>=80)and(m<90)):
        print('B')
    elif((m>=70)and(m<80)):
        print('C')
    elif((m>=60)and(m<70)):
        print('D')
    elif((m<60)and(m>0)):
        print('E')
    else :
        print("Invalid Input")
    del m 
elif(ch == 5) :
    tol = int(input("Define max. travel time\n"))
    tolpr = float(input("Define Afforable Rate\n"))
    t=int(input("Travel from City A to B , enter Time\n"))
    pr = float(input("Enter Price\n"))
    if(t>tol) :
        if(pr>tolpr) :
            print("Via Train")
        else :
            print("Via Coach")
    else :
        if(pr>tolpr) :
            print("Via Daytime Flight")
        else :
            print("Via Nightime Flight")
print("Safe Journey to City B")
        
        
    
    


