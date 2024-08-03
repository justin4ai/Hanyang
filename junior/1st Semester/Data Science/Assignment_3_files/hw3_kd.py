import numpy as np
from sklearn.neighbors import KDTree
import time
import sys
import os

def range_query(tree, point, eps):
    ind = tree.query_radius([point], r=eps)
    return ind[0]

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

def dbscan(DB, eps, min_pts):
    labels = {id: 0 for id in DB.keys()}  # -1 : anomaly, 0 : undefined, 1~ : cluster label
    c = 0
    points = np.array(list(DB.values()))
    tree = KDTree(points, leaf_size=30)

    for p in DB.keys():
        if labels[p] != 0: continue  # Skip processed points

        N = range_query(tree, DB[p], eps)

        if len(N) < min_pts:
            labels[p] = -1
            continue

        c += 1
        labels[p] = c

        N = list(N)
        N.remove(p)
        S = N.copy()

        labels = growth(DB, labels, S, c, eps, min_pts, tree)

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

    sorted_clusters = sorted(clusters.items(), key=lambda x: len(x[1]))
    clusters_to_write = sorted_clusters[-n:]

    # 작은 클러스터들을 -1로 변경
    clusters_to_ignore = sorted_clusters[:-n]
    for cluster_id, obj_ids in clusters_to_ignore:
        for obj_id in obj_ids:
            labels[obj_id] = -1

    # 재정렬된 클러스터 번호 부여
    new_cluster_id = 0
    for _, obj_ids in clusters_to_write:
        for obj_id in obj_ids:
            labels[obj_id] = new_cluster_id
        new_cluster_id += 1

    # 텍스트 파일로 저장
    for cluster_id in range(new_cluster_id):
        obj_ids = [obj_id for obj_id, label in labels.items() if label == cluster_id]
        file_name = f"Assignment 3 self test/input{input_file.split('/')[-1].split('.')[0][-1]}_cluster_{cluster_id}.txt"
        with open(file_name, 'w') as file:
            for obj_id in obj_ids:
                file.write(f"{obj_id}\n")

    end_time = time.time()
    print(f"코드 실행 시간: {end_time - start_time:.6f} 초")
