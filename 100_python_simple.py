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

#------------------------ dislike 'global' 

# Begin here:   https://www.w3schools.com/python/python_datatypes.asp



