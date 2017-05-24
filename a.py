a = ['4A', '4B', '4B-', '4B+', '4A','1B-']
a.append('4A')
a.append('4A')
a.append('4A')

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
    print(dengdip)

gpa = dengdi / xuefen
print(gpa)
