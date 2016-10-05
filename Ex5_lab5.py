
# coding: utf-8

# In[12]:

v = list(map(int, input().split()))

a = [ 1 for i in range(v[0])]
for i in range(v[0], v[1] + 1):
    a.append(sum(a))
    a.pop(0)
    
print(a[v[0] - 1])
    

