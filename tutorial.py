#When we assign a value to a word it becomes a variable
#Variable names are case-sensitive


name = "anshul"
last_name = "dongre"
final_name = name + " " + last_name
print("My name is :"   + (final_name))

    
age = 21
age *= 4 
print("My age is :"  + str(age))

   

height = 209.56
height *= 10
print("My height is : " + str(height)) 

ok = True
print("ok is a word : " + str(ok))

name  = "djfnijanfkndfnn"
print(len(name))



no = "HoPoPoPjdk"
print(no.find("P"))

mo = "sndsnnskn"
print(mo.upper())
#we can aslo use capitalize and lower like upper

ol = "8594858"
print(ol.isdigit()) 
#if your value is a digit it will give true otherwise false

kl = "ksaojdj"
print(kl.isalpha())
#it will not return the true value if there is a space between your value

jl = "vndiksvninvjnnnknadnjvanvnnv"
print(jl.count("v"))

hl = "vnshul"
print(hl.replace("v","a"))

gl= "he"
print(gl*5)

fl = 2
dl = 3.0
sl = "9"
fl = float(fl)
dl = int(dl)
sl = int(sl)
print(fl)
print(dl)
print(sl*5)
#similarly we can convert the data type to others like integer to float and string  

al = input("What is your name : ")
ql = int(input("My age is :" ))
wl = float(input("WHAT IS YOUR HEIGHT : "))
ql = 12
ql *= 2 
print("HELLO "+al)
print ("HEY "+str(ql))
print("YOUR HEIGHT IS : "+str(wl))

import math
pi = 3.14
si = 3.14
ti = 3.14
ri = -7
fi = 4
gi = 225
print(round(pi)) #this thing rounds to the nearest integer
print(math.ceil(si))#this thing rounds up to the nearest integer
print(math.floor(ti))# this thing rounds down to the nearest integer
print(abs(ri))#tells how far a  number is from  0
print(pow(fi,4))#increases the power of an integer
print(math.sqrt(gi))#gives the square root of an integer
print(max(gi,fi,ri))#gives the highest value 
print(min(gi,fi,ri))#gives the lowest value

qw = "hello anshul"
we = qw[0:9]
print(we)#it will give the output acc/ to the value set in the brackets and that value contains the position of the value assigned to a qw like = in hello h has the position of 0 and the position of the  space between hello anshul is 6 [start:stop:step]
er = "http://google.com"
re = slice(7,-4)
print(er[re])#this is slice

mn = int(input("How old are you : "))
if mn >= 18:
    print("you are an adult")
elif mn <0:
    print("pehle dhang se paida toh hoja dalle! ")    
else:
    print("chhoti bachi ho kya? ") 
#the order of the if statement is imp bcz while giving the output it first check from the first statement if it doesn't meet the requirement it will check the else or elif statement anf if the other statements meet the requirement it will produce an output based on the given print 

vc = int(input("HOW'S THE TEMPERATURE OUTSIDE: "))
if  not(vc >= 0 and vc <= 30):
    print("Todays weather is good")
elif vc < 0 or vc > 30:
    print("Todays weather is bad") 
#and statement gives the value of true only when both the conditions are true otherwise it will not give any output
#or statement doesn't check both the conditon if only one condition is true it will output true
#not statement reverse the condition

ml = ""

while len(ml) == 0:
    ml = input("Enter your ml: ")

print("hello "+ml)       
  #while loop creates a infinite loop until the condition gets false

for v in range(10) :
    print(v)       
for g in range(50,101) :
    print(g)    
import time
for e in range(10,0,-1) :
    print(e)
    time.sleep(1)
print("Your system has been hacked")    
#for loop creates an limited time loop

rows = int(input("How many rows ? : "))
columns = int(input("How many columns ? : "))
symbols = input("Enter a symbol to use :" )
for q in range(rows) :
    for w in range(columns) :
        print(symbols , end="")
    print()    
    #this is nested loop a loop inside a loop

while True:
        jk = input("enter your jk: ")
        if jk != "":
            break
phone_number = "1234-567-890"
for l in phone_number:
    if l == "-":
        continue
    print(l, end=" ")    
for k in range(1,21):
    if k == 13:
        pass
    else:
        print(k)  
#break = breaks the loop after etering a right value,  continue= skips to the next reptition of loop , pass= does nothing act as a placeholder

food = ["pizza","hamburger","chicken roll","sushi"]
food[3] = "momos"
print(food[3])
drinks = ["pepsi","coco-cola","frooti","thumbs-up"]
for a in drinks:
    print(a)  #so this was the list elements btw with range it will print in the list like a column
food.append("icecream")#this will increase one more item in our list
food.remove("hamburger")#this will remove a item from our list
food.pop()#this will remove the last item from our list
food.insert(0,"egg-roll")#this will replace pizza with egg-roll
food.sort()#this will print the list from 1-0
#food.clear(this will clear our list)                 

dinner = ["sandwhich","burger","noodles"]
dessert = ["chocolava","cone","ice-cream"]
breakfast = ["rice cake","tacos","ramen"]
lk = [breakfast,dinner,dessert]
print(food[2][2])
print(food[1])

vb = ("student",24,"yoho")
#we can print it with many functions like -- count,index
for g in vb:
    print(g)
if "yoho" in vb :
    print("yohohohohohoho") #so this was the tuple function this are unchangebale and it is a ordered collection

#set - collection which is unordered,and display the list in an unordered form everytime. and is doesn't print duplicate values
vehicles = {"car","motorcycle","bicycle","bcicyle"}
for gb in vehicles :
    print(gb)
bike = {"honda","apache","KTM"}
car = {"honda","tata","tesla","suzuki"}
#bike.update(car) this will print both the list
#vehicle = bike.union(car) this will print both the list
print(car.difference(bike))#this will tell what they didn't have in common
print(bike.intersection(car))#this will tell what they have in common    

