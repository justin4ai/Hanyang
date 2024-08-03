from collections import defaultdict
from itertools import combinations
#import argparse
import sys
import time

# parser = argparse.ArgumentParser()

# parser.add_argument('--min_sup', default=5, type=int)
# parser.add_argument('--input_file', default='input.txt', type=str)
# parser.add_argument('--output_file', default='output.txt', type=str)

# args = parser.parse_args()
# min_sup = args.min_sup

min_sup = float(sys.argv[1])
input_file = sys.argv[2]
output_file = sys.argv[3]

db, freq_list, sup_list, c_1, unique_items = [], dict(), defaultdict(int), set(), set()


def generate_candidates(l_k, k):
    
    self_joined = self_joining(l_k, k)
    #print(self_joined)
    pruned_self_joined = pruning(self_joined, cursor, k-1)

    return pruned_self_joined

def self_joining(l_k, k): # k is larger than that of l_k by 1
    #print(l_k)

    res = set()
    for transaction_1 in l_k:
        for transaction_2 in l_k:
            superset = transaction_1.union(transaction_2)

            if len(superset) == k: # only if the superset matches the length we want
                res.add(frozenset(superset)) # set is not hashable > frozenset

    return res    

def pruning(new_candidates, l_k, k): # checking subsets
    pruned_candidates = new_candidates #
    for candidate in new_candidates:

        if any([not True for subset in combinations(candidate, k) if frozenset(subset) not in l_k]):
            pruned_candidates.remove(candidate)
    
    return pruned_candidates


def support_filter(candidates):
    global min_sup, sup_list, db


    l_k, keys = set(), set()

    for item in candidates:
        for transaction in db:
            if item.issubset(transaction):
                sup_list[item] += 1 # increment in total support list
                keys.add(item) #]

    for item in keys:
    #for item in sup_list_tmp.keys():
        if( (float(sup_list[item] / len(db))) * 100 >= min_sup): l_k.add(item)

    return l_k




with open(input_file, 'r') as file:

    for line in file:
        line_numbers = [int(num) for num in line.strip().split()]
        db.append(line_numbers)
        for item in line_numbers:
            unique_items.add(item)

    num_trans = len(db) # number of transactions
    num_unique = len(unique_items)
    print(f"#(unique items) : {num_unique}")
    #min_sup = min_sup_percentage / 100

    # num_items = len(l1.keys()) # number of unique items
    # min_sup = int(num_trans * (min_sup_percentage/100))

    # for key, value in l1.items():
    #     if value < min_sup:
    #         del l1[key]

    for transaction in db:
        for item in transaction:
            c_1.add(frozenset([item])) # since set is not hashable but frozenset is

    l_k = support_filter(c_1)#, sup_list)
    #print(l_k) # from 1 to ?, we reuse this variable
    cursor = l_k.copy()



########################### Initialization with l_1 is done #############################


for k in range(2, num_unique + 1):
    if not cursor:
        break
    print(k)
    
    freq_list[k-1] = cursor

    c_k = generate_candidates(cursor, k)
    l_k = support_filter(c_k)#, sup_list)
    
    cursor = l_k



#print(freq_list[2])
#for key in freq_list.keys():
#   print(len(freq_list[key]))
#print(rules)

#print(freq_list[4])

#print(sup_list.keys())
#x = sup_list[frozenset({12, 13, 16})]
#y = sup_list[frozenset({12, 16})]

#print(x/y)

############################ Frequent itemsets and their supports calculated ############################

association_rules = []

for n in freq_list.keys():
    
    freq_k_list = freq_list[n]
    for freq_itemset in freq_k_list:
        #for k in range(n//2): # check only to the half of #(items) since the rest will be redundant
        for k in range(1, n): # naive approach
            itemset_combinations = combinations(freq_itemset, k)

            for itemset in itemset_combinations:


                associative_itemset = freq_itemset.difference(frozenset(itemset))
                
                support = sup_list[freq_itemset] # used in common
                #print(itemset)
                support_X = sup_list[frozenset(itemset)] # count, not real support thus far
                support_Y = sup_list[associative_itemset] # the same
                # X -> Y
                confidence = (support / support_X) * 100
                # Y -> X by reversing the order
            
                #confidence_reversed = support / support_Y

                association_rules.append((itemset, associative_itemset, (support / len(db)) * 100, confidence))
                
                #association_rulse.append((associative_itemset, itemset, support, confidence_reversed))


with open(output_file, 'w') as file:

    for itemset, associative_itemset, support, confidence in association_rules:
        file.write(f"{set(itemset)}\t{set(associative_itemset)}\t{support:.2f}\t{confidence:.2f}\n")