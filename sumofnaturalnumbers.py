num=int(input("Enter a number: "))
print(num)
sum=0
for i in range(1,num+1):
    sum=sum+i
    i+=1
    print(sum)