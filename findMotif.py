def findMotif(seq1, seq2):
    #find the length of the motif so we know what value
    #to add onto the start value
    seq2len = len(seq2)
    #loop through the sequence
    for start in range(0,len(seq1)):
        #if the substring is equal to the motif
        if seq1[start:start+seq2len] == seq2:
            #then print the start location of the substring
            print(start+1)
            
with open ("rosalind_subs.txt", "r") as motiffile:
    seq1, seq2 = motiffile.read().split()

result = findMotif(seq1, seq2)
