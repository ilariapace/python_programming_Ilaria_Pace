#Exercise1:
#
L = list(range(21,40))
#
for i in L:
    if i%2 == 0:
        print(i)
#
for i in L:
    if i%3 == 0:
        print(i)

#Exercise2:
print(L[-2:])

#Exercise3:
'''Wrong:
    L = ['1', '2', '3']
    for i in range(10)
        if i in L:
        print(i is in the list)
        else:
        print(i not found)
wrong indent
wrong arguments.'''
#
for i in range(10):
    if str(i) in L:           #str() to define i as a string
        print(i, 'is in the list')  #'' to print the argument as a string
    else:
        print(i, 'not found')

#Exercise4:
#
fasta_file = open('sprot_prot.fasta')
seq_fasta = fasta_file.readlines()
first_line = seq_fasta[0]
f_line = first_line.split('OS=')
print(f_line[1])

#Exercise5:
second_element = f_line[1]
s_element = second_element.split()
concat = s_element[0] + s_element[1]
#
concat = s_element[0:2] # the first and second element in the same variable


#Exercise6:
#
a = 'asor rosa'
b = a[::-1]  #reverse of the string in a

#Exercise7:
#
L = [1, 7, 3, 9]
L.sort()

#Exercise8:
#
L = [1, 7, 3, 9]
List2 = []
for i in L:
    if i not in List2:
        List2.append(i)
        List2.sort()
    print(List2)

#Exercise9:
#
T = [[2,4] , [3,6]]
file = open('table_file.txt', 'w')
file.write('2\t 4 \n 3\t 6')
([[2,4] , [3,6]])  #list of list = table


