# Project to plot the logical difference equation
# Equation >> f(x+1) = l*f(x)*(1-f(x))

# Importing libraries
import matplotlib.pyplot as plt
import random


def recursion(x0, dict, l, r):
    global n
    x1 = x0*l*(1-x0)
    if n <= r:
        dict[n] = x1
        n += 1
        return recursion(x1, dict, l, r)
    else:
        return


def check(x0, l, r):
    global n
    dict = {}
    recursion(x0, dict, l, r)
    return dict


x0 = random.uniform(0, 1)
l = random.uniform(0, 4)

while True:
    try:
        r = int(input("Enter the number of rounds: "))
        break
    except ValueError:
        print("Enter a valid number.")

print(f'The initial value is x is {x0}')  # To check which x
print(f'The initial value is l is {l}')
global n
n = 1
x = check(x0, l, r)

lists = sorted(x.items())

alpha, beta = zip(*lists)
plt.plot(alpha, beta)
plt.show()
