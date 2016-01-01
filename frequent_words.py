#intended to find the most common k-mer in a dnastring.
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

def freq_k(text,k):
	all_count = []
	for i in range(4**k):
		all_count.append(0)
	for i in range(len(text)-k+1):
		txt = text[i:i+k]
		num = pat_to_num(txt)
		all_count[num] +=1
	max_count = max(all_count)
	index = 0
	for i in range(len(all_count)):
		if all_count[i]==max_count:
			index = i
	final_pat = num_to_pat(index,k)
	return final_pat

print freq_k("CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA",3)

