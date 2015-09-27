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
    final = ""
    for i in range(k):
        bla = 4**digit
        if num - 3*(bla) >= 0:
            final += "T" 
            num -= 3*(bla)
        elif num - 2*(bla) >= 0:
            final += "G"
            num -= 2*(bla) 
        elif num - (bla) >= 0:
            final += "C"
            num = num- (bla) 
        else: 
            final += "A"
        digit = digit-1
    return final

def freq_array(k):
    frq = []
    for i in range(4**k):
        frq.append(0)
    return frq

def comp_frq(text,k):
    txt_len = len(text)
    frq_arr = freq_array(k)
    for i in range(txt_len-k+1):
        pattern = text[i:i+k]
        pat_num = pat_to_num(pattern)
        frq_arr[pat_num] += 1
    return frq_arr

def clump_find(genome, k, L, t):
    frq_pat = [] 
    clump = []
    ks = (4**k)
    for i in range(ks):
        clump.append(0)
    text = genome[0:L]
    frq_arr = comp_frq(text,k)
    for i in range(ks):
        if frq_arr[i] >= t:
            clump[i]+=1
    for i in range(1,len(genome)-L+1):
        f_pat = genome[i-1:i+k-1]
        index = pat_to_num(f_pat)
        frq_arr[index] -= 1
        l_pat = genome[i+L-k:i+L]
        index = pat_to_num(l_pat)
        frq_arr[index] +=1
        if frq_arr[index] >= t:
            clump[index]+=1
    for i in range(ks):
        if clump[i] == 1:
            pattern = num_to_pat(i,k)
            frq_pat.append(pattern)
    return frq_pat
