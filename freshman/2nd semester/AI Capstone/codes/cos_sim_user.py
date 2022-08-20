import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

user = pd.read_csv("./ratings.csv")

sparse_matrix_user = csr_matrix((user['rating'], (user['userId'], user['movieId'])))

row_index_user, col_index_user = sparse_matrix_user.nonzero()
data_user = sparse_matrix_user.data

rows_user = np.unique(row_index_user)
length = max(rows_user)

f = open("simliaritymatrix_user.csv", 'a')
for i in range(length):
    f.write("user"+str(i)+",")
f.write("\n")
f.close

for row in range(length):
    sim = cosine_similarity(sparse_matrix_user.getrow(row), sparse_matrix_user).ravel()

    f = open("simliaritymatrix_user.csv", 'a')
    
    for i in range(length):
        f.write(str(sim[i])+",")

    f.write("\n")
    f.close
    print(row/length*100, "% is done")
