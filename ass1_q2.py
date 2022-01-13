x=float(input('enter your gross income\n'))
y=int(input('enter number of dependents\n'))
p=(x-10000-(3000*y))
s=p*0.2
print('income tax =', s)