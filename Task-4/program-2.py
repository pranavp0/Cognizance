a=input("Enter string:")                # input
b=''
for i in range(0,len(a),2):             # looping will give even index
    b=b+a[i]                            # catenation
print(b)    
