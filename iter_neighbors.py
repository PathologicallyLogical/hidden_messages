
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
    neighborhood = set(pattern)
    for i in range(d):
        for string in neighborhood:
            store = one_neighbors(pattern)
            neighborhood = neighborhood.union(store)
    neigh_arr = []
    for j in neighborhood:
        if len(j) == len(pattern):
            neigh_arr.append(j)
    return neigh_arr
    
