print("=================== replace() ====================")
s1="this is demo.this is string program"
print(s1)
s1=s1.replace("is","IS",3)
print(s1)
print("=================== join() ====================")
mylist=["hello","world" ]
s1=""
for x in mylist:
    s1+=" "+x
print(s1.strip())
print("=================== just() ====================")
s1="hello world"
print(s1)
print(s1.center(50,'*'))
print(s1.ljust(50,'*'))
print(s1.rjust(50,'*'))
print("========================================")
s1="this is DEMO"
print(s1.capitalize())
print(s1.lower())
print(s1.upper())
print(s1.swapcase())
print(s1.title())


