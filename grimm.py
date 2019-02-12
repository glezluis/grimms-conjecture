from sympy import isprime, primefactors

def set_p#rimes(s):
    for composite in sorted(s, reverse = True):
        for prime in reversed(primefactors(composite)):
            if prime not in s.values():
                s[composite] = prime
                break
        if s[composite] == 0:
            raise Exception('no unique prime found for %d' % composite)
    return s

# Algorithm that finds all the sets of consecutive composites between the give range
# input: a tuple r of two postive integers
# output: a dictionary whos key is the number of the set and value is another dictionary.
#		  That dictionary's key is the composite number and value is the unique prime
def consecutive_composites(r):
    a, b = r
    clist = [i for i in range(a,b) if not isprime(i)]
    ccsets = {}
    singleset = {}
    setkey = 1

    for i in range(len(clist)-1):
        n1 = clist[i]
        n2 = clist[i+1]
        if n2 - n1 == 1:
            if singleset and n1 - list(singleset.keys())[-1] > 1:
                ccsets[setkey] = set_primes(singleset)
                setkey += 1
                singleset = {}
            singleset[n1] = 0
            singleset[n2] = 0
 
    if singleset:
    	ccsets[setkey] = set_primes(singleset)

    return ccsets            

# Prints the set of of consecutive composites
# input: none
# output: none
def print_comps(s): 
    for index, x  in s.items():
        print(index, ". ", x, "\n")

# Prints the menu
# input: none
# output: none
def menu():
    print('\nGrimm\'s conjecture! what do you want to? ')
    print('(f)ind consectuive composite sets')
    print('(p)rint sets')
    print('(q)uit')

#This function handles all the input for the program
# input: none
# output: tuple of two positive integers
def input_range():
    print('Enter a range [a,b]')

    while True: 
        try:
            a = int(input('a = '))
            b = int(input('b = '))
            if a < 0 or b < 0:
                print('*** only enter positive values! ***')
                continue
            return((a,b))
        except:
            print("*** enter a valid integer! ***")

   