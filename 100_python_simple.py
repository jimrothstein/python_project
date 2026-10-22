import sys
# print('hi')

sum = 0
for i in range(10):
    sum+=i

    print(sum)


# ------------------------  version

print("python version ", sys.version)

#------------------------  cast


# cast
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

for letter in [x,y,z]:
    print(letter)

# ------------------------  unpack list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x, y, z)
#------------------------  function

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 

#------------------------ tuple
tu = (23, (4,5), 'a', 4.1, 7)

tu[0], tu[1], tu[-2]
tu
print(tu)
#------------------------ dislike 'global' 

# -------------------------  tuple concatenation

# concat 
(1,2,3) + (4,5,6) # (1,2,3,4,5,6)

# rep
(1,2,3)* 3 # means (1,2,3,1,2,3,1,2,3)



# Begin here:   https://www.w3schools.com/python/python_datatypes.asp


# -------------------------- read files
open("pyproject.toml")   # default is text (not binary), read
open("pyproject.toml", "rw") # read and write


# --------------------------   
f = open("pyproject.toml")
print(f)   # open is not enough to READ
print(f.read()) 


# --------------------------  use with,  
with open("pyproject.toml") as f:
  print(f.read(5)) 

#--------------------------  be sure to close, also readline

# ---- loop, every line
with open("pyproject.toml") as f:
  for x in f:
    print(x) 


# ----- delete file, check first 
import os

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") 


# ---- plot
import matplotlib


# 3.10.9
print(matplotlib.__version__)

# --- "pyplot" is module  ,  weird plots segments (0,0) to (6,250)
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

# ---- mean
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x) 

# ---- histogram 
# help(hist)
import numpy
import matplotlib.pyplot as plt

# mean=5, sd = 1, size = 100,000
x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show() 
# NeXT:    https://www.w3schools.com/python/python_ml_linear_regression.asp