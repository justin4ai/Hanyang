from collections import defaultdict
from itertools import combinations
import argparse
import time

start_time = time.time()

parser = argparse.ArgumentParser()
parser.add_argument('--min_sup', default=10, type=int)
parser.add_argument('--input_file', default='input.txt', type=str)
parser.add_argument('--output_file', default='output.txt', type=str)

args = parser.parse_args()


min_sup_percentage = args.min_sup


db = []
l1 = defaultdict(int)

def generate_candidates(l_k, k):
    candidates = []
    num_patterns = len(l_k)
    
    for i in range(num_patterns):
        for j in range(i+1, num_patterns):
            candidate = set(set(l_k[i]) | set(l_k[j]))
            if len(candidate) == k+1:
                candidates.append(tuple(sorted(candidate))) # 정렬된 튜플로 저장
    return candidates

with open(args.input_file, 'r') as file:

    for line in file:
        line_numbers = [int(num) for num in line.strip().split()]
        db.append(line_numbers)
        for item in line_numbers:
            l1[(item,)] += 1

    num_trans = len(db) # number of transactions
    num_items = len(l1.keys()) # number of unique items
    min_sup = int(num_trans * (min_sup_percentage/100))

    for key, value in l1.items():
        if value < min_sup:
            del l1[key]

freq_list = [l1] + [defaultdict(int)] * (num_items - 1) # L_k is accessible by freq_list[k-1]


for k in range(1, num_items):
    candidates = generate_candidates(list(freq_list[k-1].keys()), k)
    print("Candidates at k =", k, ":", candidates)
    
    # Count support for each candidate
    for transaction in db:
        for candidate in candidates:
            if set(candidate).issubset(transaction):
                freq_list[k][candidate] += 1
    
    for candidate in list(freq_list[k].keys()):  # 딕셔너리 키의 복사본을 반복
        support = freq_list[k][candidate]
        if support < min_sup:
            del freq_list[k][candidate]
print("Frequent patterns:")
for k in range(num_items):
    print("Frequent patterns at k =", k+1, ":", list(freq_list[k].keys()))

end_time = time.time()
execution_time = end_time - start_time
print("Execution Time:", execution_time // 60 , "minutes")