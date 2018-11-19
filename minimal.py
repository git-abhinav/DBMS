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
def print_fd(fd):
    for i in range(0, len(fd['lhs'])):
        print("{", fd['lhs'][i], "->", fd['rhs'][i],"}")
fd = {
    'lhs':{
        0:'x',
        1:'wz',
        2:'wz',
        3:'y',
        4:'y',
        5:'y'
    },
    'rhs':{
        0:'w',
        1:'x',
        2:'y',
        3:'w',
        4:'x',
        5:'z'
    }
}
relation = "wxyz"
number_of_dependencies = len(fd['lhs'])
fd_counter = 0
print("Redundent attributes are : ")
for i in range(0, len(fd['lhs'])):
    fd_counter = 0
    # print("hiding", i)
    which_to_hide = i
    fd_with_out = {
        'lhs':{},
        'rhs':{}}
    for j in range(0, len(fd['lhs'])):
        if which_to_hide != j:
            fd_with_out['lhs'][fd_counter] = fd['lhs'][j]
            fd_with_out['rhs'][fd_counter] = fd['rhs'][j]
            fd_counter+=1
    tempClosure = find_closure(fd, fd['lhs'][which_to_hide], relation, len(fd['lhs']))
    for k in range(0, len(fd_with_out['lhs'])):
        if tempClosure == find_closure(fd_with_out, fd_with_out['lhs'][k], relation, len(fd_with_out['lhs'])):
            print(fd_with_out['lhs'][k], "->", fd_with_out['rhs'][k])