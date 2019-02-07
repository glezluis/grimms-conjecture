from sympy import isprime, primefactors

def set_primes(s):
    for composite in sorted(s, reverse = True):
        for prime in reversed(primefactors(composite)):
            if prime not in s.values():
                s[composite] = prime
                break
        if s[composite] == 0:
            raise Exception('no unique prime found')
    return s

def con_comp(x):
    clist = [i for i in range(4,x) if not isprime(i)]
    ccsets = dict()
    setkey = 1
    singleset = {}

    for i in range(len(clist)-1):
        a = clist[i]
        b = clist[i+1]
        if b - a == 1:
            if singleset and a - list(singleset.keys())[-1] > 1:
                ccsets[setkey] = set_primes(singleset)
                setkey = setkey + 1
                singleset = {}
            singleset[a] = 0
            singleset[b] = 0
    ccsets[setkey] = set_primes(singleset)
    return ccsets            

def print_comps(n): 
    for index, x  in con_comp(n).items():
        print(index, ". ", x, "\n")
    

con_comp(100)
# print_comps(100)
