import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([1,2,3,4,5])
c=True
for i in range(0,a.__len__()):
    if a[i]==b[i]:
        c=True
    else:
        c=False
        break
print(c)    # will give true if equal, false if they are not equal
