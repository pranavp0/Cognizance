from pickle import FALSE, TRUE


a=545
b=str(a)                            # string
c=''
for i in range(len(b)-1,-1,-1):     # reverse indexing
    c=c+b[i]                        # inverted string
if b==c:
    print('TRUE')
else:
    print('FALSE')