capitals = {'USA':'Washington DC',
            'INDIA':'New delhi',
            'china':'Beijing'}
print(capitals.get('germany'))#with get function we will get none as a output when we didn't have the required value in our list
#print(capitals.keys())this will only give the output as of keys eg - usa,india
#print(capitals.values())this will only give the output of value eg - newdelhi,beijing
#print(capitals.items())this will give the output of the whole list
capitals.update({'Germany':'Berlin'})#this will add a new value to our list
capitals.update({'India':'C.G'})#this will add a new value to exsisting value of our list
capitals.pop('china')#this will remove china
#capitals.clear()this will clear the whole list
for er in capitals.items() :
    print(er) #so this was the dictionary function which is changeable ordered collection of the keys:values pair

#negative value means from the backside in the indes operator so lets now talk about the index operator
#index operator -- gives access to sequences elements (str,list,tuples)
x = "no is A word"
#if = (name[3].islower())
     #name = name.capitalize()
xm = x[2:5].upper()
xn = x[:7].lower()
xz = x[-3]
print(xm)
print(xn)
print(xz) 

#function = a block of code which is executed only when it is called
def hello(fr,ln,ge):
    print("hello "+fr+" "+ln)
    print("you are "+str(ge)+" years old")
    print("have a nice day!")
hello("Master","Anshul",16)

#return statement = functions send python values/objects back to the caller these value are known as the functions's return value
def multiply(number1,number2):
    return number1 * number2
print(multiply(4,5))    

#keyword arguments = arguments preceded by an identifier when we pass them to a function the order of the arguments doesn't matter unlike he positional arguments pyhton knows the names of the arguments that our function receives

def mono(first,middle,last):
    print("hello "+first+" "+middle+" "+last)
mono("sir","anshul","hello")
def duo(uno,dos,fry):
     print("how are you? "+uno+" "+dos+" "+fry) 
duo(fry="sir",dos="anshul",uno="hello")    

# nested function value = function calls inside other function calls innermost function calls are resolved first returned value is used as arguments for the next outer function
print(round(abs(float(input("Enter a whole positive number: ")))))

# variable scope = the region that a variable is reconized a variable is only available from insisde the region it is created.a global and locally scoped versions of a variable can be created
bv = "bro" #it is a global scope(available inside and outside the functions)
def display_name():
    bv = "code" #this is a local scope (available only insisde this function)
    print(bv)
display_name
print(bv)
#an scope function always use the value of local scope first 

#*args = parameter that will pack all arguments into a tuple useful so that a function can accept a varying amount of arguments.
 
def add(*stuff): #the asterisk symbol is imp without it you cannot use this function
    sum = 0
    stuff = list(stuff) #changing the stuff into list bcz without changing it we cannot change it after output
    stuff[4] = 3
    for i in stuff:
        sum += i
        return sum
print(add(1,2,3,0,5,6,))

#**kwargs =  parameter that will pack all arguments into a dictionary useful so that a function can accept varying amount of keyword arguments
def gg(**jok):
    print("hello",end=" ")

    for key,value in jok.items():
        print(value,end=" ")
gg(title="Mr.",gold="Anshul",holo="WE",dolo="KNOW",bolo="YOU",solo="ARE",tolo="BATMAN")        

#str.format() = optional method that gives users more control when displaying output
ja = "cow"
ka = "moon"
print("the "+ja+"jumped over the "+ka)
#print("the {} jumped over the {}".format(ja,ka))
#print("the {0} jumped over the {1}".format(ja,ka)) this is a positional argument
#print("the {ja} jumped over the {ka}".format(ja="cow",ka="moon")) this is a keyword argument
text = "The {} jumped over the {}"
print(text.format(ja,ka))
jh ="bro"
print("hello, my name is {}".format(jh))
print("hello my name is {:10}.nice to meet you".format(jh))#padding
print("hello, my name is {:<10}nice to meet you".format(jh))#left align
print("hello, my name is {:>10}.nice to meet you".format(jh))#right align
print("hello, my name is {:^10}.nice to meet you".format(jh))#center align
mb = 3.14567
nb = 1000
print("the number pi is {:.3f}".format(mb))
print("the number is{:,}".format(nb))
print("the number is{:b}".format(nb))#binary no.
print("the number is{:o}".format(nb))#octo no.
print("the number is {:x}".format(nb))# hexa decimal form
print("the number is {:E}".format(nb))#prints in scientific notation

import random
ck = random.randint(1,10)#integers
dk = random.random()#float
mylist = ['rock','papers','scissors']
xc = random.choice(mylist)
cards = [1,2,3,4,5,6,7,8,9,"A","K","J"]
random.shuffle(cards)
print(ck)
print(dk)
print(xc)
print(cards)

#exception = events detected during execution that interrupt the flow of a program
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)#this thing is optional its upon you whether you add it or not
    print("you can't divide by zero! idiot!")
except ValueError:
    print("Enter only numbers plz")
except Exception:
    print("something wnet wrong")
else:
    print(result)            

#file detection
import os
path = "C:\\Users\\dell\\Documents" #if you have slash in your location add one more slash
if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
else: 
    print("that location doesn't exist")
#if your file is a folder we can use[ if os.path.isdir(path):  ]      

try:
    with open('text.test') as file: #write the full source of the file if itn't opened in vs code
        print(file.read())
        print(file.closed)
except FileNotFoundError:
    print("This file is can't be found")
except FileExistsError:
    print("this file doesn't exist")              #oepning a file

#re-writing or adding something in your existing file!
wtext = "this file has been overwritten\n with some line spaces shit\n"
with open('text.test','w') as file:
    file.write(wtext)#for rewriting
