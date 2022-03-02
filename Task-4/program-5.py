a=5
b=a-1                               # no of space
for i in range(0,a):                # for loop for row
    for j in range(0,b):            # for loop for spacing between start of line and *
        print(end=' ')              
    b=b-1                           # decreasing the no of space
    for k in range(0,i+1):          # for loop for printing star
        print('* ',end='')   
    print('\r')                     # new row


