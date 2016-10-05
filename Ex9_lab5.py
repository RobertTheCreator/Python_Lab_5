
# coding: utf-8

# In[59]:

n = int(input())
a = list(map(int, input().split()))
k = int(input())

max = 0
for i in range(n - k + 1):
    if max < sum(a[i:k+i]):
        max = sum(a[i:k+i])
print(max)