atext = "so this is gonna add text in your file"
with open('text.test','a') as hell:
    hell.write(atext)

#copyfile() = copies the contents of file
#copy() = copyfile() + permission mode + destination can be a directory
#copy2() = copy() + copies metadata (file's creation and modification times)
import shutil
shutil.copy('text.test','styles')#in the bracket first write which file you have to copy(source) after the comma write where to copy(destination)
#we are keeping the destination empty

#moving a file
import os
source = "styles"
destination = "C:\\Users\\dell\\documents\\styles"
try:
    if os.path.exists(destination):
        print("there is already a file there")
    else:
       os.replace(source,destination)
       print(source+" was moved")    
except FileNotFoundError:
     print(source+" was not found")

#deleting a file
#import os
#import shutil
#lath = "C:\\Users\\dell\\documents\\abcd"
#try:
    #os.remove(lath) deletes a file
    #os.rmdir(lath) #deletes an empty directory/folder
    #shutil.rmtree(path) delete a folder conatining a file
#except FileNotFoundError:
 #   print("that file was not found")
#except PermissionError:
#    print("you do not have permission to delete this file")
#except OSError:
#    print("you cannot delete that using that function")
#else:
#    print(lath+"was deleted"

# module = a file containing python code may contain functions classes etc.
#used with modular programming which is to separte a program into parts
#import test as msg
#test.hello()
#test.bye()
#msg.hello()
#msg.bye()
# from test import hello,bye
#hello()
#bye()
# from test import *     =  this will import all the functions from the module
help("modules") #this will give the lsit of all the  modules

bbl = type(source)  #type()  tells the type 
print(bbl)

bla = "235323"
alb = int(bla) #we can also convert this to float and strings
shl = bla * 3
print(shl)

zx = 97
if zx > 100:
    print("your number is bigger than 100")
elif zx >= 100:
    print("Your number is greater than 100 or equal to 100")
elif zx < 100:
    print("your number is smaller than 100")       #we can use elif many times
elif zx <= 100:
    print("your number is smaller than 100 or equal to 100")
elif zx == 100:
    print("Your number is equal to 100")
else:
    print("nothing is true")    

def thing():
    print("hello")
    print("run")
thing()
print("zip")
thing()    

XYZ = max("xyz")
print(XYZ)
ABC = min("abc")
print(ABC)

def anshul():
    print("I AM BATMAN")
    print("I AM VENGEANCE") #this 2 print statement will not get printed because thats what def do
print("hello")
anshul()

def greetings(lang):
    if lang ==  "op":
       print("You are op")
    elif lang == "bb":
        print("you are not op")
  
greetings("op")
greetings("bb")       

N = 3
while N > 0:
    print(N + 1)
    print(N)
    break  
 #if we didnt use break it will keep running infinitely times

#definite loops 
i = [5,4,3,]
for i in i:
    print(i) #it will print the listed values one by one in a line
    break

#finding the largest value
largest_so_far = -1
print("before", largest_so_far)
for the_num in [9,41,12,3,74,15] :
    if the_num > largest_so_far :    #to find the smallest number change the ">" sign to "<"
        largest_so_far = the_num
        print(largest_so_far, the_num)
print("after" , largest_so_far)  

#counting a loop
zork = 0 
print('before' , zork)
for thing in [9,41,12,3,74,15] :
    zork = zork + 1 
    print(zork, thing)
print('after' , zork)

#summing in a loop
pork = 0
print('before ' , pork)
for thing in [9,41,6,15,3,77] :
    pork = pork + thing
    print(pork , thing)
print('after' , pork)    

#finding average in loop
count =  0
sum = 0
print("before " , count , sum)
for value in [9,41,42,34,21,22] :
    count =  count + 1
    sum = sum + value
    print(count, sum, value)
print("after" , count , sum, sum / count)   

fruit = 'banana'
nn = 3
nm = fruit[nn-1]
print(nm)

hur = 'banana'
for letter in hur:
    print(letter)

vo = "i am batman"
print(vo[2:10]) #it will print from 2 to upto 10 but not including 10
print(vo[:]) #this will print every value   
#this 2 are also called slicing strings

'n' in vo 
"z" in vo
pos = vo.find('am')
sos = vo.find('z') #if the value not found prints -1
tos = vo.upper()
qos = vo.lower()
wos = vo.replace('am' ,'was')
vo.lstrip()
vo.rstrip()
vo.strip()

#kj = open('test.py')
#jb = open('test.py')
#count = 0
#for line in jb:
#    count = count + 1
#print('line count:' , count)#counting a  file
#inp = jb.read()
#print(len(inp))
#kn = open('notes') #this all will read the lines that starts with   is: 
#for fine in jb:
#    if fine.startswith("is") :
#        print(fine)

xa = input("Enter a file name :")
fg = open(xa)
count = 0
for hine in fg:
    if hine.startswith("is") :
        count = count + 1
print("there were", count, "subject lines in" , xa)     

OG = ["batman" , 'SUPERMAN' , 'FLASH']
OG[2] = 'WONDER WOMAN'
print(OG)
go = ["iron man" , 'captain america' , 'thor']
ov = OG + go
print(ov)

bo = "I AM BATMAN"
ho = bo.split() # SPLIT breaks a string into parts and produces a list of strings 
print(ho)
print(ho[2])

lo = "dongreanshul25@gmail.com 25 sep 2007"
ao = lo.split(';')
print(ao)

ddd = dict()
ddd["age"] = 21
ddd["course"] = "ca"
print(ddd)
ddd['age']= 23
print(ddd)
ddd["age"] = ddd["age"] * 2
print(ddd)

ooo = {  }
print(ooo) #we can use curly brackets for empty strings
for shame in ddd:
    shame = ddd.get(23)

