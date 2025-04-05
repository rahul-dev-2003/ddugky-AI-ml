# default function 
def greet():
    print("hello")

greet()  # function call

##############################################################################################

# ane argument function
def greet(name):
    print(f"Hello, {name}!")
greet("rahul")   

###############################################################################################
#  Function With Return Value and two argument 
def add(a,b):
    return a+b
result = add(2,5)
print(result)

###############################################################################################
# Function With Multiple Arguments (*args)
def addAll(*number):
    return sum (number)
res = addAll(2,3,4,5)
print(res)