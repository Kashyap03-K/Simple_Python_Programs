i=2
f=0
n=int(input("Enter value for n"))
while i<n:
      if(n%i==0):
            print("NOT PRIME NUMBER")
            f=1
            i=n
      i+=1 
if(f==0):
      print("PRIME NUMBER")
