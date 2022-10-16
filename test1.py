rows = int(input("input:"))+1
for i in range(0,rows):
    for j in range(0, rows - i):
        print(' ',end='')    
    for k in range(rows - i, rows):
        if(k == (rows-i) or i == (rows-1)):
            print(' *',end='')
        elif(k == rows-1):
            print(' * ',end='')
        else :
            print(' ',end=' ')
    print('')