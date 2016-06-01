#BioPython is one of the easiest ways to accomplish this problem.
from Bio import SeqIO
from Bio.SeqUtils import GC

#Setting global variables
name = ""
content = 0

#Read in the data provided by Rosalind
fasta_seqs = SeqIO.parse(open("gc_content.txt"), 'fasta')

#Loop through the fasta entries
for fasta in fasta_seqs:
    name, sequence = fasta.id, fasta.seq
    #If the content # is greater than the existing content #, overwrite it
    #This is necessary since the question is asking for the ID of the string that
    #has the highest amount of GC content
    if content < GC(sequence):
        content = GC(sequence)
        name = name
    print(name)
    print('%f%%' % content)
