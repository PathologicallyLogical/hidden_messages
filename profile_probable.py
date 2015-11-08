
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
    
def matrix_maker(matrix_string):
    big_arr = matrix_string.splitlines()
    final_arr = []
    for row in big_arr:
        new_row = row.split(" ")
        final_arr.append(new_row)
    for i in range(len(final_arr)):
        for num in range(len(final_arr[i])):
            final_arr[i][num] = float(final_arr[i][num])
    return final_arr

def matrix_searcher(letter,matrix_col, matrix):
    if letter == "A":
        matrix_row = 0
    elif letter == "C":
        matrix_row = 1
    elif letter == "G":
        matrix_row = 2
    elif letter == "T":
        matrix_row = 3
    return matrix[matrix_row][matrix_col]

new_matrix = """0.155 0.197 0.254 0.225 0.296 0.338 0.254 0.169 0.239 0.225 0.141 0.197 0.31 0.324
0.254 0.282 0.211 0.225 0.268 0.169 0.31 0.268 0.239 0.197 0.296 0.225 0.338 0.296
0.352 0.239 0.268 0.296 0.183 0.211 0.239 0.324 0.268 0.296 0.324 0.296 0.183 0.197
0.239 0.282 0.268 0.254 0.254 0.282 0.197 0.239 0.254 0.282 0.239 0.282 0.169 0.183"""

a = matrix_maker(new_matrix)
b = "CTCACTAAGGCTTAGTTATACTCGGTCGCATCTGGTGCAGCACGCAGGGGCTAAGTGTGTTCAAGCCCTGTACAGGAATATTCATGAGGTAGGGAGCGAAGCCACGCCCGGCCCACCAGCTCTAATTGATAAGAGGCATCGAACATAATCGAGTTATGCAGTCTCCACCTTTCGACCGCTTCATCCGACCCTTGCACACCTTGGGGGCTCACACGTTGTACGATTTCCTGGCTTCTGACAACGCGTATCGGTTACTACCCATTCTGCCTTCTTTGCACCGTCTCTGATGTTCTGCGATCGCCTCTCTCGTTAAACCCAAGCATACACACTCTTACAGGCTACGAGGACGGAGCGCTAATACGGACAATAGCACAACCTGCGCTCAGTCGTCCTTGACGTACTATTTCGTCATGATGGTGTCCATGATGTTTAGAAGATGAACCTAGTTTGGAACGCGCGGTACCTACTCTTGGGCCGAAATCAGTTGAAATGCAATCGTGAATCTGCCAAAACCTCACGTGACATCAAAAATATCGAGCTCGTCGCACCCGGCAAATGGTTCATGCCATTCCCGTACCCCAACCTCGTGTTGTGTTTTGGCTCACATATCTAAGCTTCTTCGTCCGGGCGTAACAAAAATCACTCTAGTGCCGCATGAATTACCTACACTACGGTTCAAGCATCTAGAGTGGGTTTGCGTAAGAACGCATCTGGCTGATAACAAGGTTGATCGCCCGAAGTGGTCCGATATCTCACCTAGTGGTCTAATTTGTGCGTAAGTGGCCATGCACCGTTATGAGTCTATTAGTCAAAAGAGCCTCGCCAAAGCGAAGGGTGACTTGCACATCAAAGCCTGTGGTTGGGTCTGTTGTAGCGCCCACGATTACGCCGGGTCATCCCACGTATCCAACTGTGATCTACTCCGCCCTGTGCGCCGCATCCAGGGATGTAGCGTGCGGCCTTCACTGCAAGTGTCTGCAAACTGCGATGTGATTTGCGG"

def profile_probable(dna_str,k,prob_matrix):
    max_prob = 0
    max_pattern = ""
    for i in range(len(dna_str)-k+1):
        str_bit = dna_str[i:i+k]
        str_prob = 1
        for i in range(k):
            character = str(str_bit[i])
            letter_prob = matrix_searcher(character,i,prob_matrix)
            str_prob *= letter_prob
        if str_prob > max_prob:
            max_pattern = str_bit
            max_prob = str_prob
    return max_pattern, max_prob
            
        

c = profile_probable(b,14,a)












        
        
        
        
        
        
        
