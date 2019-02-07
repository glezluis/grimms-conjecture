def factors(x):
    #for a number x, returns a list of x's factors 
    i = 1
    list = [];
    for i in range(i,x+1):
        if x % i == 0:
            list.append(i)
            i += 1
        else:
            i += 1
    return list
    
def is_prime(x):
    #using the function factors(x), returns prime factors from 1 to x
    prime_factors = [];
    for i in factors(x):
        if len(factors(i)) == 2:
            prime_factors.append(i)           
    return prime_factors
    
def composite_list(x):
    #using function factors(x), returns composite factors from 1 to x
    composite_factors = [];
    i = 1
    for i in range(i, x+1):
        if len(factors(i)) > 2:
            composite_factors.append(i)
    return composite_factors

def prime_list(x):
    q= [];
    i= 2
    for i in range(i, x + 1):
        if len(factors(i)) == 2:
            q.append(i)
    return q
            
def consecutive_composites(x):
    # takes a list of composite numbers and determines the consecutive sets
    tupl= ();
    a= dict();
    
    for j in range(0, len(composite_list(x))-1):
        i= composite_list(x)[j]
        k= composite_list(x)[j+1]

        if k-i == 1:
            mykeys = list(a.keys())
            if len(a) !=0 and i- mykeys[-1] > 1:
                tupl = tupl + (a,)
                a= dict();   
            a[i]= 0
            a[k]= 0
    tupl = tupl + (a,)
    return tupl 


def pc_factors(x):
    plist= [1];
    comptup = consecutive_composites(x)
    for cd in comptup:
        for k in cd:
            p = is_prime(k)
            if p[-1] not in plist:
                plist.append(p[-1])
                cd[k] = p[-1]
        plist = [1]
    return comptup

def prime_of_composite_factors(x):
 #   takes the list of consecutive composite numbers from the previous function and returns distinct primes
    tupx= ();
    plist= [];
    for cl in consecutive_composites(x):
        nlist= [];
        for i in cl:
            p= is_prime(i)
            if p[-1] not in plist:
                plist.append(p[-1])
                tupc= (i, p[-1])
                nlist.append(tupc)

        plist= [];
        tupx= tupx + (nlist,)
        
 
    return tupx

def con_comp(x):
    clist = composite_list(x)
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

        
def primeOfComp(x):
    comps = con_comp(x)
    for index , cl in comps.items():
        for comp in sorted(cl, reverse = True):    
            for k in reversed(is_prime(comp)):
                if k not in cl.values():
                    cl[comp] = k
                    break
            if cl[comp] == 0:
                print(index, ". ",comp,  " no prime")
    return comps

def printComps(n): 
    for index, x  in primeOfComp(n).items():
        print(index, ". ", x, "\n")
    return 0

printComps(1810)

