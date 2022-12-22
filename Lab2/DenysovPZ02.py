#Task 2
#Lowing dimentions
import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([1,-5]);
x2 = np.array([2,-6]);
x3 = np.array([3,-7]);
x4 = np.array([4, -8]);

w1=4
w2=4

x5 = np.array([-2, 3]);
x6 = np.array([-3, 4]);
x7 = np.array([-4, 5]);



m1 = (1/w1)*(x1+x2+x3+x4)
m2 = (1/w2)*(x5+x6+x7)

print("Среднее значение векторов класса 1:",m1)
print("Среднее значение векторов класса 2:",m2)

minus1=np.array([(x1-m1),(x2-m1),(x3-m1),(x4-m1)])
minus1_t=minus1.transpose()
s1 = np.dot(minus1_t,minus1)

minus2=np.array([(x5-m2),(x6-m2),(x7-m2)])
minus2_t=minus2.transpose()
s2 = np.dot(minus2_t,minus2)
s=s1+s2
w = np.around(np.dot((1/s),(m1-m2)),decimals = 1)
print("Матрица расброса векторов класса 1:",s1)
print("Матрица расброса векторов класса 2:",s2)
print("Матрица расброса векторов всей выборки:",s)
print("Линейный дискриминант:",w)

x1_ = np.dot(w,x1.reshape(2,1))
x2_ = np.dot(w,x2.reshape(2,1))
x3_ = np.around(np.dot(w,x3.reshape(2,1)),decimals=1)
x4_ = np.around(np.dot(w,x4.reshape(2,1)),decimals=1)
x5_ = np.dot(w,x5.reshape(2,1))
x6_ = np.around(np.dot(w,x6.reshape(2,1)),decimals=1)
x7_ = np.dot(w,x7.reshape(2,1))


print(x1_,"\n",x2_,"\n",x3_,"\n",x4_,"\n",x5_,"\n",x6_,"\n",x7_,"\n")
plt.title("Lab 2    v8")
plt.grid('blue',linestyle ='--',linewidth=0.5)
t=np.linspace(-5,5)
plt.plot(t,t,'hotpink',linewidth=2)

plt.plot(x1[0],x1[1],'p')
plt.annotate("X1",xy = (1,-5),xytext=(0.7,-5.6))
plt.plot(x2[0],x2[1],'p')
plt.annotate("x2",xy = (2,-6),xytext=(1.7, -6.7))
plt.plot(x3[0],x3[1],'p')
plt.annotate("x3",xy = (3,-7),xytext=(2.7,-7.7))
plt.plot(x4[0],x4[1],'p')
plt.annotate("x4",xy = (4,-8),xytext=(4.1,-7.9))
plt.plot(x5[0],x5[1],'p')
plt.annotate("x5",xy = (-2,3),xytext=(-1.7, 2.7))
plt.plot(x6[0],x6[1],'p')
plt.annotate("x6",xy = (-3,4),xytext=(-2.7, 3.7))
plt.plot(x7[0],x7[1],'p')
plt.annotate("x7",xy = (-4,5),xytext=(-3.7,4.7))

plt.plot(-0.2, -0.2, 'o m')
l1=np.linspace(-0.5,1)
l2=np.linspace(1,-5)
plt.plot(l1,l2,'lightblue',linestyle='--',linewidth=1)
plt.annotate('x1\'',xy=(-0.2, -0.2),xytext=(-0.5,0.4))

plt.plot(0.4, 0.5, 'o m')
l1=np.linspace(0.41,2)
l2=np.linspace(0.5,-6)
plt.plot(l1,l2,'lightblue',linestyle='--',linewidth=1)
plt.annotate('x2\'',xy=(0.4, 0.5),xytext=(0.3,1.1))

plt.plot(1, 1.1, 'o m')
l1=np.linspace(1.05,3)
l2=np.linspace(1,-7)
plt.plot(l1,l2,'lightblue',linestyle='--',linewidth=1)
plt.annotate('x3\'',xy=(1, 1.1),xytext=(0.8,2))



plt.plot(1.6, 1.67, 'o m')
l1=np.linspace(1.53,4)
l2=np.linspace(2,-8)
plt.plot(l1,l2,'lightblue',linestyle='--',linewidth=1)
plt.annotate('x4\'',xy=(1.6, 1.67),xytext=(1.6,2.2))

plt.plot(-1.1, -1.06, 'o c')
l1=np.linspace(-1.14,-2)
l2=np.linspace(-0.9,3)
plt.plot(l1,l2,'darkgray',linestyle='-',linewidth=1)
plt.annotate('x5\'',xy=(-1.1, -1.06),xytext=(-1.1,-1.8))


plt.plot(-1.76, -1.67, 'o c')
l1=np.linspace(-1.14,-2)
l2=np.linspace(-0.9,3)
plt.plot(l1,l2,'darkgray',linestyle='--',linewidth=1)
plt.annotate('x6\'',xy=(-1.76, -1.67),xytext=(-1.76,-2.5))


plt.plot(-2.4, -2.39, 'o c')
l1=np.linspace(-1.14,-2)
l2=np.linspace(-0.9,3)
plt.plot(l1,l2,'darkgray',linestyle='-',linewidth=1)
plt.annotate('x7\'',xy=(-2.4, -2.39),xytext=(-2.6,-3.2))


plt.show()
