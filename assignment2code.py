#Ans1
a=('python is a case sensitive langauge ')
#a
print(len(a)) 
#b
print(a[::-1])
#c            
print(a[10:-9])
#d
print(a.replace('a case sensitive', 'object orentated'))
#e
print(a.index('a'))
#f
print(a.replace(' ', ''))

#Ans2
intro ='''Hey, <|NAME|> Here!
My SID is <|ID|>
I am from <|BRANCH|> and my CGPA is <|cgpa|>'''
Name= (input('enter your name\n'))
id= (input('enter your sid\n'))
branch= (input('enter your branch\n'))
cgpa=(input('enter your CGPA\n'))
intro=intro.replace("<|NAME|>" , Name)
intro=intro.replace("<|ID|>", id)
intro=intro.replace("<|BRANCH|>", branch)
intro=intro.replace('<|cgpa|>', cgpa)
print(intro)

#Ans3
a=56
b=10
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b<<2)
print(a>>2)
print(b>>4)

#Ans4
a=int(input('enter 1st no.\n'))
b=int(input('enter 2nd no.\n'))
c=int(input('enter 3rd no.\n'))
if a>b:
    f1=a
else:
    f1=b
if f1>c:
    print('greaest no. is ', f1)
else:
    print('greatest no. is',  c)

#Ans5
a=str(input('enter name\n'))
found='name not exist'
for i in ['sonu','monu','tony','steve']:
    if i==a:
        found='name exist'
print(found)

#Ans6
a=int(input('side 1st\n'))
b=int(input('side 2nd\n'))
c=int(input('side 3rd\n'))
result= 'no'
if (a+b>c)&(b+c>a)&(c+a>b):
    result='yes'
print(result)
