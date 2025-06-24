n=int(input("enter no: "))
print("prime no are")
for i in range(1,n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)
