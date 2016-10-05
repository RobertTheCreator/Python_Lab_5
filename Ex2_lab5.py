
# coding: utf-8

# In[118]:

a = [1, 2, 3, 4, 5]
for i in range(0, len(a) - 1, 2):
    a[i], a[i+1] = a[i+1], a[i]
print(a)

a = [1, 2, 3, 4, 5]
a.insert(0, a[-1])
a.pop()
print(a)

a = [1, 2, 2, 3, 3, 3]   
for i in range(len(a)):
    k = a.count(a[i])
    if k == 1:
        print(a[i], end = ' ')
print('')

a = [1, 2, 2, 4, 4, 4, 1, 4, 4, 4, 1, 3, 3, 3] 
max = 1
elem = a[0]
for i in range(len(a)):
    k = a.count(a[i])
    if max < k:
        max = k
        elem  = a[i]
print(elem)