jjj = { 'chuck' : 1 , 'fred' : 42, 'jan' : 100}
for aaa,bbb in jjj.items():
    print(aaa, bbb)

#once again tuple
(t, z) = (7388938 , "BATMAN")
print(t)
print(z)

#sorting in tuple
ll = {'a':1, 'b':22 , 'c':10}
print(sorted([ (xx,zz) for zz,xx in ll.items() ])) #ascending order
print(sorted([ (xx,zz) for zz,xx in ll.items() ], reverse=True )) #descending order

#import re
#hand = open('test.py')
#for line in hand:
#    line = line.rstrip()
#    if re.search('hello' , 'shut up') :
#      print(line)
#learn regular expression from = https://www.w3schools.com/python/python_regex.asp  or W3SCHOOL

#A HTTP REQUEST IN PYTHON
#import socket
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mtsock.connect(('data.pr4e.org" , 80))
#cmd = 'GET http//data.pr4e.org/romeo.txt HTTP/1.0\n\n' .encode()
#mysock.send(cmd)
#while true:
#    data = mysock.recv(512)
#    if (len(data) < 1) :
#        break
#    print(data.decode())
#mysock.close()

print(ord("H")) #the ord function tells us the numeric value of a simple ASCII character
 

#import urllib.request, urllib.parse, urllib.error
#ghand = urllib.request.urlopen('file:///C:/Users/dell/Documents/idk2.html')
#for dine in ghand:
#    print(dine.decode() .strip)
#using like a file
#dhand = urllib.request.urlopen('file:///C:/Users/dell/Documents/test.html')
#counts = dict()
#for hine in dhand:
#    words = hine.decode() .split()
#    for lord in words:
#        counts[lord] = counts.get(lord, 0) + 1
#print(counts)        

#READING WEB PAGES:
#khand = urllib.request.urlopen("file:///C:/Users/dell/Documents/test.html")
#for shine in khand:
#we    print(shine.decode() .strip())
    
#import urllib.request, urllib.parse, urllib.error    
#import bs4
#url = input('ENTER - ')
#html = urllib.request.urlopen#(url).read()
#soup = bs4(html, 'html.parser')
#tags = soup("a")
#for tag in tags:
#    print(tag.get('href' , None))
#this code will help you in scrapping throught sites

import json
data = '''{
 "name" : "chuck",
  "phone" : {
  "type" : "intl",
  "number" : "+1 734 303 4456"
  },
  "email" : {
   "hide" : "yes"
   }
 }'''
info = json.loads(data)
print('Name:' ,info["name"])
print('hide:' ,info["email"]["hide"])

aata = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(aata)
print(info[1]['name'])

#import urllib.request, urllib.parse, urllib.error, _json
#servicecour1 = 'http://maps.googleapis.com/maps/api/geocode/json?'
#while True:
 #   address = input('enter location: ')
#    if len (address) < 1: break
#url = servicecour1 + urllib.parse.urlencode({'address' : address})

#print('retreieving', url)
#uh = urllib.request.urlopen(url)
#datas = uh.read().decode()
#print('retrieved' , len(datas), 'characters')

#try:
#    js = json.loads(datas)
#except:
#    js = None
#if not js or 'status' not in js or js[ "status"] !=  'OK':
#    print("=== Failure to retrieve === ")
#    print(datas)
    

#lat = js["results"][0]["geometry"]["location"]["lat"]
#eng = js["results"][0]["geometry"]["location"]["eng"]
#print('lat', lat, 'eng', eng)
#location = js['results'][0]["Formatted_address"]
#print(location)

{
    "status": "OK",
    "results": [
       {
           "geometry": {
               "location_type": "APPROXIMATE",
           "location": {
              "lat": 42.2808256,
              "lng": -83.7430378

           }  
       },
       "address_coponents": [
           {
               "long_name": "ann arbor",
               "types": [
                   "locality"
                   "political"

               ],
               "short_name": "ann arbor"

           }
       ],
       "formatted_address" : "ann arbor, MI, USA",
       "types": [
           "locality"
           "political"

            ]
       }
    ]
}

#import urllib.request, urllib.parse, urllib.error,
#import twurl
#import json
#
#TWITTER_URL = "https://api.twitter.com/1.1/friends/list.json"

#while true:
#    print('')
#    acct = input('Enter twitter account')
#    if (len(acct) < 1): break
#    url = twurl.augment(TWITTER_URL,
#                        {"screen_name" : acct, "count": "5"})
#    print('Retrieving', url) 
#    connection = urllib.request.urlopen(url)
#    nata = connection.read().decode()
#    headers = dict(connection.getheaders())
#    print('Remaining', headers['x-rate-limit-remaining'])
#    js = json.loads(nata)
#    print(json.dumps(js, indent-4))

#   for u in js ["users"]:
#        print(u["screen_name"])
#        s = u['status']["text"]
#        print(' ',s[:50])

class Partyanimal:
    lll = 98

    def party(self):
        self.lll = self.lll + 1
        print("so far",self.lll)

an = Partyanimal()



class zPartyAnimal:
    x = 0
    def zparty(self):
        self.x = self.x + 2
        print(self.x)

an = zPartyAnimal()


class badanimal:
    pl = 0
    def __init__(self):
        print("IM CONSTRUCTED")

    def opart(self) :
            self.pl = self.pl + 1
            print("so far", self.pl)

    def __delattr__(self):
        print("Im destructed", self.pl)

pn = badanimal()
pn.opart()
pn.opart()
pn = 42
print("pn contains", pn)        

class football(badanimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.opart()
        print(self.pl, "points", self.points)

print(4 // 3)
print(8/2)
print(4*2)
print(4**2)    

#ATTRIBUTE = what a object is/has  ex= name,height,age
#METHODS = ACTION ex= SLEEP,EAT,RUN

#OBJECT ORIENTED PROGRAMMING


class Car:
    # __init__ = IT CONSTRUCTS OBJECT FOR US
    def __init__(self,make,model,year,color): #IN THIS BRACKET THOSE VALUES WILL COME THAT WILL USE THE METHOD
        self.make = make #ASSIGNING THIS VALUE MEANS THAT IT WILL DO WHAT SOMEONE WILL ASSIGN TO IT
        self.model = model  #This are known as instance variable
        self.year = year   #THIS VALUES INSIDE THE DEF IS INSIDE THE CLASS BUT OUTSIDE THE CONSTRUCTOR
        self.color = color

    def drive(self):
        print("This "+self.model+" is driving") #WE PUT (SELF.MODEL) SO THAT THE VALUE ASSIGNED TO THE MODEL WILL PRINT AUTOMATICALLY AND MAKE IT EFFICIENT

    def stop(self):
        print("This "+self.model+"is stopped")    
        
#TO USE THE (CLASS CAR) IT IS REQUIRED TO PASS IN A VALUE EX = (MAKE,MODEL,YEAR,COLOR)        
 
#IF YOUR CLASS IS ON ANOTHER FILE USE THIS = FROM (NAME OF YOUR FILE NAME)  IMPORT  (NAME OF YOUR MODULE)

car_1 = Car("ford","Mustang GT",2015,"red") 
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)       
car_1.drive()
car_1.stop()

class character:
    Antonganist = "JOHAN LIEBERT" #CLASS VARIABLE HAS A UNIQUE VALUE ASSIGNED TO IT THAT CAN BE CHANGED LATER
    def __init__(self,nomero,agew,Ability,profession):
        self.nomero = nomero
        self.agew = agew  
        self.Ability = Ability
        self.profession = profession


    def info(self):
        print("Showing "+self.nomero+"'s information:""\n""PLAYER'S AGE = " +self.agew+"\n""PLAYER'S ABILITY = "+self.Ability+"\n""PLAYER'S PROFESSION = " +self.profession) 


player_1 = character("Johan Liebert","32","MANIPULATION","SERIAL KILLER")
player_2 = character("Dr.TENMA","42","HEALER","DOCTER")

player_1.info()
player_2.info()
print("THE NAME OF THE ANTONGANIST OF MONSTER ANIME IS = "+character.Antonganist)

#INHERITENCE = CHILDREN CLASS CAN USE ATTRIBUTES OF PARENT CLASS
class animal:
    alive =  "Yes"
    def run(self):
        print("THIS ANIMAL IS RUNNING")
#METHOD OVER RIDING = CHILD CLASS CAN CHANGE A METHOD
class rabbit(animal):
    yeat = "EATING"
    def run(self):
        print("This rabbit is running")
#MULTI-LEVEL INHERITENCE = ANOTHER CHILDREN CAN USE THINGS OF ANOTHER CHILDREN CLASS
#MULTI INHERITENCE =  CAN USE THINGS OF MORE THAN ONE PARENT CHILD
class rabbitbaby(rabbit,animal):
    def run(self):
        print("The rabbits's baby is running")
print(rabbit.alive)      
print(rabbitbaby.yeat)  
print(rabbitbaby.alive)
print(rabbit.run)
print(rabbitbaby.run)

class van:
    def onn(self):
        print("the vehichle is on")
        return self            #RETURN IS USED TO RETURN THE OUTPUT OF THE FUNCTION
    def engine(self):
        print("The engine of the vehicle is started")
        return self
    def brake(self):
        print("You have reached your destination please push the brake")
        return self
    def off(self):
        print("Your vehichle is turned off")
        return self
van = van()
van.onn().engine().brake().off()
         

# super() = function used to give access to the methods of a parent class
#           Returns a temporary object of a parent class when used

class Rectangle:
     def __init__(self,length,width):
         self.length = length
         self.width = width
class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        return self.length*self.width
class cube(Rectangle):
    def __init__(self, length, width,height):
        super().__init__(length, width) 
        self.height = height
    def volume(self):
        return self.length*self.width*self.height

square = Square(3, 3)
Cube = cube(3, 3, 3)
print(Square.area)
print(cube.volume)

#ABSTRACT CLASS = CLASS WICH CONTAINS ONE OR MORE ABSTRACT METHODS
#ABSTRACT METHOD = A METHOD THAT HAS A DECLARATION BUT DOES NOT HAVE AN IMPLEMENTATION
#PREVENTS A USER FROM CREATING AN OBJECT OF THAT CLASS
#COMPELS A USER TO OVERRIDE ABSTARCT METHODS IN A CHILD CLASS
from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    def stopp(self):
        pass
class train(vehicle):
    def go(self):
        print("THIS TRAIN IS MOVING")
        return self
    def stopp(self):
        print("THIS TRAIN IS STOPPED")
        return self
class aeroplane(vehicle):
    def go(self):
        print("THIS AEROPLANE IS FLYING")
        return self
    def stopp(self):
        print("THIS AEROPLANE IS STANDING")
        return self
aeroplane.stopp(vehicle)
train.go(vehicle)        

#DUCK TYPING = CONCEPT WHERE THE CLASS OF AN OBJECT IS LESS IMPORTANT THAN THE METHODS/ATTRIBUTES
#              CLASS TYPE IS NOT CHECKED IF MINIMUM METHODS/ATTRIBUTES ARE PRESENT 

class duck:
    def walk(self):
        print("THIS DUCK IS WALKING")
    def talk(self):
        print("THIS DUCK IS TALKING")
class chicken:
     def walk(self, duck):
        print("THIS CHICKEN IS WALKING")
     def talk(self, duck):
        print("THIS CHICKEN IS TALKING")
class person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You catched the duck")

duck = duck()
chicken = chicken()
person = person()
person.catch(duck)        

#Walrus operator ( := ) assigns values to variables as part of a larger expression

foods = list()
while True:
    food = input("What food do you like?:  ")
    if food == "quit":
        break
    foods.append(food)
#With walrus 
foodss = list()
while foodsss := input("What food do you like?: ") != "quit":
    foodss.append(foodsss)

print(password := "Batman_2517")
kol = print
kol("WHAT IS KOL")

#Higher order function = a function that either:
#                          1. accepts or function as an argument
#                                or
#                          2. returns a function    
#(in python functions are also treated as objects)

def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):
    text = func("Hello")
    print(text)
hello(loud)
hello(quiet)

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))

