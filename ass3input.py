# ans1
string=input('enter string:')
word=input('enter word:')
a=[]
count=0
a=string.split(" ")
for i in range(0,len(a)):
    if (word==a[i]):
        count=count+1
print('count of the word is:')
print(count)







# ans2
year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))








# ans3
c=int(input('enter lower range:'))
d=int(input('enter upper range:'))
a=[(x,x**2) for x in range(c,d+1)]
print(a)










# ans4
x=int(input('enter grade point:'))
if 4==x:
    print('your grade D' )
elif 5==x:
    print('your grade C')
elif 6==x:
    print('your grade C+')
elif 7==x:
    print('your grade B  ')
elif 8==x:
    print('your grade B+')
elif 9==x:
    print('your grade A')
elif 10==x:
    print('your grade A+ ')
else:
    print("invalid input")





# ans5
row = int(input('Enter how many lines? '))

a = 65 # ASCII value for 'A'

# Generating pattern
for i in range(1,row+1):


    # for space
    for j in range(1, row+1-i):
        print(' ', end='')


    # for pattern
    for j in range(0, 2*i-1):
        print('%c' % (a+j), end='')
    
    
    
    
    
    # Moving to next line
    print()




# ans6
n=int(input('enter number of students:'))
dict={}
for i in range(n):
    p=input('enter student name:')
    dict[p]=int(input('enter student SID:'))
    print('Dictionary is', dict )




# ans7
# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))





# ans8
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}
set_a=(set1 | set2)-(set1&set2)
print("part a:",set_a)

set_b=(set1|set2|set3)-(set1&set2)-(set2&set3)-(set3&set1)
print('partb:',set_b)


set_c=(set1&set2)|(set2&set3)|(set3&set1)-(set1&set2&set3)
print('part c:',set_c)


list_d=[]
for i in set1:
    if i>=1 and i<=10:
        list_d.append(i)
    set_d=set(list_d)
    print('part d:', set_d)





list_e=[]
for i in (set1|set2|set3):
    if i>=1 and i<=10:
        list_e.append(i)
    set_eout=set(list_e)
    print('part e:',set_eout)


