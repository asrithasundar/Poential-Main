import numpy as np
from numpy.typing import ArrayLike

import matplotlib as mpl
import matplotlib.pyplot as plt
#def a quadratic equation
def quadratic_potential(a: float, b: float, c: float, x: ArrayLike) -> ArrayLike:
    """
     calculate the value of quadratic equation for  given a,b,c,x
    Args:
        a: coefficient of x^2
        b: coefficient of x
        c: constant
        x:x_value

    Returns:f(x)


    """
    return  a * x**2 + b * x + c

result = quadratic_potential(2,-1,3,-3)
print("f(x)=", result)


#plot a quadratic function
#define a plot function
def  plot_quadratic_pot(x_values,y_values,title,xlabel,ylabel,save_fig) -> None:

    plt.plot(x_values,y_values,label="f(x)=ax^2 + bx + c",color="blue",linewidth=2,marker=".",markerfacecolor="black",markersize=4)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(save_fig)
    plt.show()


a,b,c =(3,-3,4)
print("y=", quadratic_potential(3,-3,4,1))
x_values = np.linspace(-5,5,150)
y_values = quadratic_potential(a,b,c,x_values)
plot_quadratic_pot(x_values,y_values,"Quadratic Potential Plot","x","f(x)",f"f(x)={a}x^2+{b}x+{c}.pdf")


def linear_potential(m: float, b: float, x: ArrayLike)-> ArrayLike:
    """
define a linear function
    Args:
        m:slope of the line
        b:intercept of the line
        x:x_value

    Returns:f(x)

    """
    return m * x + b
result = linear_potential(2,3,1)
print("f(x)=", result)

def  plot_linear_pot(x_values,y_values,title,xlabel,ylabel,save_fig ) -> None:

    plt.plot(x_values,y_values,label="f(x)=mx+c",color="k",linewidth=2,marker=".",markerfacecolor="#cc2529",markersize=4)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(save_fig)
    plt.show()


m,b =(10,1)
print("y=", linear_potential(10,1,2))
x_values = np.linspace(-5,5,150)
y_values = linear_potential(m,b,x_values)
plot_linear_pot(x_values,y_values,"Linear potential Plot","x","f(x)",f"f(x)={m}x+{b}.pdf")



def double_well_potential(a:float ,b:float, c:float, x:ArrayLike)->ArrayLike:
    """
    calculate the double well potential
    Args:
        a: coefficients
        b:coefficients
        c: coefficients
        x: array of x values

    Returns:double well potential for all x


    """
    return a * x**4 - b * x**2 + c
result = double_well_potential(2,3,1,1)
print("v(x)=", result)

def  plot_double_well_potential(x_values,y_values,title,xlabel,ylabel,save_fig ) -> None:

    plt.plot(x_values,y_values,label="f(x)=mx+c",color="red",linewidth=2,marker=".",markerfacecolor="k",markersize=4)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(save_fig)
    plt.show()


a,b,c=(2,4,1)
print("v(x)=", double_well_potential(10,1,2,1))
x_values = np.linspace(-2,2,50)
y_values = double_well_potential(a,b,c,x_values)
plot_double_well_potential(x_values,y_values,"Double Well Potential Plot","x","v(x)",f"v(x)={a}x^4+{b}x^2+c.pdf")
#