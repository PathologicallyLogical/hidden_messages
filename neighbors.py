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
    for i in range(len(text)):
        symbol = text[i]
        for j in nucleotides:
            if j != symbol:
                for m in range(len(text)):
                    if m != i:
                        replace += text[m]
                    else:
                        replace +=j
                neighborhood.append(replace)
            replace = ""
    return neighborhood
    
def neighbors(text,d):
    fin_arr = []
    x = one_neighbors(text)
    for i in range(d):
        for j in x:
            y = one_neighbors(j)
            for k in y:
                fin_arr.append(k)
        x = y
    fin = list(set(fin_arr))
    return fin
            
    
    
x = neighbors("CTGCCAGG",3)
final = ""
for i in x:
    print i
    
    
