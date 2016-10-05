
# coding: utf-8

# In[36]:

n= int(input())
a = [0]*n
for i in range(n):
    a[i] = list(map(int, input().split()))
t = int(input())
k = 0
for i in range(n):
    if a[i][0] <= t <= a[i][1]:
        k += 1
print(k)

