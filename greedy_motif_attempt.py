def pat_to_num(dnastr):
    #returns a number given a pattern
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
#returns a pattern given a number
    
def ham_distance(dna1,dna2):
    count = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            count+=1
    return count
#given two dna strings, returns the numeric difference between them
    
def min_distance(pattern,dna_string):
    min_dist = len(pattern)
    for i in range(len(dna_string)-len(pattern)+1):
        string_bit = dna_string[i:i+len(pattern)]
        difference = ham_distance(string_bit,pattern)
        if difference < min_dist:
            min_dist = difference
    return min_dist
#given a pattern and a long string, finds the lowest possible ham_distance between the two

def add_mins(pattern,dna_arr):
    count = 0
    for dna_str in dna_arr:
        count+= min_distance(pattern,dna_str)
    return count
#the score function, returns all min_distances of dna in an array, added together
    
def median_string(dna,k):
    distance = 100
    final = []
    for i in range((4**k)-1):
        pat = num_to_pat(i,k)
        dist_thing = add_mins(pat,dna)
        if distance > dist_thing:
            distance = dist_thing
            median = pat
    for i in range((4**k)-1):
        pat = num_to_pat(i,k)
        if add_mins(pat,dna) <= distance:
            final.append(pat)
    return final
#given an array of dna strings and k, it returns the pattern with the smallest score (I think)

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
#given a matrix in string form, converts to usable 2-d array

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
#given a letter, the column, and the matrix, it returns the exact point (finds the row, basically)

new_matrix = """0.155 0.197 0.254 0.225 0.296 0.338 0.254 0.169 0.239 0.225 0.141 0.197 0.31 0.324
0.254 0.282 0.211 0.225 0.268 0.169 0.31 0.268 0.239 0.197 0.296 0.225 0.338 0.296
0.352 0.239 0.268 0.296 0.183 0.211 0.239 0.324 0.268 0.296 0.324 0.296 0.183 0.197
0.239 0.282 0.268 0.254 0.254 0.282 0.197 0.239 0.254 0.282 0.239 0.282 0.169 0.183"""

a = matrix_maker(new_matrix)
b = "CTCACTAAGGCTTAGTTATACTCGGTCGCATCTGGTGCAGCACGCAGGGGCTAAGTGTGTTCAAGCCCTGTACAGGAATATTCATGAGGTAGGGAGCGAAGCCACGCCCGGCCCACCAGCTCTAATTGATAAGAGGCATCGAACATAATCGAGTTATGCAGTCTCCACCTTTCGACCGCTTCATCCGACCCTTGCACACCTTGGGGGCTCACACGTTGTACGATTTCCTGGCTTCTGACAACGCGTATCGGTTACTACCCATTCTGCCTTCTTTGCACCGTCTCTGATGTTCTGCGATCGCCTCTCTCGTTAAACCCAAGCATACACACTCTTACAGGCTACGAGGACGGAGCGCTAATACGGACAATAGCACAACCTGCGCTCAGTCGTCCTTGACGTACTATTTCGTCATGATGGTGTCCATGATGTTTAGAAGATGAACCTAGTTTGGAACGCGCGGTACCTACTCTTGGGCCGAAATCAGTTGAAATGCAATCGTGAATCTGCCAAAACCTCACGTGACATCAAAAATATCGAGCTCGTCGCACCCGGCAAATGGTTCATGCCATTCCCGTACCCCAACCTCGTGTTGTGTTTTGGCTCACATATCTAAGCTTCTTCGTCCGGGCGTAACAAAAATCACTCTAGTGCCGCATGAATTACCTACACTACGGTTCAAGCATCTAGAGTGGGTTTGCGTAAGAACGCATCTGGCTGATAACAAGGTTGATCGCCCGAAGTGGTCCGATATCTCACCTAGTGGTCTAATTTGTGCGTAAGTGGCCATGCACCGTTATGAGTCTATTAGTCAAAAGAGCCTCGCCAAAGCGAAGGGTGACTTGCACATCAAAGCCTGTGGTTGGGTCTGTTGTAGCGCCCACGATTACGCCGGGTCATCCCACGTATCCAACTGTGATCTACTCCGCCCTGTGCGCCGCATCCAGGGATGTAGCGTGCGGCCTTCACTGCAAGTGTCTGCAAACTGCGATGTGATTTGCGG"

def arr_maker(string):
    arr = string.splitlines()
    return arr
#given a string, returns a usable array by splitting by newlines

def profile_probable(dna_str,k,prob_matrix,boolean):
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
    if boolean == True:
        return max_pattern
    else:
        return max_prob
#given a long dna_str, k, a matrix, and a bool, it can return either the highest possible probability in the string for a k-mer, or just the associated pattern 

c = profile_probable(b,14,a,True)

def letter_marker(num):
    if num == 0:
        return "A"
    elif num == 1:
        return "C"
    elif num == 2:
        return "G"
    elif num == 3:
        return "T"
#given a row number, returns associated letter
    
def probability_searcher(prob_matrix,k):
    final_pat = ""
    for h in range(k):
        for i in range(3):
            if prob_matrix[i][h] > max_prob_in_col:
                max_prob_in_col = prob_matrix[i][h]
                max_letter = letter_marker(i)
        final_pat+=max_letter
    return final_pat
#given a prob matrix, returns the most probable pattern
    
def probability_matrix_maker(list_of_mers,k):
    final_arr = []
    a_row = []
    c_row = []
    g_row = []
    t_row = []
    for n in range(k):
        c_count = 0
        a_count = 0
        g_count = 0
        t_count = 0
        total = len(list_of_mers)
        for m in range(len(list_of_mers)):
            store = list_of_mers[m][n]
            if store == "A":
                a_count +=1
            elif store == "C":
                c_count +=1
            elif store == "G":
                g_count +=1
            elif store == "T":
                t_count +=1
        a_prob = a_count/total
        c_prob = c_count/total
        g_prob = g_count/total
        t_prob = t_count/total
        a_row.append(a_prob)
        c_row.append(c_prob)
        g_row.append(g_prob)
        t_row.append(t_prob)
    final_arr.append(a_row)
    final_arr.append(c_row)
    final_arr.append(g_row)
    final_arr.append(t_row)
    return final_arr

listmers = ["ACGT","CGAT","GCAT","GAAT"]
a = probability_matrix_maker(listmers,4)

def greedy_motif_search(k,t,dna_arr):
    best_motif = []
    for i in range(len(dna_arr[0])-k+1):
        all_together = []
        print(i)
        for string in range(len(dna)):
            print(string,i+k)
            k-mer_in_question = dna[string][i:i+k]
            print(k_mer_in_question)
            all_together.append(k-mer_in_question)
        temp_prob_mat = probability_matrix_maker(all_together,k)
        temp_pat = probability_searcher(temp_prob_mat,k)






