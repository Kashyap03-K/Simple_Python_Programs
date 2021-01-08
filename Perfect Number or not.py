'''
Write a program to check whether a number is Perfect Number or not.
[What is perfect Number ? --> If the sum of factors of the number N (excluding N)is equal to the number itself it is a perfect number.
 Ex: Factors of 6 =1,2,3 and 1+2+3=6  ,6 is a perfect number]
'''
n=int(input("Enter any number"))
s=0
for i in range(1,n):
         if n%i==0:
               s=s+i
               print(s)   
if s==n:
         print(n,"is a Perfect Number")
else:
         print(n,"is not a Perfect Number")
