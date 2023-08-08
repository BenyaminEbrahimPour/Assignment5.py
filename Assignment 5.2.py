from cmath import sqrt
def moadele():
    a=float(input("::"))
    b=float(input(":"))
    c=float(input(":"))
    delta=b**2-4*a*c
    if delta>=0:
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b-sqrt(delta))/(2*a)
        if x1==x2:
            print(x1)
        else:
            print(x1,x2)
    else:
        print("There is no answer!!!")
moadele()
moadele()
moadele()       
  



