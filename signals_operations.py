import matplotlib.pyplot as plt
import math

#THE FUNCTIONS         

def signal_input():
    origin = int(input("Position of Origin signal : "))
    length = int(input("Length of the signal : "))
    y = []
    print("Enter the signal values : ")
    for i in range(0,length):
        y.append(int(input()))
    x = []
    for i in range(1-origin,length+(1-origin)):
        x.append(i)
    return x,y,origin
#returns x,y axis values as list and origin - origin position

def plotting(a,b,title,yaxis):
    plt.stem(a,b)
    plt.xlabel('n')
    plt.ylabel(yaxis)
    plt.title(title)
    plt.show()

    #takes x,y values and plots

def reverse_signal(x,y,origin):
    y1=[]
    for i in x:
        y1.append(-1*i)
    y1.sort()
    x1=list(y[::-1])
    origin1=len(x1)-origin+1
    return y1,x1,origin1
#takes x,y axis values and origin position
#returns reversed x,y and new origin position

def add_signal(x1,x2,origin_x1,origin_x2):
    diff_origin = max(origin_x1,origin_x2) - min(origin_x1,origin_x2)
    test_1=[]
    test_2=[]
    if origin_x1 > origin_x2:
        for i in range(0,diff_origin):
            test_1.append(0)
        for i in x2:
            test_1.append(i)
        test_2=x1
        origin_x2+=diff_origin
    elif origin_x1 < origin_x2:
        for i in range(0,diff_origin):
            test_2.append(0)
        for i in x1:
            test_2.append(i)
        test_1=x2
        origin_x1+=diff_origin
    else:
        test_2=x1
        test_1=x2
    if len(test_2) < len(test_1):
        d = len(test_1) - len(test_2)
        for i in range(0,d):
            test_2.append(0)
    elif len(test_1) < len(test_2):
        d = len(test_2) - len(test_1)
        for i in range(0,d):
            test_1.append(0)
    result_x2 = []
    if len(test_2)==len(test_1):
        for i in range(0,len(test_2)):
            a = test_2[i]+test_1[i]
            result_x2.append(a)
    result_x1 = []
    for i in range(1-origin_x1,len(result_x2)+(1-origin_x1)):
        result_x1.append(i)
    return result_x1,result_x2
#takes 2 signales y1 and y2 and their starting position
#retutns final added signal's x,y axis values

def scale_signal(y_n,origin,multiplefactor):
    test1 = []
    for i in range(1-origin,len(y_n)+(1-origin)):
        test1.append(i)
    result_x = []
    result_y = []
    for i in range(0,len(test1)):
        c = test1[i]/float(multiplefactor)
        if math.floor(c)==math.ceil(c):
            result_x.append(int(c))
            result_y.append(y_n[i])
    if len(result_x)>1:
        if result_x[1]!=result_x[0]+1:
            c=len(test1)-1 
            j=1
            s=[]
            while j<=c:
                s.append(j)
                j+=2
                c+=1
            for i in s:
                result_x.insert(i,result_x[i-1]+1)
                result_y.insert(i,0)
    for i in range(0,len(result_x)):
        if result_x[i]==0:
            origin=i+1
            break
    return result_x,result_y,origin

#takes signal,starting position and scaline unit
#returns scaled signal axis and changed starting position

#MAIN PROGRAM

#n1=[-3,-2,-1,0,1,2,3]
#x_n=[2,-2,1,0,1,-1,2]
#n2=[-3,-2,-1,0,1]
#y_n=[2,1,-2,2,3]
#origin_position1=4
#origin_position2=4

n1,x_n,origin_position1=signal_input()
n2,y_n,origin_position2=signal_input()

print("input informations")
print("n1=",n1)
print("x_n=",x_n)
print("n2=",n2)
print("y_n=",y_n)

#QUESTION NO 6 22BEE0063 RAJAGOPAL.B
# question number 1
print("Question number 1")
n21,y_n1,b1=reverse_signal(n2,y_n,origin_position2)
plotting(n21,y_n1,"reverse y(n) 22BEE0063","y(-n)")
print("n=",n21,"y(-n)",y_n1)

n111,x_n11,a11=scale_signal(x_n,origin_position1,2)
plotting(n111,x_n11,"scale of x(n) 22BEE0063","x(2n)")
print("n=",n111,"x(2n)",x_n11)

print("result")
x,y=add_signal(x_n11,y_n1,a11,b1)
print("n=",x)
print("y(-n)+x(2n)=",y)
plotting(x,y,"result(i) 22BEE0063","y(-n)+x(2n)")

#question number 2
print("Question number 2")
n11,x_n1,a1=reverse_signal(n1,x_n,origin_position1)
plotting(n11,x_n1,"reverse x_n 22BEE0063","x(-n)")
print("n=",n11,"x(-n)=",x_n1)

n211,y_n11,b11=scale_signal(y_n,origin_position2,0.5)
plotting(n211,y_n11,"scale y_n 22BEE0063","y(0.5n)")
print("n=",n211,"y(0.5n)=",y_n11)

print("result")
x1,y1=add_signal(x_n1,y_n11,a1,b11)
print("n=",x1)
print("x(-n)+y(0.5n)=",y1)
plotting(x1,y1,"result(ii) 22BEE0063","x(-n)+y(0.5n)")





