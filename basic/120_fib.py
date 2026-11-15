# REF: https://web.engr.oregonstate.edu/~huanlian/teaching/ML/2025fall/extra/python-numpy.pdf
# 120_fib.py
print(" ------ fib")
# fib
a,b = 0,1
while b <= 1000:
    print(b)
    a,b = b, a+b


print(" ---  if-else")

    
if 4 > 5:
    print (True)
else:
    print (False)


    print("---- factorial")

def fact(n):
  if n == 0:
   return 1
  else:
   return n * fact(n-1)


print(fact(4))

print("--------- list, begin with 0")
a = [1,'python', [2,'4']]
print(len(a))  # 3
print(a[1])  # python
print(a[2])
print(a[2][1]) # 4
