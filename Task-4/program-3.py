a=[[1,'Abc',90],[2,'Def',95],[3,'Ghi',85]]          # input list
b=['Rollno','Name','Marks']                         # input list column name
for i in range(0,len(b)):                           # printing column names
    print(b[i],end='   ')
print()    
for j in range(0,len(a)):                           # printing rows
    print()
    for i in range(0,len(a)):
        print(a[j][i],end='       ')
print('\n')        
for i in range(1,2):
    for j in range(0,len(a)):
        print(a[i][j],end='       ')
