
# coding: utf-8

# In[47]:

def fac(n):
    if n == 0:
        return 1
    else:
        k = 1
        while n > 1:
            k *= n
            n -= 1
        return k
    
n = int(input())
for i in range(n+1):
    for k in range(i+1):
        print(int(fac(i)/(fac(k)*fac(i - k))), end = ' ')
    print('')

