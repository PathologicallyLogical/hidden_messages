
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
    
def ham_distance(dna1,dna2):
    count = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            count+=1
    return count
    
def min_distance(pattern,dna_string):
    min_dist = len(pattern)
    for i in range(len(dna_string)-len(pattern)+1):
        string_bit = dna_string[i:i+len(pattern)]
        difference = ham_distance(string_bit,pattern)
        if difference < min_dist:
            min_dist = difference
    return min_dist

def add_mins(pattern,dna_arr):
    count = 0
    for dna_str in dna_arr:
        count+= min_distance(pattern,dna_str)
    return count
    
def median_string(dna,k):
    distance = 100
    for i in range((4**k)-1):
        pat = num_to_pat(i,k)
        dist_thing = add_mins(pat,dna)
        if distance > dist_thing:
            distance = dist_thing
            median = pat
    return median
    
dna = ["TCCTCGCCGTTATCGTGTCGCCAATGTAAACAATCGGAGGTA","CACAGGCGTGAGCTATCCACAGCAGGGATCCGCCAACAACAC","AAATCGGTGGCTTTGCTATATAATCGCCAGTCGTCATATATC","TTGTTGAGTCCACGCCACTGTGGTACTCATAGCTAGGGCGAC","CCAATGCCCCATCGCCAAGCTGCTGCGGTCGTGTATTAACAA","TGCTTTGAGGAGTAGATGCGCCATAGCGAGCTCCCGCGGTTC","TGCCCCGGTTGGCGCCAGTCGTCCAGGTGCAAGCATGTGTCT","TCCAGCGTACTGAAACGCCGCCAGAACGCTAGCTTCAAGGTA","TTGAACCGCCACTAACGCACGTGCGGCACCCATGATTCCTGG","TTTGGTGACAAAAGAGGGCGCCACGTCCCCGAGTCAGGTACC"]

a = median_string(dna,6)
print(a)
        
        
        
        
        
        
        
