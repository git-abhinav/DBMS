import math                 # for math.power function
lhs = {     
                            # for Storing FD's LHS
}
rhs = {
                            # for Storing FD's LHS
}
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
relation = input("Enter relation R(..) : ")     
number_of_dependencies = int(input("How many functional dependencies : "))
# taking input in form of x -> y
for i in range(0, number_of_dependencies):
    x = input("lhs : ")
    lhs[i] = x
    print("->")
    x = input("rhs : ")
    rhs[i] = x

# printing fd
print("Functional depencencies are : ")
for i in range(0, number_of_dependencies):
    print("{ ", lhs[i], "->", rhs[i], " }")


closure_of = input("Closure of what : ")
closure_is = closure_of                    # trivial

for i in range(0, number_of_dependencies): # direct dependencies
    if closure_of == lhs[i]:
        closure_is += rhs[i]
        closure_of += rhs[i]

closure_is = unify(closure_is)             # aaab to ab 
closure_of = unify(closure_of)             #

for k in range(1, 2^len(relation)+1):      # no need to check for size > the power set
    x = printPowerSet(closure_of, len(closure_of))
    for i in range(1, len(x)+1):
        c1 = x[i]                          # trying 
        for j in range(0, number_of_dependencies):
            if c1 == lhs[j]:
                closure_is += rhs[j]
                closure_of += rhs[j]
                closure_is = unify(closure_is)
                closure_of = unify(closure_of)
print("Closure is : ", a_to_z_form(closure_is), "for R(", relation, ")")





















