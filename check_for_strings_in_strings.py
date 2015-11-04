def str_check(string,pat,d):
    store = iter_neighbors(pat,d)
    for i in range(len(string)-len(pat)):
        patt = string[i:i+len(pat)]
        if patt in store:
            return True
        else: 
            return False
