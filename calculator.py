import sys
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b



while(True):
    print('''Choice:
      1.Additio
      2. Subtection
      3. Multiplication
      4. Division
      5. Exit''' )
    ch = int(input("Enter you Choice: "))
    
    if(ch!=5):
        A = int(input("Enter no.1: "))
        B = int(input("Enter no.2: "))
    match ch:
        case 1:
            z = add(A,B)
            print(z)
            
        case 2:
            y = sub(A,B)
            print(y)
            
        case 3:
            x = mul(A,B)
            print(x)
            
        case 4:
            w=div(A,B)
            print(w)
            
        case 5:
            print("Your Exit from a loop")
            sys.exit(0)

    
