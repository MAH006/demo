#frequencies of word in string
a=input("enter any string:")
arr=a.split(" ")
d1={}
d2={}
for x in arr:

    c=arr.count(x)
    d1[x]=c
for y in d1:
    d=len(y)
    d2[y]=d
print(d2)