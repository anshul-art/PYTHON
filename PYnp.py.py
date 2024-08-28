import numpy as np
a = np.array([[1,2,3,4,5],[6,7,8,9,0]], dtype=int)
print(a)
print(a.ndim) #gives the dimension
print(a.shape) #gives the shape
print("array of a: ",np.sum(a))
print(a.dtype) #tells the type
print(a.size) #tells how many elements are there
print(a.itemsize) #tells size in bytes of each element
print(a.itemsize * a.size)
print(a.nbytes)
b = a[1,4]
print(b)
c = a[1,:] # here , colon stands for all the remaning columns included
d = a[:,0] #here , colon stands for all the rows included
print(c)
print(d)
e = a[1, 1:-1]
print(e)
f = np.zeros((4,8)) #will make an array consisting of zeroes only with 4 rows and 8 columns
print(f)
print(f.shape)
print(f.dtype) #tells the type
print(f.ndim)
g = np.ones((4,8)) # does the same as zeroes,but replace zeroes with ones
print(g)
print(g.shape)
print(g.ndim)
print(g.dtype)
h = np.arange(20) #prints from 0 to -1 , it is not a list it as a numpy array
print(h)
i = np.linspace(1,100,8) #prints equally distant elements from each other  (starting no. , ending no. , no. of elments wanted)
print(i)
j = np.linspace(1,50,3)
print(j)
k = np.empty_like((4,6)) #gives random elments of (rows,columns)
print(k)
l = np.empty_like(f) #exact copy
print(l)
m = np.identity(45)  #gives identity of 45*45 matrix
print(m)
print(m.shape)
n = np.arange(100)
print(n)
o = n.reshape(2,50) #the border value multiplies then gives output if the multiplication isnt correct it will not give output 
#it reshapes our array  (no. of array wants , no. of elments want in an array)
print(o)
p = n.ravel()#the divided list will get become 1-D list again and the shape will also become 1-D
print(p)
print(p.shape)


#NUMPY AXIS = 1-D is has only axis = 0 axis 
# 2-D = has 2 axis = 0 axis and 1 axis  take it as like a x and y of graphs
#When taking a random array   [1,2,3]  [6]      the upper line is axis 1 (horizontal) we can also call it columns
#                             [5,6,7]  [18]     the side line is axis 0 (vertical) we can also call it rows 
#                             [9,8,4]  [21]    the sum of axis 0  will be=
#                             [15,16,14]
q = [1,2,3],[5,6,7], [9,8,4]
r = np.array(q)
print(r)
print(r.sum(axis=0)) #gives the sum of  axis 0
print(r.sum(axis=1)) #gives the sum of  axis 1
print(r.T) #it transposes the array(to change the order of two or more things)
s = r.flat
for items in r.flat:
    print(items)

#Accessing in 1-D array
t = np.array([1,3,8,242,0])
print(t.argmax()) #it gives the index of the highest element
print(t.argmin()) #it gives the index of the lowest element 
print(t.argsort()) #Returns the indices(index) that would sort an array. 

#Accessing in 2-D array
print(r)
print(r.argmax(axis=0)) #The first column of axis 0 has highest element in 2nd index similarly, the second column has highest element in 2nd index and the third column has the highest element in 1st position
print(r.argmin(axis=1)) #The first row of axis 1 has lowest element in 0th  index similarly, the second row  has lowest element in 0th index and the third row has the lowest element in 2nd position
print(r.argsort())
print(r.argsort(axis=0))
print(r.argsort(axis=1))

u = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

v = np.array([[1,4,7],
              [3,5,8,],
              [2,6,9]])
print(v.ndim)
print(u.ndim)
x = (u+v)
print(x)
print(u-v)
print(u*v)
print(u/v)
print(np.sqrt(x)) #gives the square root 
print(np.count_nonzero(x)) #counts the non-zero elements
print(np.nonzero(x)) 

#STATISTICAL FUNCTIONS

# 1) MEDIAN FUNCTION = Gives the middle element
y = np.array([1,3,4,5,6])
print(np.median(y)) #middle element of the 1-D array
z = np.array([[1,3,4],
              [2,6,7],
              [8,0,7,]])
print(np.median(z)) #Middle element of whole   2-D array 
print(np.median(z, axis=0))
print(np.median(z, axis=1))

#2) MEAN FUNCTION = GIVES THE AVERAGE OF ELEMENTS (Addition of all elements divided by No. of elements)

print(np.mean(y)) #gives the average of 1-D element 
print(np.mean(z)) #gives the average of 2-D element
print(np.mean(z, axis=0)) 
print(np.mean(z, axis=1))

#3) STANDARD DEVIATION = The standard deviation is a measure of the spread of the data in the array. It gives us the degree to which the data points in an array deviate from the mean.

