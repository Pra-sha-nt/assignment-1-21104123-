#q1
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         
# Driver code
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')



#q2
n=int(input('enter no of rows:'))
for i in range(1,n+1):
    for j in range (0,n-i+1):
        print(' ', end='')
 
    # first element is always 1
    C = 1
    for j in range(1, i+1):
 
        # first value in a line is always 1
        print(' ', C, sep='', end='')
 
        # using Binomial Coefficient
        C = C * (i - j) // j
    print()


#q3
def find(n, m):
      
    # for quotient
    q = n//m
    print("Quotient: ", q)
      
    # for remainder
    r = n%m
    print("Remainder", r)
n=int(input('enter your 1st number:'))
m=int(input('enter your 2nd number:'))
# Driver Code
find(n,m )



#b
if (n and m)>>0:
    print('all values are non zero')
else:
    print('not')






#q4
class Student:                
 
 def __init__(self, name,number):
     


  
    self.name = name   
    self.number = number 
 
prashant = Student("Prashant",21)
 
print("my name is ",prashant.name,"and my roll no. is ",prashant.number)





#q5
class employe:                
 
 def __init__(self, name,salary): 
  
    self.name = name   
    self.salary = salary



 
mehak = employe("Mehak",40000)
ashok = employe("Ashok",50000)
viren = employe("Viren",60000)


mehak.salary=70000   #  a part of question 


 
print("Employe name:",mehak.name," , Employe salary:",mehak.salary)
print("Employe name:",ashok.name," , Employe salary:",ashok.salary)
print("Employe name:",viren.name," , Employe salary:",viren.salary)




#q6
import random

print('Type a word!')
i = 0
wordJ = ''

word = input()
word = str(word)
while i < len(word):
    wordJ = wordJ + word[random.randrange(len(word))]
    i = i + 1

print(wordJ)
