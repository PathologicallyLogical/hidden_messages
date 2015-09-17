def ham_distance(dna1,dna2):
    count = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            count+=1
    return count

def approx_match(pat,text,d):
    e = len(pat)
    final = ""
    for i in range(len(text) - e+1):
        bit = text[i:i+e]
        diff = ham_distance(pat,bit)
        if diff <= d:
            final+=str(i)+" "
    return final
    
#returns the indexes of all patterns in the text that have less than d differences from the pattern you're looking at
#because sometimes the sequence is there, just slightly mutated
