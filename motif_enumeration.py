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
    replace = ""
    for i in range(1,len(text)+1):
        for j in nucleotides:
            rep = text[:i-1]+j+text[i:]
            neighborhood.append(rep)
    return set(neighborhood)
    
def iter_neighbors(pattern,d):
    neighborhood = [pattern]
    if d == 0:
        return neighborhood
    for i in range(d):
        for string in neighborhood:
            store = one_neighbors(string)
            for j in store:
                if j not in neighborhood:
                    neighborhood.append(j)
    neigh_arr = set(neighborhood)
    return neigh_arr
    
def str_check(string,pat,d):
    neigh = iter_neighbors(pat,d)
    for i in range(len(string)-len(pat)+1):
        patt = string[i:i+len(pat)]
        if patt in neigh:
            return True

def motif_enumeration(dna,k,d):
    patterns = []
    for i in range(0,len(dna[0])-k+1):
        count = 0
        patt = dna[0][i:i+k]
        store = iter_neighbors(patt,d)
        for neighbor in store:
            for string in dna:
                if str_check(string, neighbor,d) == True:
                    count+=1
            if count >= (len(dna)):
                patterns.append(neighbor)
    patterns = set(patterns)
    return patterns
    


dna = ["AAAAA","AAAAA","AAAAA"]
a = motif_enumeration(dna,3,3)
