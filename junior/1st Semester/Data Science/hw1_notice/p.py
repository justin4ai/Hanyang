from collections import defaultdict
from itertools import combinations
import argparse

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
    print(num_items)
    min_sup = int(num_trans * (min_sup_percentage/100))

    for key, value in l1.items():
        if value < min_sup:
            del l1[key]

