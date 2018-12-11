'''
pseudocode:
open the file e read it.
do a for loop to read line by line, and a new file to write in.
define two variable for the seq e for the header.
ij the line vith '>' not  contains 'homo sapiens', put line in the variable, else increase the seq.
if is not of the homo sapiens, put in a variable the seq and the header and writr it in a file.
Do a split and join for the source organism, and len for the lenght.
'''

fastafile = open('sprot_prot.fasta')
fasta_read = fastafile.readlines()     #read thev file line by line

seq_fasta = open('sprot_prot.fasta')
seq = ''
header = ''
fastafile = open('fastafile.fa' , 'w')

for line in seq_fasta:
    if line[0] == '>':
        if "Homo sapiens" not in line:
            header = line
            s_line = header.split(OS=)
            second = s_line[1]
            s_second = second.split()
            organism = s_second[0] + s_second[1]
            print('the organism is:' , organism)    #for the source organism    
	else:
            if header:
                seq = seq + line
                len(seq)       #for the lenght of the sequence

if header:
    record = header + seq
    fastafile.write(record)
