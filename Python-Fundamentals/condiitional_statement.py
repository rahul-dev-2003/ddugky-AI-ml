# if - elseif-else(syntax)

age =21
if(age >=18):
    print("you are eligibale to voat")
    print("you can drive")
else:
    print("you are not eligible to boat")
    print("you can not drive")  


# elif 
light= "red"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("ready")
else:
    print("wrong signal")    

# Student marks
marks = int(input("Enter your marks"))
if(marks>90 & marks>80):
    print("A")
elif(marks>80 & marks>60):
    print("A")
elif(marks>60 & marks>40):
    print("A")
elif(marks>40 & marks>30):
    print("pass")
elif(marks>30 & marks>25):
    print("fail")
else:
    print("invalid number")        

######3#### nested if  conddition
num = 10
if(num > 0):
    print("number is positive")
    if(num % 2==0):
        print("number is even")
    else:
        print("number is odd")
else:
    print("number is not positive")


######3#####3###########3#3#######3#3##############3#
# compare of 3 numbers
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))

if(num1>num2):
    if(num1>num3):
        print(num1,"num1 is gretest")
    else:
        print(num3,"num 3 gretest")
elif(num2>num3):
    print(num2,"num 2 is gretest")
else:
    print(num3," num 3 is gretest")    

# # number clssification
num1 = int(input("enter number"))
if(num1>0):
    if(num1%2==0):
        print(" number is even")
    else:
        print("number is nagative")  

#################################################              
        

    

        



      
