#INCOMPLETE
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
    
def str_check(string,pat,d):
    for i in range(len(string)-len(pat)+1):
        patt = string[i:i+len(pat)]
        if patt ==pat:
            return True
    
def motif_enumeration(dna,k,d):
    patterns = []
    for i in range(0,len(dna[0])-k+1):
        patt = dna[0][i:i+k]
        store = iter_neighbors(patt,d)
        print(len(store))
        for neighbor in store:
            count = 0
            for string in dna:
                if str_check(string, neighbor,d) == True:
                    count+=1
            print(count)
            if count >= len(dna):
                patterns.append(neighbor)
    return patterns
    
    
dna = ["ATTTTAAGAACATTCATGGAAAGCG","TCTAGAGGGAGTTGTTTAAGCAGGG","AATAGTCGTCCGACCAGGCATCTGA","CTGTACAGACGGAATATAAGACGTA","TTCTAGGTCGCGCCCAGGTAACACG","AGGTATTAGACAGATATGGCAAAGC"]