# LAMBDA FUNCTION  = function written in 1 line using lambda keyword
#                     accepts any number of arguments but only has one expression
#                        useful if needed for short time
# lambda paramters:expression

addd = lambda i, o, p: i + o + p
m_name = lambda fn, ln: fn+" "+ln
acheck = lambda age:True if age >18 else False
print(addd(4,5,6))
print(m_name("I'm","Vengeance"))
print(acheck(16))

#Sort method =  used with lists
#sort function = used with iterables
# 
studentsss =   [("Batman", "A", 44),
             ("superman", "F", 48),
             ("flash", "B", 22),
             ("anshul", "AA", 14),
             ("cyborg", "D", 34)]

student =    [("tony", "A", 44),
             ("thor", "F", 48),
             ("hulk", "B", 22),
             ("anshul", "AA", 14),
             ("vision", "D", 34)]


grades = lambda grade:grade[1]
studentsss.sort(key=grades)
ages = lambda agh:agh[2] 
student.sort(key=ages)
for k in studentsss:
    print(k)
for j in student:
    print(j)

#MAP = APPLIES A FUNCTION TO EACH ITEM IN A ITERABLE(LIST,TUPLES)
#MAP(FUNCTION,ITERABLE)

store = [("shirt",20.00),
         ("pant",50.00),
         ("jeans",80.00),
         ("coat",160.00)]
