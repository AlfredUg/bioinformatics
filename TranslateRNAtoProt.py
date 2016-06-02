#A simple way of completing this problem is to 
#use a dictionary of amino acids
protein_map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
       "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

def RNAtoprot(seq):
    #Initialize the protein variable
    protein = ''
    #get the location of the last codon
    last_codon = len(seq) - 2
    #loop through the string, using range's third optional attribute
    #to increase the step by 3 each time
    for start in range(0,last_codon,3):
        codon = seq[start:start+3]
        #Stop the loop when the code reaches a stop codon
        if codon == "UAG" or codon == "UAA" or codon == "UGA": break;
        #Retrieve the amino acid from the dictionary
        aminoacid = protein_map.get(codon)
        #Add the amino acid to the existing string
        protein = protein + aminoacid
    return protein

with open ("rosalind_prot.txt", "r") as rnafile:
    seq = rnafile.readline()

result = RNAtoprot(seq)
print(result)