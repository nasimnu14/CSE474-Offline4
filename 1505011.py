import random 
import pandas
def noise(mean=0,var=0.01):
    a=random.normalvariate(mean,var)
    return a
def channelOutput(h,Ik,Ik1):
    a=h[0]*Ik+h[1]*Ik1+noise()
    return a
if __name__ == '__main__':
    train=open("train.txt","r")
    train=train.read()
    parameter=open("parameter.txt","r")
    param=parameter.readline().split()
    mean=float(param[0])
    var=float(param[1])
    param=parameter.readline().split()
    h1=float(param[0])
    h2=float(param[1])
    h=[h1,h2]
    Ik1=0
    Ik2=0
    xk1=channelOutput(h,Ik1,Ik2)
    print(xk1)
    l=len(train)
    for i in range(0,l):
        Ik=int(train[i])
        xk=channelOutput(h,Ik,Ik1)
        

        Ik2=Ik1
        Ik1=Ik
        xk=xk1

