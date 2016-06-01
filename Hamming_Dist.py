def hamming_dist(seq1, seq2):
    assert len(seq1) == len(seq2)
    return sum(n1 != n2 for n1, n2 in zip(seq1, seq2))

sequences = open("rosalind_hamm.txt").read()
seq1, seq2 = sequences.split()

value = hamming_dist(seq1, seq2)
print(value)