#Smaller standard deviation indicates that the data points are closer to the mean
#Larger standard deviation indicates that the data points are more spread out.

print(np.std(y))
print(np.std(z))
print(np.std(z, axis=0))
print(np.std(z, axis=1))

#4) PERCENTILE
print(np.percentile(y, 25))
print(np.percentile(z, 75))

#5) MIN AND MAX
print(np.min(y))
print(np.max(z))

# COMPARISON / LOGICAL OPERATORS = deals with boolean values

y = np.array([1,3,4,5,6])
aa = np.array([2,4,1,2,8])
print(y > aa) #will print true if y is greater than aa
print(aa > y) #will print true if aa is greater than y
print(np.less(y,aa)) #checks if first variable is lesser than the other
print(np.less_equal(y,aa)) 
print(np.greater(y,aa))
print(np.greater_equal(y,aa))
print(np.equal(y,aa))
print(np.not_equal(y,aa))

bb = np.array([True,False,True])
cc = np.array([False,False,True])
print(np.logical_and(bb,cc))# checks if both the array are True
print(np.logical_or(bb,cc)) #checks if one of the arrays is true
print(np.logical_not(bb,cc)) #checks if the arrays are false

#MATH FUNCTIONS
print(r)
print(r.sum(axis=0)) #gives the sum of  axis 0
print(u)
print(v)
x = (u+v)
print(x)
print(u-v)
print(u*v)
print(u/v)

#*Trignometric functions
dd = np.array([1,3,5])
print(np.sin(dd)) #prints sin of the dd array
print(np.arcsin(dd)) #prints inverse of the dd array
#others trignometric ratios : 
#cos = gives cos the array
#tan = gives tan the array
#arccos = gives inverse of the cos array
#arctan =  gives inverse of the tan array
#degrees = 	converts an angle in radians to degrees
#radians =	converts an angle in degrees to radians

some = 23
print(np.degrees(some))
print(np.radians(some))
#we can also convert degree into radians and radians into degrees

#* Rounding functions
ee = np.array([1.2234,2.3435,3.453])
print(np.round(ee,2))  # 2 - denotes the number of decimal places to which the array is rounded
print(np.floor(ee)) # rounds down to the nearest integer = = returns the values of array down to the nearest integer that is less than each element
print(np.ceil(ee)) #rounds up to the nearest integer = = returns the values of array up to the nearest integer that is greater than each element.

#np.exp = np.e * 1
print(ee + np.pi) #pi = value of pi

#STRING FUNCTIONS

ff = np.array(['iPhone: ', 'price: '])
gg = np.array(['15', '$900'])
print(np.char.add(ff,gg)) #Adds both the string arrays
print(np.char.multiply(ff,2)) #Multiplys the arrays to itself = 2 denots 2 times
print(np.char.capitalize(ff))
print(np.char.upper(ff))
print(np.char.lower(ff))
print(np.char.join('-',ff)) #will join the array with "-"/desired symblos or anything  in between
hh = (['ghost','portal','spirit'])
ii = (['revive','door','spirit'])
print(np.char.equal(hh,ii))#Returns true/false values after comparing they are equal or not

#BROADCASTING = An array with a smaller shape is expanded to match the shape of a larger one. This is called broadcasting.
#NumPy compares a set of array dimensions from right to left.
#Rules = 1)one of them has a length of 1 or 
#        2) they are equal
jj = np.array([1,2,3]) #1-D
kk = np.array([[1],[2],[3]]) #2-D
print(jj+kk) #first it adds the 0th index of 1-D array to all the 2-D  arrays similarly after adding them up the 1st index of 1-D array adds with 1st index of 2-D array,similarly with the rest 
ll = 5
print(jj+ll) #performs similarly as the upper 
#last index needs to be empty,1 or same to do broadcasting between two arrays

#NumPy Matrix Operations
mm = np.array([[2,6], #This is 2x2 matrix
              [4,8]]) 
nn = np.array([[1,2,3], #This is 3x3 matrix
               [4,5,1],
               [2,3,4]])
oo = np.array([[1,3],
              [5,7]])
print(np.dot(mm,oo)) #prints multiplication of both matrix
print(np.transpose(oo)) #The transpose of a matrix is a new matrix that is obtained by exchanging the rows and columns.
print(np.linalg.inv(nn)) #calculates inverse of matrix
#Only square matrices that have a non-zero determinant have an inverse.
print(np.linalg.det(nn)) # finds determinant of matrix
print(nn.flatten()) #prints the matrix into 1-D array
print(mm.ndim)

#NUMPY SET OPERATIONS

#A set is a collection of unique data. That is, elements of a set cannot be repeated.
#NumPy set operations perform mathematical set operations on arrays like union, intersection, difference, and symmetric difference.

