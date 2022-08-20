import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

k=3 #the number of the cluster

df = pd.read_excel("C:/Users/JihongJeong/international_students.xlsx")
dfp = pd.read_excel("C:/Users/JihongJeong/studentsnumber.xlsx")

#sns.scatterplot(x='Longitude', y='Latitude', data=df)
plt.ylabel('Latitude')
#print(df)

points = df.values
kmeans = KMeans(n_clusters=k).fit(points)
df2 = pd.DataFrame(kmeans.cluster_centers_, columns=['Latitude', 'Longitude'])
#print(df2)

df['cluster']=kmeans.labels_
sns.scatterplot(x='Longitude', y='Latitude', hue='cluster', data=df)

#sns.scatterplot(x='Longitude', y='Latitude', data=df2, size = 100)
plt.xlabel('Longitude')
plt.ylabel('Latitude')

df=pd.concat([df, dfp], axis=1)
#print(df)
df3 = pd.DataFrame(df.groupby('cluster')['international students'].sum())
#print(df3)
df3.reset_index()
df2 = pd.concat([df2,df3], axis=1)
df2['tot_lat']=df2['Latitude']*df2['international students']/df2['international students'].sum()
df2['tot_long']=df2['Longitude']*df2['international students']/df2['international students'].sum()
#print(df2)
print("the candidate point of cluster",k,"is : (", df2['tot_lat'].sum(),",",df2['tot_long'].sum(),")")
df4=pd.DataFrame(data={"Latitude": [df2['tot_lat'].sum()], "Longitude":[df2['tot_long'].sum()]})

sns.scatterplot(x='Longitude', y='Latitude', size='international students', data=df2)
sns.scatterplot(x='Longitude', y='Latitude', data=df4)
plt.xticks(np.arange(126.764, 127.182, step=0.02))
plt.yticks(np.arange(37.426, 37.700, step=0.02))
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.show()
