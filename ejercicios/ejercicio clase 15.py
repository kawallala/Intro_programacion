D = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print D[6]
print sum(D)
print D.index(min(D)) + 1
M = []
for i in range(len(D)):
    if D[i] == max(D):
        M.append(i)
print M
L = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
for i in range(len(L)):
    print 'dias de', L[i], ':', D[i]


def minmes(l, d):
    print l[d.index(min(d))]


def maxmes(l, d):
    m = []
    for I in range(len(d)):
        if l[I] == 31:
            m.append(I)
    for I in m:
        print l[I]


agenda = [['a', 2], ['c', 1], ['d', 4]]
