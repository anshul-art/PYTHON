import matplotlib.pyplot as  plt
import numpy as np
x = [0,1,2,3,4,5]
y = [0,2,4,6,8,10]
p = [12,3,13,17,22,15]
q = [11,2,12,16,21,14]
plt.figure(figsize=(5,3),dpi=100)
plt.plot(x,y, label='2x', color='red', linewidth=2, marker='.',markersize=6, linestyle='--',markeredgecolor='blue')
plt.title('First Graph', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})

plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.xticks([0,1,2,3,4,5]) #actual points on the x-axis
plt.yticks([0,2,4,6,8,10]) #actual points on the y-axis
plt.legend()
plt.savefig('graph.png', dpi=200)
plt.show()


#OR
#'[color][marker][line]'
plt.figure(figsize=(8,4),dpi=100) 
plt.plot(x, 'co-', label='2x', marker='o',ms=6,mec='k',mfc='w',linewidth=5) #ms=marker size,mec=marker color,mfc=marker face color
plt.plot(y, 'ko-', label='2x', marker='o',ms=6,mec='k',mfc='w',linewidth=5)
plt.title('First Graph', fontdict={'fontname':'Comic Sans MS', 'fontsize':20,},loc='center')#can be left and right too
plt.xlabel('NO. OF STUDENTS',fontdict={'family':'serif','fontname':'Comic Sans MS', 'fontsize':10})
plt.ylabel('NO. OF BISCUITS',fontdict={'family':'serif','fontname':'Comic Sans MS', 'fontsize':10})
plt.legend()
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()


plt.subplot(1,2,1)
plt.subplot(1,2,2)
plt.plot(x, 'co-', label='2x', marker='o',ms=6,mec='k',mfc='w',linewidth=5) #ms=marker size,mec=marker color,mfc=marker face color
plt.plot(y, 'ko-', label='2x', marker='o',ms=6,mec='k',mfc='w',linewidth=5)
plt.title('First Graph', fontdict={'fontname':'Comic Sans MS', 'fontsize':20,},loc='center')#can be left and right too
plt.xlabel('NO. OF STUDENTS',fontdict={'family':'serif','fontname':'Comic Sans MS', 'fontsize':10})
plt.ylabel('NO. OF BISCUITS',fontdict={'family':'serif','fontname':'Comic Sans MS', 'fontsize':10})
plt.legend()
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()

#subplot order (1row,2column,order of plot(1or2))
x = [0,1,2,3,4,5]
y = [0,2,4,6,8,10]
plt.figure(figsize=(8,4),dpi=100) 
plt.subplot(1, 2, 1)
plt.plot(x,y, 'co-', label='2x', color='red', linewidth=2, marker='.',markersize=6,     markeredgecolor='blue')
p = [12,3,13,17,22,15]
q = [11,2,12,16,21,14]
plt.subplot(1,2,2)
plt.plot(p,q, 'co-', label='2x', color='red', linewidth=2, marker='.',markersize=6,     markeredgecolor='blue')
plt.show()


plt.plot(p, 'co-', label='2x', color='red', linewidth=2, marker='.',markersize=6, markeredgecolor='blue')
plt.plot(q, 'co-', label='2x', color='red', linewidth=2, marker='.',markersize=6, markeredgecolor='blue')
plt.show()


plt.figure(figsize=(8,4),dpi=100) 
plt.subplot(2,2,1)
plt.plot(x, 'co-', label='2x', color='red', linewidth=2, marker='.',markersize=6,   markeredgecolor='blue')
plt.plot(y, 'co-', label='2x', color='red', linewidth=2, marker='.',markersize=6,   markeredgecolor='blue')
plt.subplot(2,2,2)
plt.plot(p, 'co-', label='2x', color='red', linewidth=2, marker='.',markersize=6,   markeredgecolor='blue')
plt.plot(q, 'co-', label='2x', color='red', linewidth=2, marker='.',markersize=6,   markeredgecolor='blue')
plt.subplot(2,2,3)
a = [10,20,30,40,50,60]
b = [5,15,25,35,45,55]
plt.plot(a, 'co-', label='2x', color='red', linewidth=2, marker='.',markersize=6,   markeredgecolor='blue')
plt.plot(b, 'co-', label='2x', color='red', linewidth=2, marker='.',markersize=6,   markeredgecolor='blue')
plt.subplot(2,2,4)
k = [3,6,9,12,15,21]
l = [9,18,27,36,45,54]
plt.plot(k, 'co-', label='2x', color='red', linewidth=2, marker='.',markersize=6,   markeredgecolor='blue')
plt.plot(l, 'co-', label='2x', color='red', linewidth=2, marker='.',markersize=6,   markeredgecolor='blue')
plt.show()

#Scatter 

plt.scatter(x, y)
plt.show()

#comparing and colouring each dot
c = np.array(['Red','Green','Hotpink','blue','Yellow','Black'])
#p = [12,3,13,17,22,15]
#q = [11,2,12,16,21,14]

plt.scatter(x,y,color=c)
plt.scatter(p,q,color=c)
plt.show()

#colormap = here a value point is needed based on the no.of values in these case it is 6
colors = np.array([0,20,40,60,80,100]) #purple at zero and yellow at 100
plt.scatter(a,b,c=colors, cmap='viridis')
plt.scatter(k,l,c=colors, cmap='viridis')
plt.colorbar()
plt.show()

sizes = np.array([20,40,60,80,100,120])
plt.scatter(a,b, s=sizes,c=colors, cmap='viridis',alpha=0.5) #alpha indicates the opacity
plt.scatter(k,l, s=sizes,c=colors, cmap='viridis',alpha=0.5)
plt.colorbar()
plt.show()

#Bar gragh

m = np.array(["A", "B", "C", "D"])
n = np.array([3, 8, 1, 10])
plt.bar(m,n,color='black',width=2.1)
plt.show()
#HORIZONTAL BAR = In horizontal bar use Height instead of width
m = np.array(["A", "B", "C", "D"])
n = np.array([3, 8, 1, 10])
plt.barh(m,n,color='black',height=2.1)
plt.show()

#PIE CHART = it starts from x-axis and moves in anti-clock direction 

f = np.array([35,15,20,25])
plt.pie(f) 
plt.show()
#label,shadow and explode(deattach)
milabel = np.array(['Apple','Banana','Orange','Grapes'])
miexplode = np.array([0.2,0,0,0])
plt.pie(f,labels=milabel,explode=miexplode,shadow=True)
plt.legend()
plt.show()

#label title,shadow and color

micolor = np.array(['Black','Pink','Blue','Red'])
plt.pie(f,labels=milabel,shadow=True,colors=micolor)
plt.legend(title = "Fruits")
plt.show()
#startangle perpendicular to 360, in x axis = 0, y axis=180,
plt.pie(f,labels=milabel,shadow=True,colors=micolor,startangle=90)
plt.show()