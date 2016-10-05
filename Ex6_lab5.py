
# coding: utf-8

# In[4]:

n = int(input())
a = list(map(int, input().split()))
while n > 0:
    mr = ml = 0
    for i in range(len(a)):
        if a[n-1] > a[i]:
            mr += 1
        if a[n-1] < a[i]:
            ml += 1
    if ml == mr:
        print(a[n- 1])
        break
    n -= 1

