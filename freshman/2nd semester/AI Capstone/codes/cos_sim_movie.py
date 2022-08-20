import pandas as pd
import numpy as np

movie = pd.read_csv("./movies.csv")

def cosine_sim(a, b):
    return np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))

add_genre = []
for i in range(len(movie)):
    add_genre.append(movie['genres'][i].split("|"))

movie['genre']=add_genre
movie=movie.drop(['genres'],axis=1)

genre_list = []
for i in range(len(movie)):
    genre_list=genre_list+movie['genre'][i]
    make_set=set(genre_list)
    genre_list=list(make_set)

genre_list.sort()

print(genre_list)

movie_matrix = [[0 for col in range(len(genre_list))] for row in range(len(movie))]

for i in range(len(movie)):
    for j in range(len(genre_list)):
        if set([genre_list[j]])&set(movie['genre'][i]):
            movie_matrix[i][j]=1
            
movie_matrix = np.array(movie_matrix)
print(movie_matrix)

f = open("simliaritymatrix_movie.csv", 'a')
for i in range(len(movie)):
    f.write("movie"+str(i+1)+",")
f.write("\n")
f.close

for i in range(len(movie)):
    f = open("simliaritymatrix_movie.csv", 'a')
    for j in range(len(movie)):
        f.write(str(cosine_sim(movie_matrix[i], movie_matrix[j]))+",")
    f.write("\n")
    f.close()
    print(i/len(movie)*100, "% is done")


