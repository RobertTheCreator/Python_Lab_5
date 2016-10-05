
# coding: utf-8

# In[2]:

a = list(map(int, input().split()))
t = int(input())
for i in range(t):
    a.insert(-1 - a[-1], a[-1])
    a.pop()
for i in range(len(a)):
    print(a[i], end = ' ')

