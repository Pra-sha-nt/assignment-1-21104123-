# answer1
num1=int(input('enter your 1st number\n'))
num2=int(input('enter your 2nd number\n'))
num3=int(input('enter your 3rd number\n'))
x=(num1+num2+num3)/ 3
print( 'your average is' , x )

# answer 2
x=float(input('enter your gross income\n'))
y=int(input('enter number of dependents\n'))
p=(x-10000-(3000*y))
s=p*0.2
print('income tax =', s)

# answer 3
x=(['SID', 'Name','Course','CGPA'])
x[0]=int(input("enter your sid\n " ,))
x[1]=input("enter your name\n")
x[2]=input("enetr your course name\n")
x[3]=float(input("enter your cgpa\n"))
print(x)

# answer 4
num1=int(input('enter 1st student marks\n'))
num2=int(input('enter 2nd student marks\n'))
num3=int(input('enter 3rd student marks\n'))
num4=int(input('enter 4th student marks\n'))
num5=int(input('enter 5th student marks\n'))
x=[num1,num2,num3,num4,num5]
x.sort()
print(x)

# answer 5(a)
colour =['red','green','white','black','pink','yellow']
print(colour)
colour.pop(3)
print(colour)

# answer 5(b)
colour =['red','green','white','black','pink','yellow']
print(colour)
colour =['red','green','white','black','pink','yellow']
colour[3:5]=['purple']
print(colour)