to_dollars = lambda data: (data[1] * 0.012 )
store_dollars = list(map(to_dollars,store))
for l in store_dollars:
    print(l)

#FILTER = CREATES A COLLLECTION OF ELEMENTS FROM AN ITERABLE FOR WHICH A FUNCTON RETURNS
#FILTER(FUNCTON,ITERABLES)

top_animes = [("ONE PIECE", 9.5),
             ("DBZ", 7),
             ("NARUTO", 8.5),
             ("JJK", 8.1),
             ("OPM", 8.4)]

rating = lambda d:d[1] >= 8
top_anime = list(filter(rating, top_animes))

#REDUCE = APPLY A FUNCTION TO AN ITERABLE AND REDUCE IT TO A SINGLE CUMALITIVE VALUE
#         PERFORMS A FUNCTION ON FIRST TWO ELEMENTS AND REPEATS PROCESS UNTIL 1 VALUE REMAINS
#REDUCE(FUNCTION, ITERABLE)

import functools

LCM = [5,6,90,2,4]
resultt = functools.reduce(lambda a, b:a * b,LCM)
print(resultt)
ANS_TO_PROPOSAL = ["Y","E","S"]
Answer = functools.reduce(lambda c, d:c + d,ANS_TO_PROPOSAL)
print(Answer) 
#LIST COMPREHENSION = A WAY TO CREATE A NEW LIST WITH LESS SYNTAX
#                     CAN MIMIC LAMBDA FUNCTIONS EASIER TO READ
#                     LIST = [EXPRESSION FOR ITEM IN VARIABLES]
squares = [p * p for p in range(1,11)]
print(squares)
estudiante = [100,90,80,70,60,50,40,30,20,10]
passed_students = [o if o >= 60 else "FAILED" for o in estudiante]
print(passed_students)

# DICTIONARY COMPREHENSION = create dictionaries using an expression
#                            can replace for loops and certain lambda expression      
# 
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if condition}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}

cities_in_F = {'New York' : 32, 'MEXICO' : 52, 'OHIO' : 22, 'BOSTON' : 42,}
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)
cities_in_A = {'New York' : "SNOWING", 'MEXICO' : "SUNNY", 'OHIO' : "rainy", 'BOSTON' : "SUNNY",}
cities_in_B = {key: value for (key, value) in cities_in_A.items() if value == "SUNNY"}
print(cities_in_B)
#ZIP = AGGREGATE ELEMENTS FROM TWO OR MORE ITERABLES(LIST,TUPLES,SETS) CREATES A 
#      ZIP OBJECT WITH PAIRED ELEMENTS STORED IN TUPLE FOR EACH ELEMENT

#username = ["DUDE","HULK","BATMAN"]
#passwords = ["p@ss","Choti master","Superman C"]
#users = dict(zip(username,passwords))#
#for key,value in users.items:
#    print(key+" : "+value)

import time

print(time.ctime(0)) #convert a time expressed in seconds since epoch to readable string
#                      epoch = when your computer thinks time began
print(time.time()) #return current seconds since epoch
print(time.ctime(time.time())) #return current time
time_object = time.localtime()  #local time 
tme_object = time.gmtime() #UTC time
tm_obj = time.strftime("%d, %B  %Y %H:%M:%S, tme_object")
print(tm_obj)


#(YEAR, MONTH , DAY , HOURS, MINUTES , SECS , DAY OF THE WEEK, DAY OF THE YEAR , DST)

time_yring = time.asctime()
print(time_yring)

time_ring = time.mktime
print(time_ring)

