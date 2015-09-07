def pattern_count(text, pattern):
    count = 0
    pat_len = len(pattern)
    txt_len = len(text)
    for i in range(txt_len-pat_len+1):
        if text[i:i+pat_len] == pattern:
            count +=1
    return count
    
def freq_words(text,k):
    freq_pat = []
    count = [1,2,3]
    for i in range(len(text) - k):
        pattern = text[i:i+k]
        count.append(pattern_count(text, pattern))
    max_count = max(count)
    for i in range(len(text) - k+1):
        temp = text[i:i+k]
        if pattern_count(text,temp) == max_count:
            freq_pat.append(temp)
    frq_pat = set(freq_pat)
    return frq_pat
    
a = "GCCTGAAGCTCCAAGTCTTTTCGCTCCAAGTCTTTTCGCTCCAAGCCTGAAGTCTTTTCGCTCCAATCCCTCCGGCCTGAACGCCGTGCTGTCTTTTCCGCCGTGCTTCCCTCCGTCCCTCCGGCCTGAACGCCGTGCTGTCTTTTCGCCTGAACGCCGTGCTCGCCGTGCTTCCCTCCGGCTCCAAGCTCCAATCCCTCCGCGCCGTGCTTCCCTCCGCGCCGTGCTGTCTTTTCGTCTTTTCGTCTTTTCGCCTGAAGTCTTTTCGCCTGAAGCCTGAACGCCGTGCTGCCTGAAGCTCCAACGCCGTGCTCGCCGTGCTCGCCGTGCTCGCCGTGCTGCCTGAACGCCGTGCTGTCTTTTCGTCTTTTCGTCTTTTCGCTCCAACGCCGTGCTTCCCTCCGTCCCTCCGTCCCTCCGGCTCCAATCCCTCCGGTCTTTTCTCCCTCCGGCCTGAAGCCTGAAGCTCCAAGCTCCAACGCCGTGCTTCCCTCCGGTCTTTTCGTCTTTTCGCCTGAAGTCTTTTCGCCTGAAGCCTGAATCCCTCCGTCCCTCCGGTCTTTTCGCTCCAATCCCTCCGTCCCTCCGGTCTTTTCGCTCCAAGCTCCAATCCCTCCGCGCCGTGCTGTCTTTTCCGCCGTGCTGCCTGAAGCCTGAAGTCTTTTCGCTCCAAGCTCCAACGCCGTGCTGCCTGAAGCCTGAAGCCTGAAGCTCCAAGCCTGAAGCTCCAAGCTCCAAGTCTTTTCGTCTTTTCGTCTTTTCGCCTGAATCCCTCCGTCCCTCCGGCCTGAAGCTCCAAGCCTGAAGCTCCAATCCCTCCGTCCCTCCGGCTCCAATCCCTCCGCGCCGTGCTCGCCGTGCT"
b = 13
c = "ACG"

freq_words(a,b)
