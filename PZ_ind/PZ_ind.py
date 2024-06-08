f = open(r'320_24.txt')
f_r = f.read()
count = 0
max_count = 0
i = 0
while i < len(f_r):
    if (f_r[i]=='A' or f_r[i]=='E') and (f_r[i+1]=='C' or f_r[i+1]=='D' or f_r[i+1]=='F'):
        count += 1
        i += 2 
        if max_count < count:
            max_count = count
    else:
        count = 0
        i += 1
print(max_count)