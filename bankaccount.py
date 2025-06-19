import sys
 
li = []

def credit(amm,balance):
    balance += amm
    return balance 

def debit(amm,balance):
    balance -= amm
    return balance

balance=2000
x = balance
while(True):
   print('''
    Choice: 1. Credit
            2. Debit
            3. Show balance
            4. Passbook Print
            5. Exit
         ''') 
   ch = int(input("Enter Choice: "))
   match(ch):
       case 1:
           balance = x
           c = int(input("Enter ammount for credit: "))
           x = credit(c,balance)
           print("Final balance: ",x)
           li.append(f"Yout money {c} is credited, balance is: {x}")

       case 2:
           balance = x
           d = int(input("Enter ammount for debit: "))
           if(d>balance):
               print("Your balance is less than ammount.")
           else:
            x = debit(d,balance)
           print("Final balance: ",x)
           li.append(f"Yout money {d} is debited, balance is: {x}")
        
       case 3:
           balance = x
           print("Balance is: ",balance)

       case 4: print(li)

       case 5: sys.exit(0)
           