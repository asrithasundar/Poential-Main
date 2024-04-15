import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random



def write(dict,filename):
    with open(filename,'w')as f:
        for key,value in dict.items():
            f.write(f"{key} {value}\n")#writing a dictionary to a file
best_list={"water":89,"ethanol": 78,"N,N-dimethylformamide": 153, "dichloromethane": 40}

write(best_list,"best_list.txt")



def add_item(dict, filename,item,quantity):
    dict[item] = quantity #addig an item to a dict
    write(dict, filename) #write function should be already defined before to include this statement


best_list={"water":89,"ethanol": 78,"N,N-dimethylformamide": 153, "dichloromethane": 40}
add_item(best_list,"best_list.txt","peroxide",2)
add_item(best_list,"best_list.txt","hydrogen",2)
print(best_list)

def write(dict,filename):
    with open(filename,'w')as f:
        for key,value in dict.items():
            f.write(f"{key},{value}\n")
buy_list={"pen":2,"car":3}
write(buy_list,"buy_list.txt")
print(buy_list)

def square(num):
    result = num*num
    return result
print(square(3))

def display(first_name,last_name):#functions with arguments
    """

    Args:
        first_name:
        last_name:

    Returns:

    """
    print("first_name:" ,first_name)#always be careful with the comma infront of first name
    print("firstname:" ,last_name)
display(first_name="manu",last_name="janu")# check on indentation of print and function

def sum(*numbers):#if there are multiple values in the same arguement * is used

    result=0 #for summation give = 0,for  multiplication give=1
    for i in numbers:
        result +=i#can be written as result = result + i
    print("sum=", result)
sum(1,2)

#for loops

for n in (2,3,4,1):
    print(f"the number is {n} and divided by 2 is {n/2}")

    print('i am done')

word = "python"
for letter in word:
    print("give me",letter)#comma is not taken into account in a string

    print(f" give me ,{letter}")#but taken into account in a f string
#range
for i in range(10):
    print(i)
for i in range(1,102,10):#10 is the skip value
    print(i)


list_1=[7,8,3]
list_2=[4,5,6]
print (list_1,list_2)

list_1=[1,2,3]
list_2=[4,5,6]
for i in range(3):#range gives the number of lines
  print (list_1[i],list_2[i])
for i in zip(list_1,list_2):#zip returns tuples

    print (i)
for i,j in zip(list_1,list_2):#unpack tuple
    print(i,j)
for i in enumerate(list_2):
    print(i)

for i,j in enumerate(list_2):
    print(i,j)


   # loops in dictionary


best_list={"water":89,"ethanol": 78,"N,N-dimethylformamide": 153, "dichloromethane": 40}
for key,value in best_list.items():#dictionary.items()
    print(key,value)
n=10
while n>0:#repeat code
    print(n)
    n-=1

#tutorial A1

plt.plot(range(10))
plt.show()
#

x=[1,2,3]
y=[6,2,7]
plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("first_graph")
plt.show()



x1=[1,2,3,4,5,6,7,8]
y1=[2,4,3,1,4,5,6,3]
plt.plot(x1,y1,label="line1",color="blue",linewidth=2,marker=".",markerfacecolor="black",markersize=4)
x2=[1,3,4,2,1,6,4,7]
y2=[3,1,4,3,6,5,7,8]
plt.plot(x2,y2,label="line2",color="red",linestyle="dotted",linewidth=2,marker="o",markerfacecolor="black",markersize=3)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend
plt.show()

x=[x for x in range(0,5)]
y=[x+1 for x in x]
plt.plot(x,y,label="line2",color="red",linestyle="dotted",linewidth=2,marker="o",markerfacecolor="black",markersize=3)
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()


#problem 1
p = (3, 4)
limits = (2, 5)
plt.plot(p[0], p[1], marker="o", markeredgecolor="k")
plt.xlim(limits)
plt.ylim(limits)
plt.title("Point")
plt.xlabel("x")
plt.ylabel("y")
plt.xticks((p[0],))
plt.yticks((p[1],))
plt.grid()
plt.show()

#problem 2
x = [x/10 for x in range(-20, 20)]
y = [
    0.13533528323661, 0.149568619222635, 0.165298888221586, 0.182683524052734, 0.201896517994655,
    0.223130160148429, 0.24659696394160, 0.27253179303401, 0.301194211912202, 0.332871083698079,
    0.367879441171442, 0.40656965974059, 0.449328964117221, 0.49658530379140, 0.54881163609402,
    0.60653065971263, 0.67032004603563, 0.74081822068171, 0.81873075307798, 0.90483741803595,
    1.0, 1.10517091807564, 1.22140275816016, 1.34985880757600, 1.49182469764127, 1.64872127070012,
    1.82211880039050, 2.01375270747047, 2.2255409284924, 2.459603111156, 2.7182818284590,
    3.00416602394643, 3.32011692273654, 3.66929666761924, 4.05519996684467, 4.48168907033806,
    4.9530324243951, 5.47394739172, 6.04964746441294, 6.68589444227926
]

plt.plot(
    x, y,
    marker=".", markeredgecolor="k", markerfacecolor="#cc2529",
    linestyle="--", color="gray",
    label="y-line"
    )

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()


#arrays

list_1=[1,3,5]
list_2=[0.0,0.3,0.4]
A=np.asarray(list_1)
B=np.asarray(list_2)
print("A=",A)
print("B=",B)

#tutorial 11
#problem 1
def is_triangle(a, b, c):


    if np.allclose(a + b, np.absolute(c)):
        return True
    return False

is_triangle(
    np.array([0, 1]),  # a
    np.array([1, 0]),  # b
    np.array([1, 1])   # c
    )



#problem 2
v = np.array([0, 0, 1])
R = np.array([[1,  0,  0],
              [0,  0, -1],
              [0,  1,  0]])
v_ = np.dot(R, v)
print(v_)
print(np.dot(v, v_))


#random
x = list(range(10))
print("Before shuffling x =", x)
random.shuffle(x)
print("After  shuffling x =", x)
print("Random samples:     ", random.sample(x, 3))
print("Random choices:     ", random.choices(x, k=6))
print("Random choice:       ", random.choice(x))

