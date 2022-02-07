sl=[1,2,3,4,5,6,7]
n=len(sl)
temp = sl[0]
sl[0] = sl[n-1 ]
sl[n-1 ] = temp
print(sl)
print("==========================================")
sl=[1,2,3,4,5,6,7]
n=len(sl)
print(sl)
#i=int(input("enter element you want to change:"))
#j=int(input("enter element you want to change with:"))
#if i<n and j<n:
 #   temp = sl[i]
  #  sl[i] = sl[j]
   # sl[j] = temp
#else:
 #   print("invalid no to change")
#print(sl)
print("==========================================")
sl=[1,2,3,4,5,6,7]
print(sl)
sum=0
for x in sl:
    sum+=x
print("sum of elemennts in list is=",sum)
print("==========================================")
sl=[1,2,3,4,5,6,7]
print(sl)
mul=1
for x in sl:
    mul=mul*x
print("multiplication of elemennts in list is=",mul)
print("==========================================")
sl=[1,2,3, 9,69,98,4,5,6,7]
print(sl)
sl=sl.sort(reverse=1)
print(sl)
print("largest no among list is =",sl[1])