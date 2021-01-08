E=0
P=int(input("Principal amount"))
R=int(input("Rate of interest"))
n=int(input("tenure of loan in months"))
E=P*R*(1+R)**n/((1+R)**n -1)
print('EMI',E)
