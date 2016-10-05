
# coding: utf-8

# In[23]:

a = list(map(int, input().split()))
for i in range(5):
    if (a[i] == 2) and (a[i+1] != 2):
        a.pop(i)
print(sum(a)//len(a))

