import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
import seaborn as sns

k_c = 4

class K_Means:
    def __init__(self, k=k_c, tol=0.001, max_iter=500):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self, data):
        
        self.centroids = {}
        
        for i in range(self.k):
            self.centroids[i] = np.array([data[i][0],data[i][1]])

        for j in range(1, self.max_iter):
            
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for i in range(data.shape[0]):
                distances = [np.linalg.norm(np.array([data[i][0], data[i][1]])-self.centroids[j]) for j in self.centroids]
                cluster = distances.index(min(distances))
                self.classifications[cluster].append([data[i][0], data[i][1]])
            
            prev_centroids = dict(self.centroids)

            for i in self.classifications:
                self.centroids[i] = np.average(self.classifications[i],axis=0)

            optimized = True

            for i in self.centroids:
                original_centroid = prev_centroids[i]
                current_centroid = self.centroids[i]
                if np.sum((current_centroid-original_centroid)/original_centroid*100.0) > self.tol:
                    optimized = False

            if optimized:
                break
   
    def Rfit(self, data):
        
        self.centroids = {}
        weight_num = [1 for i in range(data.shape[0])]
        weight = [data[i][2] for i in range(data.shape[0])]
        check = [[1 for j in range(data.shape[0])] for i in range(self.max_iter)]
        
        for i in range(self.k):
            self.centroids[i] = np.array([data[i][0],data[i][1],data[i][3]])

        for j in range(1, self.max_iter):
            
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for i in range(data.shape[0]):
                distances = [weight_num[check[i][j-1]]*(1/weight[i])*np.linalg.norm(np.array([data[i][0], data[i][1], data[i][3]])-self.centroids[j]) for j in self.centroids]
                cluster = distances.index(min(distances))
                check[i][j] = cluster
                self.classifications[cluster].append([data[i][0], data[i][1], data[i][3]])

            for i in range(self.k):
                weight_num[i] = data.shape[0]/len(self.classifications[i])
            
            prev_centroids = dict(self.centroids)

            for i in self.classifications:
                self.centroids[i] = np.average(self.classifications[i],axis=0)

            optimized = True

            for i in self.centroids:
                original_centroid = prev_centroids[i]
                current_centroid = self.centroids[i]
                if np.sum((current_centroid-original_centroid)/original_centroid*100.0) > self.tol:
                    optimized = False

            if optimized:
                break

df = pd.read_excel("C:/Users/JihongJeong/international_students.xlsx")
dfp = pd.read_excel("C:/Users/JihongJeong/studentsnumber.xlsx")
dfh = pd.read_excel("C:/Users/JihongJeong/k_hub.xlsx")
df=pd.concat([df, dfp], axis=1)
A = df.values
B = np.array([dfh.loc[0]['Latitude'], dfh.loc[0]['Longitude']])
new = []
for i in range(A.shape[0]):
    new.append(np.linalg.norm(B-np.array([A[i][0],A[i][1]])))
new = np.array([new])
new = new.T
df2 = pd.DataFrame(new)
df2.columns=['k_hub']
df['k_hub'] = df2['k_hub']
X = df.values
Y = df.values

model_1 = K_Means()
model_1.Rfit(X)

df_cent = pd.DataFrame(model_1.centroids)
df_cent = df_cent.T
df_cent.columns=['Latitude', 'Longitude', 'k_hub']
print("the centroid point is : \n", np.array([[df_cent.loc[i]['Latitude'],df_cent.loc[i]['Longitude']] for i in range(df_cent.values.shape[0])]))

fig = plt.figure()
fig2 = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax2 = fig2.add_subplot()

for i in range(k_c):
    df_clas = pd.DataFrame.from_dict(model_1.classifications[i])
    df_clas.columns=['Latitude', 'Longitude', 'k_hub']
    df_clas['cluster'] = i
    x = df_clas['Longitude']
    y = df_clas['Latitude']
    z = [0.1-df_clas['k_hub']]
    color = df_clas['cluster']
    ax.scatter(x, y, z, marker = 'o', c = color)
    ax2.scatter(x, y, marker = 'o', c=color)

xs = df_cent['Longitude']
ys = df_cent['Latitude']
zs = [0.1-df_cent['k_hub']]
ax.scatter(xs, ys, zs, marker='^')
ax2.scatter(xs, ys, marker='^')

ax.set_xticks(np.arange(126.764, 127.182, step=0.02))
ax.set_yticks(np.arange(37.426, 37.700, step=0.02))
ax.set_zticks(np.arange(0, 0.1, step=0.02))
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('K-Hub')

ax2.set_xticks(np.arange(126.764, 127.182, step=0.02))
ax2.set_yticks(np.arange(37.426, 37.700, step=0.02))
ax2.set_xlabel('Longitude')
ax2.set_ylabel('Latitude')

ax.view_init(30, 60)


'''
for i in range(k_c):
    df_clas = pd.DataFrame.from_dict(model_1.classifications[i])
    df_clas.columns=['Latitude', 'Longitude', 'k_hub']
    df_clas['cluster'] = i
    if i==0:
        df_point = df_clas
    else:
        df_point = pd.concat([df_point, df_clas], ignore_index = True)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
xs = df_cent['Longitude']
ys = df_cent['Latitude']
zs = df_cent['k_hub']

x = df_point['Longitude']
y = df_point['Latitude']
z = df_point['k_hub']

ax.scatter(xs, ys, zs, marker='^')
ax.scatter(x, y, z, marker='o')
'''

'''
model_2 = K_Means()
model_2.fit(Y)

df2_cent = pd.DataFrame(model_2.centroids)
df2_cent = df2_cent.T
df2_cent.columns=['Latitude', 'Longitude']

for i in range(k_c):
    df2_clas = pd.DataFrame.from_dict(model_2.classifications[i])
    df2_clas.columns=['Latitude', 'Longitude']
    df2_clas['cluster'] = i
    if i==0:
        df2_point = df_clas
    else:
        df2_point = pd.concat([df2_point, df2_clas], ignore_index = True)

plt.subplot(122)
sns.scatterplot(x='Longitude', y='Latitude', data=df2_cent, marker='x')
sns.scatterplot(x='Longitude', y='Latitude', data=df2_point, marker='o', hue = 'cluster')
plt.xticks(np.arange(126.764, 127.182, step=0.02))
plt.yticks(np.arange(37.426, 37.700, step=0.02))
plt.xlabel('Longitude')
plt.ylabel('Latitude')
'''
plt.show()
