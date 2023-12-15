import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer

# Read 'arrests_final.csv' into a DataFrame
arrests_df = pd.read_csv('arrests_final.csv')

# Extract relevant numeric columns for clustering
numeric_columns_for_clustering = ['ArLZip', 'HZIP']

# Select data for clustering
data_for_clustering = arrests_df[numeric_columns_for_clustering]

# Impute missing values
imputer = SimpleImputer(strategy='mean')
data_for_clustering_imputed = imputer.fit_transform(data_for_clustering)

# Standardize the data
scaler = StandardScaler()
data_for_clustering_scaled = scaler.fit_transform(data_for_clustering_imputed)

# Perform KMeans clustering
n_clusters = 3  # You can adjust this based on your analysis
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
arrests_df['Cluster'] = kmeans.fit_predict(data_for_clustering_scaled)

# Visualize the clusters using PCA for dimensionality reduction
pca = PCA(n_components=2)
data_for_clustering_pca = pca.fit_transform(data_for_clustering_scaled)
arrests_df['PCA1'] = data_for_clustering_pca[:, 0]
arrests_df['PCA2'] = data_for_clustering_pca[:, 1]

# Plot the clusters
plt.figure(figsize=(12, 8))
sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=arrests_df, palette='viridis', s=50)
plt.title('Clusters Visualization using PCA')
plt.xlabel(f'Principal Component 1 ({numeric_columns_for_clustering[0]})')
plt.ylabel(f'Principal Component 2 ({numeric_columns_for_clustering[1]})')
plt.show()
