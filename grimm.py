from sympy import isprime, primefactors

def con_comp(x):
    clist = [i for i in range(4,x) if not isprime(i)]
    ccsets = dict()
    singleset = dict()
    setkey = 1;
    for i in range(0,len(clist)-1):
        a = clist[i]
        b = clist[i+1]
        if b - a == 1:
            mykeys = list(singleset.keys())
            if len(singleset) != 0 and a - mykeys[-1] > 1:
                ccsets[setkey] = singleset
                singleset = dict()
                setkey = setkey + 1
            singleset[a] = 0
            singleset[b] = 0
    ccsets[setkey] = singleset
    return ccsets            

        
def prime_of_comp(x):
    comps = con_comp(x)
    for index , cl in comps.items():
        for comp in sorted(cl, reverse = True):    
            for k in reversed(primefactors(comp)):
                if k not in cl.values():
                    cl[comp] = k
                    break
            if cl[comp] == 0:
                print(index, ". ",comp,  " no prime")
    return comps

def print_comps(n): 
    for index, x  in prime_of_comp(n).items():
        print(index, ". ", x, "\n")
    return 0

print_comps(100)

#print(list(primerange(2,10)))
