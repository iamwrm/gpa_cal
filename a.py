a = ['4A', '4B', '4B-', '4B+']
"first semester"

b = ['4A','1B-','3A-','2A-','1B']
"second semester"

for i in b:
    a.append(i)


dengdi = 0
xuefen = 0
for i in a:
    fen = int(i[0])
    deng = 4 + (ord('A') - ord(i[1])) * 0.9
    if(len(i) == 2):
        xuefen += fen
        dengdip = fen * (deng)
    else:
        xuefen += fen
        if i[2] == '+':
            dengdip = fen * (deng + 0.3)
        else:
            dengdip = fen * (deng - 0.3)
    dengdi += dengdip

gpa = dengdi / xuefen
print(gpa)
