import random
import matplotlib.pyplot as plt
import math
import time
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
def circle(list):
    list0=list
    num=[]
    for i in range(len(list)):
        num.append([i,0])
    count=0
    count1=0
    list2=[i for i in range(len(list))]
    while 1:
        list1=[]
        count=count+1
        for i in range(len(list)):
            if list2[list0[i]]==i and num[i][1]==0:
                num[i][1]=count
                count1=count1+1
            list1.append(list2[list0[i]])
        list2=list1
        if count1==len(list):
            break
    l=[]
    for i,e in num:
        if e not in l:
            l.append(e)
    count=[[i,0] for i in l]
    for i, e in num:
        for s in range(len(count)):
            if count[s][0]==e:
                count[s][1]=count[s][1]+1
    l=1
    for s in range(len(count)):
        l=lcm(l,count[s][0])
    return count,l

def average_order(num):
    N=0
    sum=0
    for i in range(len(num)):
        N=N+num[i][1]
        sum=sum+num[i][0]*num[i][1]
    return sum/N

def logistic(u,x0,M,N):
    x=x0
    list=[]
    for i in range(0,M):
        x=u*x*(1-x)
    for i in range(0, N):
        x = u * x * (1 - x)
        list.append(x)
    Disorder = [idx for idx, _ in sorted(enumerate(list), key=lambda x: x[1])]
    return Disorder

def Sine(a,x0,M,N):
    x = x0
    list = []
    for i in range(0, M):
        x = 4 / a * math.sin(math.pi*x)
    for i in range(0, N):
        x = 4 / a * math.sin(math.pi*x)
        list.append(x)
    Disorder = [idx for idx, _ in sorted(enumerate(list), key=lambda x: x[1])]
    return Disorder

def Cubic(a,x0,M,N):
    x = x0
    list = []
    for i in range(0, M):
        x = a*x*(1-x*x)
    for i in range(0, N):
        x = a*x*(1-x*x)
        list.append(x)
    Disorder = [idx for idx, _ in sorted(enumerate(list), key=lambda x: x[1])]
    return Disorder

def draw_pic(x,y,name):
    plt.figure()
    plt.plot(x, y, marker='.')
    plt.title(name)
    plt.xlabel("N")
    plt.ylabel("average_order")
    plt.show()

time1 = time.time()
u=3.7#3.57-4
M=1000
seedsize=100
Nsize=100

x= []
y =[]
order=[]
for N in range(1,Nsize):
    for i in range(0,seedsize):
        x0=random.random()
        list=logistic(u,x0,M,N)
        count,l=circle(list)
        order.append(average_order(count))
    x.append(N)
    y.append(sum(order)/len(order))

draw_pic(x,y,"N-average_order imagation(logistic)")

time2 = time.time()

a=4#一般为4
M=1000
seedsize=100
Nsize=100

x= []
y =[]
order=[]
for N in range(1,Nsize):
    for i in range(0,seedsize):
        x0=random.random()
        list=Sine(a,x0,M,N)
        count,l=circle(list)
        order.append(average_order(count))
    x.append(N)
    y.append(sum(order)/len(order))

draw_pic(x,y,"N-average_order imagation(Sine)")

time3 = time.time()

a=2.595#一般为2.595
M=1000
seedsize=100
Nsize=100

x= []
y =[]
order=[]
for N in range(1,Nsize):
    for i in range(0,seedsize):
        x0=random.random()
        list=Cubic(a,x0,M,N)
        count,l=circle(list)
        order.append(average_order(count))
    x.append(N)
    y.append(sum(order)/len(order))

draw_pic(x,y,"N-average_order imagation(Cubic)")

time4 = time.time()
print(f"logistic运行时间:{time2-time1}s,Sine运行时间:{time3-time2}s,Cubic运行时间:{time4-time3}s,总运行时间:{time4-time1}s")