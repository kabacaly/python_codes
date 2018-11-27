from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist

distortions = []
scores = []
K = range(1,13)
for k in K:
    kmean_model = KMeans(n_clusters=k, n_jobs=-1).fit(df_dummies)
    distortions.append(sum(np.min(cdist(df_dummies, kmean_model.cluster_centers_,'euclidean'), axis=1))/df_dummies.shape[0])
    scores.append(kmean_model.score(df_dummies))


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(K, distortions, 'bx-')
plt.xlabel('K')
plt.ylabel('Distortions')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(K,scores, 'bx-')

plt.show()
