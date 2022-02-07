#frequencies of words in string
a=input("enter any string:")
arr=a.split(" ")
d1={}

for x in arr:

    c=arr.count(x)
    d1[x]=c
print(d1)