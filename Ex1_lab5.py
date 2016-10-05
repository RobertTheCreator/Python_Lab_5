
# coding: utf-8

# In[65]:

a = [1, 2, 3, 4, 5]
a = [print(a[i], end = ' ') for i in range(len(a)) if i % 2 == 0]
print('')
a = [1, 2, 3, 4, 5]
a = [print(a[len(a) - 1 - i], end = ' ') for i in range(len(a))]
print('')
a = [1, 2, 3, 2, 1]
print(max(a), a.index(max(a)), end = ' ')

