n=int(input("Enter number of elements till which Fibonacci series is to be Run "))
a=0
b=1
print(a)
print(b)
for i in range(1,n-1):
      c=a+b
      print(c)
      a,b=b,c
 
