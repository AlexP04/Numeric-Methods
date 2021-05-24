import math
import sympy as smp

x =smp.symbols('x')

#eps - accuracy of method
eps = 0.00001

function=smp.sympify(input("Enter function f(x) (ex. x**5+3.5*x**2+x+0.333): "))
print("Enter [a,b] - interval, where only one solution of f(x)=0 exists (can be find graphicaly):")
a=float(input("Enter a : "))
b=float(input("Enter b : "))

# c  - middle of [a,b].
c=.5*(a+b)

while math.fabs(function.subs(x,c))>=eps:
	if function.subs(x,c)*function.subs(x,a)<0:
		b=c
	else:
		a=c
	c=.5*(a+b)

print("Solution of f(x)=0 equation on interval [a,b]: "+str(c))


		