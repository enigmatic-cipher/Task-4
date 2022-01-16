# Given n as input. Print product of all numbers from 1 to n.

n = 5
prod = 1
count = 1
for i in range(1,n+1):
  prod = prod * count
  count = count + 1
print(prod)


