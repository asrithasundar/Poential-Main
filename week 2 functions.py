#lesson 8 ##problem1
def my_adder(a,b):
     return a+b
print(my_adder(3,4))

#problem 2

def cum_sum(seq):
    result=[] #obtain result as a list
    total =0
    for value in seq:
       total+=value
       result.append(total)
    return  result

seq=[1,2,3]
print(cum_sum(seq))

#problem 3
def fact(n):
    fact =1
    for value in range(1,n+1):

        fact *= value #multiply consecutive numbers
    return float(fact)#get the result as  float

n=6
print(fact(n))






#tutorial 9.problem 1
def read(filename):
    """

    Args:
        filename:

    Returns:

    """
    # define my dictionary
    dict = {}
    # start reading file line by line
    with open(filename) as f:
        for line in f:
            item, amount = line.split()
            dict[item] = int(amount)

    return dict

print(read('shoppinglist.txt'))



#problem2
def write(dict,filename):
    with open(filename,'w')as f:
        for key,value in dict.items():
            f.write(f"{key} {value}\n")#writing a dictionary to a file
best_list={"water":89,"ethanol": 78,"N,N-dimethylformamide": 153, "dichloromethane": 40}

write(best_list,"best_list.txt")

#problem3


def add_item(dict, filename,item,quantity):
    dict[item] = quantity #addig an item to a dict
    write(dict, filename) #write function should be already defined before to include this statement


best_list={"water":89,"ethanol": 78,"N,N-dimethylformamide": 153, "dichloromethane": 40}
add_item(best_list,"best_list.txt","peroxide",2)
add_item(best_list,"best_list.txt","hydrogen",2)
print(best_list)


#practice

def read(input):
    try:
        # define my dictionary
        dict = {}
        # start reading file line by line
        with open(input) as f:
            for line in f:
                # define key nd values
                (key, val) = line.split()
                # put keys and values in dictionary
                dict[str(key)] = val
    except FileNotFoundError:
        print('file doesn’t exist')
    return dict

print(read('shoppinglist.txt'))
dict = {"water": 100,
    "ethanol": 78,
    "N,N-dimethylformamide": 153,
    "dichloromethane": 40 }


print(f"The boling point of ethanol is {dict['ethanol']} °C")
for k,v in dict.items():
    print(f"the bp of {k} is {v} °c")

def my_adder(a,b,c):
    return sum((a,b,c))
d=my_adder(1,2,3)
print(d)

def my_adder(a, b, c):
    out = a + b + c
    print(f'The value out within the function is {out}')
    return out
d=my_adder(1,2,3)

def my_thermo(temp,desired_temp):
    if temp>desired_temp:status='heat'
    elif desired_temp>temp:status='AC'
    else:
        status='OFF'
    return  status

status=my_thermo(25,60)
print(status)
x=3
if x<5:
    y=2
elif x>100:
    y=50
else:
    y=0
print(y)
for c in "banana":
    print(c)
    def hey(name):
        print("my name is" +name)
    name="asru"
    hey(name)


    #tutorial 7
l=[]
for i in range(2,13,2):
    l.append(float(i))
print(l)
x=list(range(-10,11))

E=[x**2-2 for x in x]
print("x:",E)






