s1=input("enter the string:")
sum=" "
arr=s1.split(" ")
c=len(arr)
while c>0:
    d=arr[c]
    sum+=d
    c=c-1
print(sum)
