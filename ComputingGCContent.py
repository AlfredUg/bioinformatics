from Bio import SeqIO
from Bio.SeqUtils import GC
name = ""
content = 0
 
fasta_seqs = SeqIO.parse(open("gc_content.txt"), 'fasta')
 
for fasta in fasta_seqs:
    name, sequence = fasta.id, fasta.seq
    if content < GC(sequence):
        content = GC(sequence)
        name = name
    print(name)
    print('%f%%' % content)

# def parse_fasta(fasta_lines):
#     fasta_dict = {}
#     lines = fasta_lines.strip().split('>')
#     
#     for line in lines:
#         if len(line) == 0:
#             continue
#         
#         fasta = line.split()
#         name = fasta[0]
#         sequence = ''.join(fasta[1:])
#         
#         fasta_dict[name] = sequence
#         
#     return fasta_dict
# 
# def calc_gc_content(sequence):
#     n = len(sequence)
#     content = 0
#     
#     for bases in sequence:
#         if bases == 'G' or bases == 'C':
#             content += 1
#             print(content)
#     
#     return 100 * (float(content) / n)
# 
# if __name__ == "__main__":
# 
#     fasta_lines = open("gc_content.txt").read()
#         
#     seqs = parse_fasta(fasta_lines)
#     seqs = dict([(name, calc_gc_content(seq)) for name, seq in seqs.items()])
#     
#     highest_name = None
#     highest_content = 0
#     
#     for name, content in seqs.items():
#         print(content)
#         if content > highest_content:
#             highest_name = name
#             #print(highest_name)
#             hightest_content = content
#             #print(content)
#     
#     print(highest_name)
#     print('%f%%' % highest_content)
