s1=input("enter the string:")
s2=""
p=-1
for x in s1:
    i=-1
    c=0
    while(1):
        i=s1.find(x,i+1)
        if i==-1:
            break
        elif i-1==p:
            c=c+1
            p=i
    if c>0:
        s2+=str(c)+x
print(s2)