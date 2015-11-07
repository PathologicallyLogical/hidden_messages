def ham_distance(dna1,dna2):
    count = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            count+=1
    return count

nucleotides =  ["G","C","A","T"]


def one_neighbors(text):
    if len(text) == 1:
        return nucleotides
    neighborhood = [text]
    for i in range(1,len(text)+1):
        for j in nucleotides:
            rep = text[:i-1]+j+text[i:]
            neighborhood.append(rep)
    return set(neighborhood)
    
def iter_neighbors(pattern,d):
    neighborhood = [pattern]
    if d == 0:
        return neighborhood
    if d == 1:
        return one_neighbors(pattern)
    for i in range(d):
        for k in neighborhood:
            store = one_neighbors(k)
            for j in store:
                if j not in neighborhood:
                    if ham_distance(pattern,j) <= d:
                        neighborhood.append(j)
    neigh_arr = set(neighborhood)
    return neigh_arr

def string_checker(string,pattern,d,original_patt):
    pattern_neigh = iter_neighbors(pattern,d)
    for a in range(len(string) - len(pattern)+1):
        string_bit = string[a:a+len(pattern)]
        if string_bit in pattern_neigh:
            return True
    else: 
        return False
        

def motif_enumeration(dna,k,d):
    patterns = []
    for i in range(len(dna[0])-k+1):
        patt = dna[0][i:i+k]
        count = 0
        patt_neighbors = iter_neighbors(patt,d)
        for pattern in patt_neighbors:
            count = 0
            for string in dna:
                if string_checker(string,pattern,d,patt) == True:
                    count+=1
                if count == len(dna):
                    patterns.append(pattern)
    patterns = set(patterns)
    for thing in patterns:
        print(thing)
    return patterns

dna = ["CTCCGGTCGAATTCTCAGTAGCCTT","TGCTCCATGCCACAGCCCTGGCATT","GGCTCTTGCACTTGTTTTAAGCGTT","GCCTAGCCTTGACGACTTGGGATGC","CTTATGCTTTGTCTCGGAGCCTTTC","AGTTTATGGCGCCAAGCTTTCCAAC"]

a = motif_enumeration(dna,5,1)
