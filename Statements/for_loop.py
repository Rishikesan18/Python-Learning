mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)
   
for eve in mylist:
    if eve %2==0:
        print("Even numbers:",eve)
    else:
        print(f"Odd numbers:{eve}")
        
        
for _ in "rishi":
    print("HI")
    
mylist1 = [(1,2,3), (5,6,7),(8,9,10)]
for a,b,c in mylist1:
    print(b)