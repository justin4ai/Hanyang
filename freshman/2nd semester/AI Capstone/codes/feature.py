import pandas as pd
import numpy as np

user = pd.read_csv("./ratings.csv")
movie = pd.read_csv("./movies.csv")
user_sim = pd.read_csv("./simliaritymatrix_user.csv")
movie_sim = pd.read_csv("./simliaritymatrix_movie.csv")

movie_sim = movie_sim.drop([movie_sim.columns[9742]], axis=1)
print("Data Loading is done", "\n")
#print(user_sim, "\n")
#print(movie_sim, "\n")

movie_id = max(user['movieId'])+1
user_id = max(user['userId'])+1

movie_check =  np.zeros(user_id*movie_id).reshape(user_id,movie_id)
for i in range(len(user)):
    movie_check[user['userId'][i]][user['movieId'][i]] = user['rating'][i]

#print(movie_check)

len_user = 100 #len(user)

#top_sim_user = np.zeros(len_user*5).reshape(len_user, 5)
#top_sim_movie = np.zeros(len_user*5).reshape(len_user, 5)

f = open("feature_creation.csv", 'a')
for i in range(5):
    f.write("sim_movie"+str(i+1)+",")
for i in range(5):
    f.write("sim_user"+str(i+1)+",")    
f.write("\n")
f.close

for i in range(len_user):
    f = open("feature_creation.csv",'a')
    ch_movie=0
    ch_user=0

    target_movie = user['movieId'][i]
    target_user = user['userId'][i]
    
    for j in range(len(movie)):
        if movie['movieId'][j]==target_movie:
            target_movie_idx=j
        
    a = np.array(movie_sim.iloc[[target_movie_idx],:])
    s = a.argsort()[::-1]

    for j in range(len(movie)):
        if movie_check[user['userId'][i]][movie['movieId'][s[0][j]]] != 0:
            #top_sim_movie[i][ch_movie] = movie_check[user['userId'][i]][movie['movieId'][s[0][j]]]
            f.write(str(movie_check[user['userId'][i]][movie['movieId'][s[0][j]]])+",")
            ch_movie=ch_movie+1
        if ch_movie == 5:
            break

    a = np.array(user_sim.iloc[[target_user],:])
    s = a.argsort()[::-1]
    
    for j in range(user_id):
        if movie_check[s[0][j]][user['movieId'][i]] != 0:
            #top_sim_user[i][ch_user] = movie_check[s[0][j]][user['movieId'][i]]
            f.write(str(movie_check[s[0][j]][user['movieId'][i]])+",")
            ch_user=ch_user+1
        if ch_user == 5:
            break
    f.write("\n")
    f.close
    print(i/len_user*100, "% is done")
    

