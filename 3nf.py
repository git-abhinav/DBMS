import math                 # for math.power function
def unify(String_to_unify):
    '''
        Objective: To remove the repeated occurances of characters
        Input: Character array or String(with repeated occurances)
        Output: String with unique characters
    '''
    return ''.join(set(String_to_unify))
def a_to_z_form(String_to_sort):
    '''
        Objective: To print the String in sorted A to Z manner
        Input: Character array or String(with repeated occurances)
        Output: String, sorted from A to Z
    '''
    return ''.join(sorted(String_to_sort))
def printPowerSet(set,set_size): 
    '''
        Objective: To return the power set
        Input: Character array or String(with repeated occurances)
        Output: String with unique characters
    '''
    pow_set_size = (int) (math.pow(2, set_size)); 
    counter = 0 
    j = 0 
    r = {} 
    c = 0
    for counter in range(0, pow_set_size): 
        temp = ""
        for j in range(0, set_size): 
            if((counter & (1 << j)) > 0): 
                temp += set[j]
                r[c] = temp
        c+=1
    return r 
def find_closure(fd, c_of, relation, dependencies):
    closure_is = c_of
    lhs = fd['lhs']
    rhs = fd['rhs']
    for i in range(0, dependencies): # direct dependencies
        if c_of == lhs[i]:
            closure_is += rhs[i]
            c_of += rhs[i]
    closure_is = unify(closure_is)
    c_of = unify(c_of)
    for k in range(1, 2^len(relation)+1):
        x = printPowerSet(c_of, len(c_of))
        for i in range(1, len(x)+1):
            c1 = x[i]
            for j in range(0,dependencies):
                if c1 == lhs[j]:
                    closure_is += rhs[j]
                    c_of += rhs[j]
                    closure_is = unify(closure_is)
                    c_of = unify(c_of)
    return a_to_z_form(closure_is)
fd = {
    'lhs' :{

    },
    'rhs' :{

    }}
no_of_fd = int(input("Number of functional dependecies : "))
print("Enter functional dependencies : ")
for i in range(0, no_of_fd):
    fd['lhs'][i] = input()
    print("->")
    fd['rhs'][i] = input()
print(fd)
relation = input("Enter relation : ")
number_of_dependencies = len(fd['lhs'])
closure_of = "ac"
not_on_rhs = ""
for i in range(0, len(relation)):
    status = -1
    for j in range(0, number_of_dependencies):
        if fd['rhs'][j].find(relation[i]) != -1:
            status = 0
    if status == -1:
        not_on_rhs += relation[i]
print("Relation is : ", relation)
print("Not on rhs : ", not_on_rhs)
r = relation
pool = r.replace(not_on_rhs, "")
cks = {}
print("checking ", find_closure(fd, not_on_rhs, relation, number_of_dependencies), "in", relation)
if find_closure(fd, not_on_rhs, relation, number_of_dependencies) == relation:
    print("CK is ", not_on_rhs)
    cks[0] = not_on_rhs
else:
    tryWith = not_on_rhs
    pool = printPowerSet(pool, len(pool))
    idx = 0
    for i in range(1, len(pool)+1):
        tryWith = not_on_rhs
        tryWith += pool[i]
        closure_got = find_closure(fd, a_to_z_form(tryWith), relation, number_of_dependencies)
        # print("Trying with", tryWith, " closure got - ", closure_got, "relation is - ", relation)
        if closure_got == relation:
            print("Ck", tryWith)
            cks[idx] = tryWith
            idx+=1
print("Candidate key : ", cks)
prime_attributes = str(cks[0])
r = relation
indexer = 0
non_prime = ""
for i in range(0, len(relation)):
    status = 1
    for j in range(0, len(prime_attributes)):
        if prime_attributes[j] == relation[i]:
            status = -1
            break
    if status == 1:
        non_prime+=relation[i]
print("Prime : ", prime_attributes)
print("Non Prime : ", non_prime)
attribute_subset = printPowerSet(non_prime, len(non_prime))
status3nf = 1
for i in range(1, len(attribute_subset)):
    #print("Pset", attribute_subset[i])
    for j in range(0, len(fd['lhs'])):
        #print("Checking", attribute_subset[i], "and", fd['lhs'][j])
        if attribute_subset[i] == fd['lhs'][j]:
            for k in range(0, len(non_prime)):
                if fd['rhs'][j] == non_prime[k]:
                    print("Transitive dependeny found", fd['lhs'][j], "->", non_prime[k])
                    status3nf = -1
if status3nf == -1:
    print("Not in 3NF")
else:
    print("In 3NF")