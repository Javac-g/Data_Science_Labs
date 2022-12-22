#Task 3
#Divide by 3 clasters
import numpy as np
import matplotlib.pyplot as plt
import math
x1 = np.array([0.7,0.6,-0.4])
x2=np.array([0.5,-0.9,0.7])
x3=np.array([-1.1,0.4,-1.4])
x4=np.array([0.1,1.3,-0.5])
x5=np.array([-0.8,-1.4,0.2])
x6=np.array([-0.3,0.2,0.6])
A = np.array([x1,x2,x3,x4,x5,x6])
ax = plt.axes(projection='3d')
ax.set_title('Lab3')

def showInput():
	xNum =A[:,0]
	yNum =A[:,1]
	zNum=A [:,2]
	ax.plot_trisurf(xNum,yNum,zNum,cmap='inferno',edgecolor='none')
	ax.scatter((xNum,yNum,zNum,s=150,c=zNum,cmap='inferno',linewidth=5)
	ax.set_xlabel('X-axis')
	ax.set_ylabel('Y-axis')
	ax.set_zlabel('Z-axis')
showInput()
plt.show()

w=np.array(([0.5,0.2,-0.6],[0.7,-0.1,0.4],[0.3,-0.6,0.8]))
k=0.5

def calculation(W,x,color):
	d1 =np.around((pow((x[0]-w[0][0]),2)+pow((x[1]-w[1][0],2)+pow((x[2]-w[2][0],2)),decimals=5)
	d2 =np.around((pow((x[0]-w[0][1]),2)+pow((x[1]-w[1][1],2)+pow((x[2]-w[2][1],2)),decimals=5)
	d3 ==np.around((pow((x[0]-w[0][2]),2)+pow((x[1]-w[1][2],2)+pow((x[2]-w[2][2],2)),decimals=5)
	netj1 =np.around(np.dot(x[0],w[0][0])+np.dot(x[1],w[1][0])+np.dot(x[2],w[2][0]),decimals =5)
	netj2=np.around(np.dot(x[0],w[0][1])+np.dot(x[1],w[1][1])+np.dot(x[2],w[2][1]),decimals =5)
	netj3 = =np.around(np.dot(x[0],w[0][2])+np.dot(x[1],w[1][2])+np.dot(x[2],w[2][2]),decimals =5)
	darr=np.array([d1,d2,d3])
	print(darr)
	jarr = np.array([netj1,netj2,netj3])
	print(jarr)
	minNumIndex =np.argmin(darr)
	minNum = Jarr[minNumIndex]
	minDistance = darr[minNumIndex]
	y=np.around(math.sin(minNum), decimals=3)
	plt.title('clusters')
	plt.grid('black',linestyle='--',linewidth=0.5
calculation(W,x1,'purple')	
w1 =np.around(w+k*(x1-w),decimals=2)
k/=2
calculation(w1,x2,'magenta')
w2=np.around(w1+k*(x2-w1),decimals=2)
k/=2
calculation(w2,x3,'magenta')
w3=np.around(w2+k*(x3-w2),decimals=2)
k/=2
calculation(w3,x4,'magenta')
w4=np.around(w3+k*(x4-w3),decimals=2)
k/=2
calculation(w4,x5,'magenta')
w5=np.around(w4+k*(x5-w4),decimals=2)
k/=2
calculation(w5,x6,'magenta')
w6=np.around(w5+k*(x6-w5),decimals=2)
k/=2