#THREAD = FLOW OF EXECUTION LIKE A SEPARATE ORDER OF INSTRUCTION
#CPU BOUND  = PROGRAM SPENDS MOST OF ITS TIME WAITING FOR INTERNAL EVENTS = USE MULTIPROCESSING
#IO BOUND = PROGRAM SPENDS MOST OF ITS TIME WAITING FOR EXTERNAL EVENTS = USE MULTITHREADING

import threading
import time
def breakfast():
    time.sleep(4)
    print("YOU HAVE FINISHED YOUR BREAKFAST ")
def drink_coffee():
    time.sleep(3)
    print("YOU HAVE FINISHED DRINKING COFFEE")
def study():
    time.sleep(6)
    print("Its time to sleep now")

pl = threading.Thread(target=breakfast,args=())
pl.start() 
llp = threading.Thread(target=drink_coffee,args=())
llp.start() 
ppl = threading.Thread(target=study,args=())
ppl.start() 
print(threading)
#The . join() method delays a program's flow of execution until the target thread has been completely read
pl.join()
ppl.join()
llp.join()
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

#DAEMON THREAD = A THREAD THAT RUNS IN THE BACKGROUND NOT IMP FOR PROGRAM TO RUN YOUR PROGRAM 
#                WILL BOT WAIT FOR DAEMON THREADS TO COMPLETE BEFORE EXITING 
#                DAEMON CAN STOP WHILE LOOPS AFTER ENTERING THE DESIRED VALUE
# 

import threading
import time

#def timer():
#    print()
#    print()
#    counter = 0
#    while True:
#        time.sleep(1)
#        counter += 1
#        print("logged in for:",counter,"seconds")
        
##co = threading.Thread(target=timer, daemon=True)
#co.start()
#ansuer = input("Do you want to exit")        

#MULTIPROCESSING = running tasks in parallel on diff. cpu cores bypasses GIL used for thread
#                multiprocessing = better for cpu bound task(heavy cpu usage)
#                multithreading = better for in bound tasks (waiting task   
 

#GUI
from tkinter import *


window = Tk() #Shows a window
window.geometry("420x420") 
window.title("IM VENGEANCE")

#icon = PhotoImage(file='')
#window.iconphoto(True,icon)
  
countii = 0

def click():
    global countii
    countii+=1
    print("Thanks")



label = Label(window,
              text="I'M VENGEANCE",
              font=('arial',40,'bold'),
              fg="#000080",
              bg="red",
              relief=RAISED,
              bd=20,
              padx=20,
              pady=20,)
photo = PhotoImage(file='like.png')
              
label.pack()
buton = Button(window,
               text="Click me",
               command=click,
                state=ACTIVE,
                activebackground="blue",
                fg="green",
                activeforeground="green",
                image=photo,
                compound='bottom',
              )
buton.pack()
window.config(background="black")
window.mainloop()  #place a window in computer screen

#for taking input from the user
window2 = Tk()
window2.geometry("420x420")
window2.title('Enter your data')

def submit():
     username=entryy.get()
     print("Hello"+ username)
   

def delete():
    entryy.delete(0,END)

def backspace():
    entryy.delete(len(entryy.get())-1, END) 

entryy  = Entry(window2,
                font=("Arial,40"),
                fg="green",
                )

entryy.insert(0,'CHUTIYA')
entryy.config(background="black")
entryy.pack()
window2.config(background="black")
entryy.pack(side=LEFT)
submit_button = Button(window2,text="submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window2,text="Delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window2,text="Backspace",command=backspace)
backspace_button.pack(side=RIGHT)

   

window2.mainloop()

#for taking user password

window3 = Tk()
window3.geometry("420x420")
window3.title('Enter your data')

def submit3():
    usernamee = entryyy.get()
    print("YOUR PASSWORD IS: "+ usernamee)
    
  

def delete3():
    entryy.delete(0,END)

def backspace3():
    entryyy.delete(len(entryyy.get())-1, END)    

entryyy  = Entry(window3,
                font=("Arial,40"),
                fg="green",
                )

entryyy.insert(0,'CHUTIYA')
entryyy.config(show="*")
entryyy.config(background="black")
entryyy.pack(side=LEFT)
entryyy.pack()
window3.config(background="black")
submit_button3 = Button(window3,text="submit",command=submit3)
submit_button3.pack(side=RIGHT)

delete_button3 = Button(window3,text="Delete",command=delete3)
delete_button3.pack(side=RIGHT)

backspace_button3 = Button(window3,text="Backspace",command=backspace3)
backspace_button3.pack(side=RIGHT)
window3.mainloop()

window4 = Tk()
window4.geometry("620x620")
window4.title('checkbox')
window4.config(background="black")


def display():
    if(yn.get()):
        print("WHY ARE YOU GAY?")
    else:
        print("YOU A GAY!")
yn = BooleanVar()

def order():
    if(ck.get()==0):
        print("You are a sigma male")
    elif(ck.get()==1):
        print("You are a awesome")
    elif(ck.get()==2):
        print("You are a lazy but sigma")


#batsy = PhotoImage(file="C://Users//dell//Documents//tutorial//logo1.jpg")
#thor = PhotoImage(file="C://Users/dell//Documents//tutorial//logo2.png")
#flash = PhotoImage(file="C://Users/dell//Documents//tutorial//logo3.png")
#heroesimage = [batsy,thor,flash]
heroes = ["Batman","THOR","Flash"]
ck = IntVar()
check_button = Checkbutton(window4,
                           text="IF YOU ARE GAY CLICK THE CHECKBOX",
                           variable=yn,
                           onvalue=True,
                           offvalue=False,
                           foreground="green",
                           activeforeground="green",
                           command=display,
                            bd=20,
                            padx=20,
                            pady=20)
