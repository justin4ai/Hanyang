from collections import defaultdict
from itertools import combinations
import numpy as np
import sys
import time
import os


def range_query(DB, p, eps):
    
    N, cnt = [], 0
    
    for id, (x, y) in DB.items():
        
        if np.linalg.norm(np.array(DB[p]) - np.array(DB[id])) < eps: # including p itself
           N.append(id)
           cnt += 1
            
    return N, cnt


def growth(DB, labels, S, c, eps, min_pts):
    while S:
        q = S.pop()
        if labels[q] == -1: labels[q] = c
        if labels[q] != 0: continue

        N, N_cnt = range_query(DB, q, eps)
        labels[q] = c

        if N_cnt < min_pts: continue
        S.extend(N)

    return labels

def dbscan(DB, eps, min_pts):
   
    labels = {id : 0 for id in DB.keys()} # -1 : anomaly, 0 : undefined, 1~ : cluster label
    c = 0
    
    for p in DB.keys(): # Iterate over every point
        print(p)
    
        if labels[p] != 0: continue # Skip processed points

        N, N_cnt = range_query(DB, p, eps) # Find initial neightbors / p is an object id
        print(f"N :{N}")
        
        if N_cnt < min_pts:
            labels[p] = -1
            continue
 
        c += 1
        labels[p] = c

        N.remove(p)
        S = N.copy()
        
        labels = growth(DB, labels, S, c, eps, min_pts)
    

    return labels


 
    



if __name__ == "__main__":

    start_time = time.time()

    input_file = "./Assignment 3 input data/" + sys.argv[1]
    n = int(sys.argv[2])
    eps = float(sys.argv[3])
    min_pts = int(sys.argv[4])

    db = {}

    with open(input_file, 'r') as file:

        for line in file:
            line_numbers = [float(num) for num in line.strip().split()]
            
            db[int(line_numbers[0])] = (line_numbers[1], line_numbers[2])
    
    labels = dbscan(db, eps, min_pts)

    clusters = {}
    for obj_id, cluster_id in labels.items():
        if cluster_id == -1:
            continue
        if cluster_id not in clusters:
            clusters[cluster_id] = []
        clusters[cluster_id].append(obj_id)

    for cluster_id, obj_ids in clusters.items():
        file_name = f"Assignment 3 self test/input{input_file.split('/')[-1].split('.')[0][-1]}_cluster_{cluster_id - 1}.txt"
        with open(file_name, 'w') as file:
            for obj_id in obj_ids:
                file.write(f"{obj_id}\n")

    end_time = time.time()
    print(f"코드 실행 시간: {end_time - start_time:.6f} 초")



