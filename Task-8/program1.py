import numpy as np
q=[]
a=np.array([0,0,0,0,0])
b=int(input("Enter first number:"))
c=int(input("Enter last number:"))

for i in range(b,c+1):
    q.append(i)
    if i !=c:
        for j in a:
            q.append(j)
q = np.array(q)
print(np.float_(q))