pp = np.array([1, 3, 5])
qq = np.array([0, 2, 3])
print(np.union1d(pp,qq))  #joins the array excluding the common value in both of them
print(np.intersect1d(pp,qq)) #gives the common value of both the arrays
print(np.setdiff1d(pp,qq)) #gives the value in which are not present in the other array(in this case it is according to pp)
print(np.setdiff1d(qq,pp)) #gives the value in which are not present in the other array(in this case it is according to qq)
print(np.setxor1d(pp,qq)) #gives the output excluding common value
rr = np.array([0,1,1,2,2,5,4,4,7,0,9])
print(np.unique(rr)) #gives a sorted and unique list of array

#NUMPY VECTORIZRTION 
#NumPy vectorization involves performing mathematical operations on entire arrays, eliminating the need to loop through individual elements.

ss = 10
print(rr + ss) #10 will be added to all the elements in an array,this is bcz of vectorization

def find_square(x):
    if x < 0:
        return 0
    else:
        x ** 2
to_vectorize = np.vectorize(find_square) 
result = to_vectorize(rr)
print(result)
#VECTORIZTION IS MORE FAST THAN PYTHON,HELPS IN DEALING WITH LARGE DATASETS

#NUMPY BOOLEAN INDEXING
#We use boolean masks to specify the condition.
tt = np.array([1,2,4,6,67,34,45,23,32])
print(tt > 10) #prints greater than 10
print(tt  % 2 != 0) #prints odd number
print(tt % 2 == 0) #prints even number
print(tt > 5 , tt < 50) 
boolean_mask = (tt >5) | (tt < 50) #both methods are correct
resultt = tt[boolean_mask] #method to get a number value
print(resultt)
uu = np.array([[1, 7, 9], 
                    [14, 19, 21], 
                    [25, 29, 35]])
print(uu < 20) #smaller  than 20
print(tt)

#NUMPY FANCY INDEXING
#In NumPy, fancy indexing allows us to use an array of indices to access multiple array elements at once.
vv = np.array([1,4,5,6,7,8,3,56,3])
selected1 = vv[7]
print(selected1)
selected2 = vv[[7,3,2]]
print(np.argsort(vv)) #in ascending order
print(np.argsort(-vv)) #in descending order
indices = [2,3,4]
new_values = [45,23,43]
vv[indices] = new_values
print(vv)
ww = np.array([[1,2,3],
               [4,5,6],
               [5,6,9]])
selected_rows = np.array([0,2])
row_indicies = ww[selected_rows, :]
print(row_indicies)

#NUMPY RANDOM
print(np.random.randint(0,10)) #prints random integer between 0 and 10
print(np.random.rand()) #prints random float between 1 and 0
print(np.random.randint(0,101,10)) #will print 10 random integers
print(np.random.rand(5)) #will print 5 random values
print(vv)
print(np.random.choice(vv,3))
print(np.random.randint(0,101,(3,3))) #will give an 2-D array between 0 and 100

#NYUMPY LINEAR ALGEBRA
#Linear algebra deals with mathematical concepts related to linear equations and their representations using matrices.

xx = np.array([1, 3, 5])
yy = np.array([2, 4, 6])
print(np.dot(xx,yy)) #gives product of both the matricies  1*2 + 3*4 + 5*6 = 44.
aaa = np.array([[1, 3], 
                   [5, 7]])
bbb = np.array([[2, 4], 
                   [6, 8]])
print(np.inner(aaa,bbb)) #prints sum of the products of their corresponding entries. 1*2+3*4     1*6+3*8    5*2+7*4         5*6+7*8
print(np.outer(xx,yy)) #product of all possible pairs of their entries. 1*2      1*4       1*6  ,   3*2      3*4       3*6  ,  5*2      5*4       5*6
print(np.linalg.det(aaa)) #calculate the determinant of a square matrix. 
ccc =   np.array([[2, 4], 
             [6, 8]])
ddd = np.array([5, 6])
print(np.linalg.solve(ccc,ddd)) #For a given matrix A and a vector b, solve(A, b) finds the solution vector x that satisfies the equation Ax = b.  Here, the output is [-2. 2.25], which is the solution to the system of linear equations 2x + 4y = 5 and 6x + 8y = 6.
print(np.linalg.inv(aaa)) #inverse of square matrix
eee = np.array([[6, 3, 5], 
                   [9, 2, 1], 
                   [7, 8, 4]])
print(np.trace(eee))#the sum of the diagonal elements of a matrix. 

# HISTOGRAM
data = np.array([1,6,21,12,18,20,23])
bins = [0,10,20,30] #intervals
print(np.histogram(data,bins)) #will see the array according to intervals(between 0 and 10 = 2 elements)
from matplotlib import pyplot as plt
plt.hist(data,bins)
plt.show()

