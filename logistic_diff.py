# Plotting Chaos: To plot the logistic difference equation
# Equation >> f(x+1) = l*f(x)*(1-f(x))

# Importing libraries
import matplotlib.pyplot as plt
import random

# Function calculating the function values using recursion


def recursion(x0, dict, l, r):
    global n
    x1 = x0*l*(1-x0)
    if n <= r:
        dict[n] = x1  # Saving the key and values in dictionary >> dict(1) = f
        n += 1
        return recursion(x1, dict, l, r)
    else:
        return

# Outer function


def check(x0, l, r):
    global n
    dict = {}  # initialising dictionary which saves function values
    recursion(x0, dict, l, r)
    return dict


x0 = random.uniform(0, 1)  # x0 is the initial random value between 0 and 1
l = random.uniform(0, 4)  # l is the constant random value between 0 and 4

# Exception Handling for number of rounds

while True:
    try:
        r = int(input("Enter the number of rounds: "))
        break
    except ValueError:
        print("Enter a valid number.")

# To check which intial values were assumed

print(f'Value of Constant is  {l} and initial random value is {x0}')

global n
n = 1


x = check(x0, l, r)  # calling the outer function

# Sorting the dictionary for their key values
lists = sorted(x.items())
x_val, function_val = zip(*lists)

# Plotting the Values
plt.plot(x_val, function_val)
plt.title('Logistic Difference Graph')
plt.xlabel('Number of Rounds')
plt.ylabel('Value of Logistic Diff. Function')
plt.show()