for index in range(len(heroes)):
 radio_button = Radiobutton(window4,
                           text=heroes[index],
                           variable=ck,
                           value=index,
                          # image=heroesimage,
                           font=("Impact"),
                           compound="left",
                         #  indicators=0,
                          
                           command=order)
check_button.pack()
radio_button.pack(anchor=W)
window4.mainloop()



#from tkinter import *
#window5 = Tk()
#window5.geometry("620x620")
#window5.title('temp')

#def sub():
#    print("The temperature is", int(scale.get()), "degree C" )

#scale = Scale(window5,
#              from_=100,
#              to=0,
#              length=600,
#              orient=VERTICAL,
#              font=(20),
#              tickinterval=10,
#              resolution=5,              troughcolor="#69EAFF",
#              fg="red",
#       bg="#111111"
#              bg="#111111"
#              )    
#scale.set(50)
#butt = Button(window5,
##             text="SUBMIT",
#             command=sub)
##scale.pack()
#butt.pack()
#window5.mainloop

#window6 = Tk()
#def subb():

 #   foody = []
    
 #   for  index in listbox.curselection():
 #    foody.insert(index,listbox.get(index))

 #   for index in foody:
 #       print(foody)

#def exit():
#    for indexx in reversed(Listbox.curselection()):
#        Listbox.delete(indexx)

#   listbox.config(height=listbox.size())
     

#def add():
#    listbox.insert(listbox.size(),entryBox.get())
#    listbox.config(height=listbox.size())



#Listbox.insert(1,"pizza")
#Listbox.insert(2,"pasta")
#Listbox.insert(3,"icecream")
#Listbox.insert(4,"burger")
#Listbox.insert(5,"sandwhich")

##entryBox = Entry(window6)
#entryBox.pack()
#listbox = Listbox(window6,
#                  bg="f7ffde",
#                  font=35,
##                  width=12,
 #                 selectmode=MULTIPLE)    
#listbox.pack()

#subb_button = Button(window6,
#                     text="Submit",
#                     command=subb)
#subb_button.pack()

#del_button = Button(window6,
#                    text="Delete item",
#                    command=exit)
#del_button.pack()

#add_button = Button(window6,
#                    text="ADD",
#                    command=add)
#add_button.pack()
#window6.mainloop()
from tkinter import messagebox
window5 = Tk()

def clickme():
 #   messagebox.info(title="HUMAN",Message="You are a human")
 #   messagebox.showerror(title="HUMAN",Message="an error occurred")
 #   messagebox.showwarning(title="HUMAN",Message="You are a alien")
 #   if messagebox.askokcancel(title="HUMAN",Message="DO YOU WANNA SEE A MAGIC"):
 #       print("YOU ARE KIND")
 #   else:
 #       print("SO RUDE")
 #   if messagebox.askyesno(title="HUMAN",Message="DO YOU LIKE ANIME"):
 #       print("YOU ARE AN AWESOME PERSON")
 #   else:
 #       print("YOU ARE BORING!")
    anser = messagebox.askyesnocancel(title="si o no",message="Do you like coding?")
    if(anser==True):
        print("GOOD GOOD")
    elif(anser==False):
        print("Then why are you wasting your time")
    else:
        print("Kuch toh bol")
            
     
bu = Button(window5,text="Click me",command=clickme)
bu.pack()
window5.mainloop()

from tkinter import colorchooser

def clickat():
    color = colorchooser.askcolor()
    hex = color[1]
    window.config(bg=hex)

window6 = Tk()
window6.geometry("420x420")
buiton = Button(text="click",command=clickat)
buiton.pack()    
window6.mainloop()


def clickyou():
    input = text.get("1.0",END)
    print(input)
   
window7 =Tk()
text = Text(window7,bg="light yellow",font=("Ink Free",25),height=8,width=20,padx=20,pady=20)
butti = Button(window7,text="submit",command=clickyou)
text.pack()
butti.pack()
window7.mainloop()

import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            print(file_contents)

app = tk.Tk()
app.title("File Reader")

open_button = tk.Button(app, text="Open File", command=open_file)
open_button.pack()

app.mainloop()

from tkinter import *
window8 = Tk()
window8.geometry = ("500x500")
window8.title("Calculator program")


def button_press():
    global equation_text

    equation_text = equation_text + str(sum)
    equation_label.set()
def equals():
    global equation_text

    total = str(eval(equation_text))
    equation_label.set(total)
    equation_text = total

def backward():
    pass
equation_text = " "
equation_label = StringVar()
label = Label(window8, textvariable=equation_label, font=('consolas',20), bg='white', height=2, width=24)
label.pack()

frame = Frame(window8)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, command= lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, command= lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, command= lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, command= lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=6, height=4, width=9, font=35, command= lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, command= lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, command= lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, command= lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, command= lambda: button_press(8))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command= lambda: button_press(0))
button0.grid(row=3, column=1)

plus = Button(frame, text="+", height=4, width=9, font=35, command= lambda: button_press("+"))
plus.grid(row=0, column=3)

minus = Button(frame, text="-", height=4, width=9, font=35, command= lambda: button_press("-"))
minus.grid(row=1, column=3)

multiply = Button(frame, text="x", height=4, width=9, font=35, command= lambda: button_press("x"))
multiply.grid(row=2, column=3)

divide = Button(frame, text="/", height=4, width=9, font=35, command= lambda: button_press("/"))
divide.grid(row=3, column=3)

clear = Button(frame, text="clear", height=4, width=20, font=35, command=backward)
clear.grid(row=6, column=2)

equal = Button(frame, text="=", height=4, width=9, font=35, command=equals)
equal.grid(row=3, column=0)

decimal = Button(frame, text=".", height=4, width=9, font=35, command= lambda: button_press("."))
decimal.grid(row=3, column=2)

window8.mainloop()
