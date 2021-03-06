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

def freq_array(k):
    frq = {}
    for i in range(4**(k-1)):
        frq[i] = 0
    return frq

def pattern_counter(text,k):
    txt_len = len(text)
    frq_arr = freq_array(k+1)
    for i in range(txt_len-k+1):
        pattern = text[i:i+k]
        pat_num = pat_to_num(pattern)
        frq_arr[pat_num] += 1
    return frq_arr
    

printer = pattern_counter("AGTATCGCCCTCTTTGAAGTCCTTTTTTGTTACATGCACCCGAGTTTAAGATTAACCGCGCGTGTTACCCCGTGGAACGAATCATGGGTCTGCTCCTGAGCATGACAACGGAAGGGGGAAATCCCCCAAGACCATTTAATAAACGCCGCCTCGCACCTGTCAATGCCGAAATTCCAACGAACAAGGTCAGGAGTGTCCCTATCGTATGGCTACCGCCTAGATCTGACGTGTTCTAGCGTCGAGGTCCCAGCAGAGCAGGCATAAGCCATCGGTCGGTGACACTTGCACATGCGGTCTGACCCTGCGCATCGGGACTACGTGATATGAGTAACCCAGATTTCCACTGTTTCAGCCTCGCCACCCCGCGGCTTGGCTGAATGACGTAGCCAACATATACAAGATCCGGGTGATCGAGTCTCTGTAAACAGCCGTGCGATCAAATCCAGGTACGCCGTGAATTAATCGCTCCACATCATTATAAAGTGCGAGCTATCCCGGCCGTGGTAGGCGTCTACAGATGTAATCGTTTCCTGGAGCCAACGCTGTGGTTAAAGTTGCCGATAGTCCCAGCGTTGTGAGCAACTTTACGAGGCCGCCTTGGCAGACGGGCAGCCGGTGGT", 5)
final = ""
for i in range(len(printer)):
    final+=str(printer[i])+" "
print final
    
    
