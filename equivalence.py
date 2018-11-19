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
    for i in range(0, dependencies):
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
def print_fd(fd):
    for i in range(0, len(fd['lhs'])):
        print("{", fd['lhs'][i], "->", fd['rhs'][i],"}")
def findIn(x, y):
    c = 0
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            if x[i] == y[j]:
                c+=1
    if c == len(x):
        #print(x, "found in ", y)
        return True
    else:
        #print(x, "found in ", y)
        return False
f = {
    'lhs':{
        0: "a",
        1: "ac",
        2: "e",
        3: "e"
    },
    'rhs':{
        0: 'c',
        1: 'd',
        2: 'ad',
        3: 'h'
    }}
g = {
    'lhs':{
        0: 'a',
        1: 'e'
    },
    'rhs':{
        0:  'cd',
        1:  'ah'
    }}
relation = "acdeh"
status1 = 1
status2 = 1
print("-"*10)
print("F")
print_fd(f)
print("-"*10)
print("G")
print_fd(g)
print("-"*10, "\n")
#check f C G
for i in range(0, len(f['lhs'])):
    tempClosure = find_closure(g, f['lhs'][i], relation, len(g['lhs']))
    #print("Checking", f['rhs'][i], " in ", tempClosure)
    if not findIn(f['rhs'][i], tempClosure):
        status = -1
if status1 == 1:
    print("F is subset of G")
else:
    print("F is not a subset of G")
#check g C f
for i in range(0, len(g['lhs'])):
    tempClosure = find_closure(f, g['lhs'][i], relation, len(f['lhs']))
    #print("Checking", g['rhs'][i], " in ", tempClosure)
    if not findIn(g['rhs'][i], tempClosure):
        status2 = -1
if status2 == 1:
    print("F is subset of G")
else:
    print("F is not a subset of G")
if status1 == 1 and status2 == 1:
    print("F and G are equivalent")
else:
    print("F and G are not equivalent")


