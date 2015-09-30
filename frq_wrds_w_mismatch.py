def ham_distance(dna1,dna2):
    count = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            count+=1
    return count
    
def pat_to_num(dnastr):
    count = 0
    digit = len(dnastr)-1
    for i in dnastr:
        if i == "C":
            count+= 1 * (4**digit)
        elif i == "G":
            count+= 2 * (4**digit)
        elif i == "T":
            count+= 3 * (4**digit)
        digit -=1
    return count

def num_to_pat(num, k):
    digit = k-1
    store = num
    final = ""
    for i in range(k):
        if num - 3*(4**(digit)) >= 0:
            final += "T" 
            num -= 3*(4**(digit))
        elif num - 2*(4**(digit)) >= 0:
            final += "G"
            num -= 2*(4**(digit)) 
        elif num - (4**(digit)) >= 0:
            final += "C"
            num = num- (4**(digit)) 
        else: 
            final += "A"
        digit = digit-1
    return final

nucleotides =  ["G","C","A","T"]

def neighbors(text,d):
    if d == 0:
        return text
    if len(text) == 1:
        return nucleotides
    neighborhood = []
    suffix_neighbors = neighbors(text[1:],d)
    for string in suffix_neighbors:
        if ham_distance(text[1:], string) < d:
            for x in nucleotides:
                neighborhood.append(x+string)
        else:
            neighborhood.append(text[:1]+string)
    return neighborhood

    
def approx_pat_count(pat,text,d):
    count = 0
    num = len(text) - len(pat)
    for i in range(0,num+1):
        patt = text[i:i+len(pat)]
        thing = ham_distance(pat,patt)
        if thing <= d:
            count +=1
    return count
            
def frq_wrds_w_mismatch(text,k,d):
    frq_pat = []
    close = []
    frq_arr = []
    big = 4**k-1
    for i in range(big):
        close.append(0)
        frq_arr.append(0)
    for i in range(len(text) - k):
        neighborhood = neighbors(text[i:i+k],d)
        for pattern in neighborhood:
            index = pat_to_num(pattern)
            close[index] = 1
    for i in range(big):
        if close[i] ==1:
            pat = num_to_pat(i,k)
            frq_arr[i] = approx_pat_count(pat,text,d)
    max_count = 0
    for i in range(len(frq_arr)):
        if frq_arr[i] > max_count:
            max_count = frq_arr[i]
    for i in range(big):
        if frq_arr[i] == max_count:
            pattern = num_to_pat(i,k)
            frq_pat.append(pattern)
    return frq_pat
   
