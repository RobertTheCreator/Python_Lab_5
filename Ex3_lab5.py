
# coding: utf-8

# In[20]:

a = list(map(int, input().split()))
k = 0
for i in range(len(a)):
    if i % 2 == 0:
        print(a[k], end = ' ')
        k += 1
    else:
        print(a[len(a) - k], end = ' ')

