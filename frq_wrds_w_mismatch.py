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
    
def approx_match(pat,text,d):
    e = len(pat)
    final = ""
    for i in range(len(text) - e+1):
        bit = text[i:i+e]
        diff = ham_distance(pat,bit)
        if diff <= d:
            final+=str(i)+" "
    return final
            
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
            close[index] == 1
    for i in range(big):
        if close[i] ==1:
            pattern = num_to_pat(i,k)
            frq_arr[i] = approx_pat_count(text,pattern,d)
    max_count = max(frq_arr)
    for i in range(big):
        if frq_arr[i] == max_count:
            pattern = num_to_pat(i,k)
            frq_pat.append(pattern)
    return frq_pat
    

        
        
        
        
        
        
        
        