#INTERPOLATION
#In NumPy, interpolation estimates the value of a function at points where the value is not known.

day = np.array([2, 4, 7])
gold_price = np.array([55, 58, 65])
day3_value = np.interp(3, day, gold_price)
print(day3_value)
interpolate_days = np.array([1, 3, 5, 6, 8, 9])

interpolated_price= np.interp(interpolate_days, day, gold_price)
print(interpolated_price)
ggg = np.array([0, 1, 2, 3, 4, 5])
fff = np.array([0, 3, 4, 5, 7, 8]) 
x_interp = np.linspace(ggg.max(),ggg.min(),100)
y_interp = np.interp(x_interp, ggg, fff)
plt.plot(ggg, fff, 'bo')
plt.plot(x_interp, y_interp, 'r-')

plt.show()

#FILES

array1 = np.array([[2, 4, 6], 
                  [8, 10, 12]])
#np.save('file1.npy', array1) (FILE NAME,ARRAY NAME)
#print(np.load(file1.npy)) loads a file
array2 = np.array([4, 8, 12])
#np.savez('file2.npz', file1 = array1, file2 = array2) saves multiple files
#To load multiple data first normallly load the file then gives a name to the arrays and print it
#load = np.load(xyx.npy) all the arrays from this file will be loaded
#array1 = load_data['file1']
#array2 = load_data['file2']
#print both the array


#ERROR HANDLING
#divide: specifies the behavior for division by zero or infinity
np.seterr(divide='raise')
array3 = np.array([1, 2, 3])
array4 = np.array([0, 2, 0])
#result1 = np.divide(array3,array4)
#print(result1)
#over: specifies the behavior for floating-point overflow
#under: specifies the behavior for floating-point underflow
#np.seterr(over='raise')
#calc1 = np.exp(1000)
#print(calc1)#because the result of the calculation is too large to be represented by the floating-point data type.
#invalid: specifies the behavior for invalid floating-point operations such as 0/0, inf-inf, and sqrt(-1)
#np.seterr(invalid='raise')
#x = np.sqrt(-1)
#try:
    # code that may cause exception
#except:
    # code to run when exception occurs

#try:
#   result = array3/array4

#except ZeroDivisionError as e:
#    print("Error: Cannot divide by zero")    

#DATE AND TIME
#The datetime64() function in Numpy stores date and time information as a 64-bit integer datetime64 object.

dt = np.datetime64('now')
print(dt)
donly = np.datetime64('today','D')
print(donly)
tonly = np.datetime64('now','h')
year = np.datetime64('2023', 'Y')
month = np.datetime64('2023-04', 'M')
day = np.datetime64('2023-04-29', 'D')
hour = np.datetime64('2023-04-29T10', 'h')
minute = np.datetime64('2023-04-29T10:30', 'm')
second = np.datetime64('2023-04-29T10:30:15', 's')

print("Year: ", year)
print("Month: ", month)
print("Day: ", day)
print("Hour: ", hour)
print("Minute: ", minute)
print("Second: ", second)

#conversion of np date time into python 
from datetime import datetime
dt64 = np.datetime64('2023-04-29T12:34:56')
dtt = dt64.astype(datetime)
print(dt)

dttt = datetime(2023, 4, 29, 12, 34, 56)
t64 = np.datetime64(dt)
print(t64)
dates = np.arange('2023-04-01', '2023-04-11', dtype='datetime64[D]')
print(dates)
today = np.datetime64('today')
tomorrow = today + np.timedelta64(1, 'D')
date1 = np.datetime64('2023-05-01')
date2 = np.datetime64('2023-04-01')
num_days = date1 - date2
print(date2)
print(date1)
print(num_days)
num_business_days = np.busday_count(date1, date2)
print(num_business_days)#gives the no.of business days [excluding holidays

#DATA VISUALISATION

car = np.array(["Caterham", "Tesla", "Audi",  "BMW", "Ford", "Jeep"])
weight = np.array([0.48, 1.7, 2, 2, 2.3, 3 ])
plt.plot(car,weight)
plt.show()
plt.scatter(car,weight)
plt.show()
colors = np.array([0, 1, 2, 3, 4, 5])
sizes = np.array([20, 40, 60, 80, 100, 120])
plt.scatter(car,weight, c=colors, s=sizes)
plt.show()
plt.bar(car,weight)
plt.title('CAR WEIGHTS')
plt.show()

plt.hist(weight)
plt.show()

companys = np.array(["Facebook","Google","Amazon","Netflix"])
salary = np.array([134,305,574,33.7])
plt.bar(companys,salary)
plt.title("AVERAGE REVENUE OF FANG IN THE YEAR 2023(IN US DOLLARS)")
plt.show()