import math
import sympy as smp
from sympy.simplify.fu import fu

x=smp.symbols('x')
#This software is valid for integrands with only one maximum of fourth derivative, it is a wide class of functions but there still a lot of nonvalid ones.

def max_of_function(func,edge_a,edge_b):
    #searching maximum using dihothomy method
    #accuracy  of searching maximum method and parametr delta of algorithm 
    eps_of_maximum_search = 0.00001
    delta =eps_of_maximum_search/2
    low_edge=edge_a
    high_edge=edge_b

    #cycle in which we find out only maximum in [a,b] choosing one of the intervals - left or right depends on inequality f(x_lower)<f(x_higher)
    while high_edge-low_edge>=eps_of_maximum_search:
        x_lower=.5*(low_edge+ high_edge)-delta
        x_higher=.5*(low_edge+ high_edge)+delta
        if (func.subs(x,x_lower)<func.subs(x,x_higher)):
            low_edge=x_higher
        else:
            high_edge=x_lower
    
    #return value of maximum
    return function.subs(x,low_edge)





#accuracy of result

eps =0.00001
function =smp.sympify(input("Enter integrand f(x) (ex. 3*x**2+sin(x)-exp(x)):  "))

print("Enter a and b for integral: ")
a=float(input("Enter a: "))
b=float(input("Enter b: "))

max_of_derivative = math.fabs(max_of_function(smp.diff(function,x,x,x,x),a,b))
h=(180*eps/(max_of_derivative*(b-a)))**(1/4)
n=math.ceil(.5*(b-a)/h)
h=(b-a)/(2*n)
integral_sum=function.subs(x,a)
integral_sum+=function.subs(x,b)


for i in range(1,2*n):
    if i%2==0:
        integral_sum+=2*function.subs(x,a+i*h)
    else:
        integral_sum+=4*function.subs(x,a+i*h)

integral_sum*=h/3

print("Integral equals to: "+str(integral_sum))



