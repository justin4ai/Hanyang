import numpy as np
from sklearn.neighbors import KDTree
import time
import sys
import os

def range_query(kdtree, point, eps):

    return kdtree.query_radius([point], r = eps)[0] # using KDTree


def growth(DB, labels, S, c, eps, min_pts, tree):

    while S:
        q = S.pop()

        if labels[q] == -1: labels[q] = c
        if labels[q] != 0: continue

        N = range_query(tree, DB[q], eps)
        labels[q] = c

        if len(N) < min_pts: continue

        S.extend(N)

    return labels


def dbscan(DB, eps, min_pts): # stick to the pseudocode in the lecture slide

    labels = {id: 0 for id in DB.keys()}  # -1 : anomaly, 0 : undefined, 1~ : cluster label
    c = 0
    points = np.array(list(DB.values()))
    kdtree = KDTree(points, leaf_size=30)

    for p in DB.keys():

        if labels[p] != 0: continue 

        N = range_query(kdtree, DB[p], eps)

        if len(N) < min_pts:
            labels[p] = -1
            continue

        c += 1
        labels[p] = c

        N = list(N)
        N.remove(p)
        S = N.copy()

        labels = growth(DB, labels, S, c, eps, min_pts, kdtree)

    return labels

if __name__ == "__main__":
    #start_time = time.time()

    input_file = "./Assignment 3 input data/" + sys.argv[1]
    n = int(sys.argv[2])
    eps = float(sys.argv[3])
    min_pts = int(sys.argv[4])

    db = {}

    with open(input_file, 'r') as file:
        for line in file:
            line_numbers = [ float(num) for num in line.strip().split() ]
            db[int(line_numbers[0])] = (line_numbers[1], line_numbers[2])

    labels = dbscan(db, eps, min_pts)


    ############################ DBSCAN finished. For file saving from now on ############################
    clusters = {}

    for id, label in labels.items():

        if label == -1: continue

        if label not in clusters:
            clusters[label] = []

        clusters[label].append(id)

    # we only need n clusters #
    clusters_sorted = sorted(clusters.items(), key = lambda x : len(x[1])) # according to the assignment suggestion
    clusters_n = clusters_sorted[-n:]

    for cluster_label, ids in clusters_sorted[:-n]: # (n-m) cluasters go to noise label

        for obj_id in ids: labels[obj_id] = -1


    # not necessary but for clarification # 
    new_id = 0
    for _, ids in clusters_n:

        for id in ids:

            labels[id] = new_id
        new_id += 1


    for cluster_label in range(0, new_id):
        ids = [ id for id, label in labels.items() if label == cluster_label ]
        file_name = f"Assignment 3 self test/input{input_file.split('/')[-1].split('.')[0][-1]}_cluster_{cluster_id}.txt"
        
        with open(file_name, 'w') as file:
        
            for id in ids:
                file.write(f"{id}\n")

    #end_time = time.time()
    #print(f"runtime : {end_time - start_time}")
