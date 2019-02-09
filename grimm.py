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

def consecutive_composites(r):
    a, b = r
    clist = [i for i in range(a,b) if not isprime(i)]
    ccsets = dict()
    setkey = 1
    singleset = {}

    for i in range(len(clist)-1):
        n1 = clist[i]
        n2 = clist[i+1]
        if n2 - n1 == 1:
            if singleset and n1 - list(singleset.keys())[-1] > 1:
                ccsets[setkey] = set_primes(singleset)
                setkey = setkey + 1
                singleset = {}
            singleset[n1] = 0
            singleset[n2] = 0
    ccsets[setkey] = set_primes(singleset)
    return ccsets            

def print_comps(s): 
    for index, x  in s.items():
        print(index, ".", x.keys())
    
def menu():
    print('\nGrimm\'s conjecture! what do you want to? ')
    print('(f)ind consectuive composite sets')
    print('(p)rint sets')
    print('(q)uit')

def input_range():
    
    print('Enter a range [a,b]')

    while True: 
        try:
            a = int(input('a = '))
            b = int(input('b = '))
            return((a,b))
        except:
            print("enter a valid integer!")

   