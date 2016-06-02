from Bio import SeqIO

def calc_profile(seqs):
    #determine the length of one of the sequences
    seq_len = len(seqs[0])
    #initialize the dictionary containing the nucleotide
    #and the number of times it exists in the sequences
    profile = {'A':[0] * seq_len, 'G':[0] * seq_len, 'C':[0] * seq_len, 'T':[0] * seq_len}
    #loop through each sequence
    for i in range(seq_len):
        #loop through each nucleotide
        for base in seqs:
            #increment the counter for each nucleotide
            profile[base[i]][i] +=1
    return profile

def consensus(profile):
    #initialize a list
    con_list = []
    #grab the keys (i.e. the base pairs)
    base_keys = profile.keys()
    #iterate over the keys
    for i in range(len(profile[base_keys[0]])):
        val_max = 0
        base_max = None
        for key in base_keys:
            if profile[key][i] > val_max:
                 val_max = profile[key][i]
                 base_max = key
        con_list.append(base_max)
    
    return(''.join(con_list))
    

with open("rosalind_cons.txt", 'r') as cons_file:
    #Easiest way to parse the fasta file is to use BioPython
    #This way I can capture just the fasta string
    data = [str(fasta.seq) for fasta in SeqIO.parse(cons_file, 'fasta')]

result = calc_profile(data)
consensus_string = consensus(result)
print(consensus_string)

#to print the matrix, I need to iterate through the keys and print
#the value for each location
for key in sorted(result.keys()):
    print("%s: %s" % (key, ' '.join(map(str, result[key]))))