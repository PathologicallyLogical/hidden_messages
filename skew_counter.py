def skewer(genome):
    g_count = 0
    c_count = 0
    final = "0 "
    for i in range(len(genome)):
        if genome[i] == "G":
            g_count+=1
        if genome[i] == "C":
            c_count+=1
        final+=  str(g_count - c_count)+" "
    return final
        
        
if skewer("CATGGGCATCGGCCATACGCC") == "0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2 ":
    print "true"
