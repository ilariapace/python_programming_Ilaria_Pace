seq1= 'ATGCCG'
seq2= 'AGCC'
#match = 2
#mismatch = -1
gap = -1
sub = { 'A':{'A':2, 'C':-1, 'G':-1, 'T':-1},\
        'C':{'A':-1, 'C':2, 'G':-1, 'T':-1},\
        'G':{'A':-1, 'C':-1, 'G':2, 'T':-1},\
        'T':{'A':-1, 'C':-1, 'G':-1, 'T':2}}

c = len(seq2)+1
r = len(seq1)+1
max_score = 0
max_pos = None
M = [[0 for j in range(c)] for i in range(r)]
T = [['0' for j in range(c)] for i in range(r)]
for j in range(1,c):
    for i in range(1,r):
        scores = []
        if seq1[i-1]==seq2[j-1]:
            diag_score = M[i-1][j-1] + sub[seq1[i-1]][seq2[j-1]]  #match
        else:
            diag_score = M[i-1][j-1] + sub[seq1[i-1]][seq2[j-1]]  #mismatch
        up_score = M[i-1][j] +gap
        left_score = M[i][j-1] +gap
        scores = [diag_score, left_score, up_score, 0]
        M[i][j]= max(scores)
        if max(scores) == diag_score:
            T[i][j]='D'
        elif max(scores) == up_score:
            T[i][j]='U'
        else:
            T[i][j]='L'

        if max(scores) > max_score:
            max_score = max(scores)
            max_pos = (i,j)

def prettymatrix(m):
    for i in m:
        print i

print 'Score_Matrix:'
prettymatrix(M)
print ' '
print 'Traceback_Matrix:'
prettymatrix(T)
print ' '
print 'The highest score is: %f' %max_score
print 'The cell with the highest score is in position: %s' %(max_pos, )
