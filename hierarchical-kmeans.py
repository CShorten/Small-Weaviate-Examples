import numpy as np
import matplotlib.pyplot as plt

class AgglomerativeClustering:
    def __init__(self, n_clusters):
        self.n_clusters = n_clusters
        self.labels = None
        self.centroids = None

    def fit(self, data):
        # Initialize each data point as a cluster
        clusters = [[point] for point in data]

        while len(clusters) > self.n_clusters:
            # Compute pairwise distances between clusters
            distances = self.pairwise_distances(clusters)

            # Find the closest clusters
            min_distance = np.min(distances)
            cluster1, cluster2 = np.unravel_index(np.argmin(distances), distances.shape)

            # Merge the closest clusters
            merged_cluster = clusters[cluster1] + clusters[cluster2]
            clusters.pop(max(cluster1, cluster2))
            clusters.pop(min(cluster1, cluster2))
            clusters.append(merged_cluster)

        # Assign labels based on the final clusters
        self.labels = np.zeros(len(data), dtype=int)
        self.centroids = []
        for i, cluster in enumerate(clusters):
            self.labels[[data.tolist().index(point) for point in cluster]] = i
            self.centroids.append(np.mean(cluster, axis=0))

    @staticmethod
    def pairwise_distances(clusters):
        distances = np.zeros((len(clusters), len(clusters)))
        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                distances[i, j] = np.sqrt(np.sum((np.array(clusters[i])[:, None] - np.array(clusters[j])) ** 2))
                distances[j, i] = distances[i, j]
        return distances

# Generate random data
np.random.seed(42)
data = np.random.rand(20, 2)

# Perform hierarchical clustering
clustering = AgglomerativeClustering(n_clusters=3)
clustering.fit(data)

# Plotting the data points and centroids
plt.scatter(data[:, 0], data[:, 1], c=clustering.labels, cmap='viridis')
plt.scatter([c[0] for c in clustering.centroids], [c[1] for c in clustering.centroids], c='red', marker='x', s=100)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Hierarchical Clustering')
plt.show()
