The programs are written in python-3, and are needed to be compiled in python-3 only 
------------------------------------------------------------------------------------

I've used the dictionary notation in the programs in which 
functional dependecnies are represented using like this
-----------------------------------------------------------


example a -> b
fd = {              # uniform across in all programs
    lhs = STRING ('a'),
    rhs = STRING ('b')
}

Used in every progarm 
---------------------
unify() 
printPowerSet()
a_to_z_form()

objective, input, output is mentioned in the code


first program is 
1) Closure
-----------
for Closure fist check if there exit a direct functional dependecny or not 
then check transitive dependecnies using the powerset of the functional 
dependecnies, and I HAD TO USE FUNCTIONS LIKE UNIFY AND PRINT_A_TO_Z 
BECAUSE I HAVE USED STRING NOTATION AND IT MAY HAPPEN THAT WHILE COMPUTING
STRING MAY GET CONVERTED TO LIKE aaabgg, which I need to conevert to "abg"

2) candidate key 
-----------------


for determing candidate key,just find which set of attribute is not on rhs
using,

for i in range(0, len(relation)):
    status = -1
    for j in range(0, number_of_dependencies):
        if fd['rhs'][j].find(relation[i]) != -1:
            status = 0
    if status == -1:
        not_on_rhs += relation[i]

then try determing relation from that attribute which is not on RHS
using, 

pool = r.replace(not_on_rhs, "")
if find_closure(fd, not_on_rhs, relation, number_of_dependencies) == relation:
    print("CK is ", not_on_rhs)

else try appending, attributes from pool

3) 2NF 
-------


In this first we have to find the candidate key, then we have to check if 
there exits any subset of prime attribute (form power set discussed earlier) 
that determines a non prime attribute    
using,


for i in range(1, len(attribute_subset)):
    for j in range(0, len(fd['lhs'])):
        if attribute_subset[i] == fd['lhs'][j]:
            for k in range(0, len(non_prime)):
                if fd['rhs'][j] == non_prime[k]:
                    print("Not in 2nf")

3) 3NF 
-------

In this we have to find the transitive dependecnies, 
checked using,

attribute_subset = printPowerSet(non_prime, len(non_prime))
status3nf = 1
for i in range(1, len(attribute_subset)):
    print("Pset", attribute_subset[i])
    for j in range(0, len(fd['lhs'])):
        print("Checking", attribute_subset[i], "and", fd['lhs'][j])
        if attribute_subset[i] == fd['lhs'][j]:
            for k in range(0, len(non_prime)):
                if fd['rhs'][j] == non_prime[k]:
                    print("Transitive dependeny found", fd['lhs'][j], "->", non_prime[k])


4) minimal 
-----------
2 sets of functional dependecnies are given fd1 and fd2

just need check closure if fd1(i) from fdset or fd2 and vice-versa 

checked using,
tempClosure = find_closure(fd, fd['lhs'][which_to_hide], relation, len(fd['lhs']))
for k in range(0, len(fd_with_out['lhs'])):
    if tempClosure == find_closure(fd_with_out, fd_with_out['lhs'][k], relation, len(fd_with_out['lhs'])):
        print(fd_with_out['lhs'][k], "->", fd_with_out['rhs'][k])


5) equivalence
----------------
using a static example coded in the program 
checked using,

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


6) BCNF
----------
code till 3nf is same just 
checking the power set of prime attribute and checking it with all fds will suffice for checking
the necessary condition for violation of BCNF 

using,
x = {}
x = printPowerSet(prime_attributes, len(prime_attributes))
# print(x)
status_bcnf = -1
for i in range(1, len(x)):
    for j in range(number_of_dependencies):
        # print("Checking", fd['rhs'][j], "=", x[i], "and", non_prime, "=", fd['lhs'][j])
        if x[i] == fd['rhs'][j] and non_prime == fd['lhs'][j]:
            print("Non-prime \'", non_prime, "\' determines a prime attribute \'",x[i], " \'")
            status_bcnf = 1
if status_bcnf == -1:
    print("Yes, in BCNF")
else:
    print("NoT in BCNF")


------------------------------------------X------------------------------------------