# Load necessary libraries
library(ggplot2)
library(dplyr)
# Load UMAP coordinates
umap <- read.csv("analysis/umap/2_components/projection.csv")
# Load graph-based clustering results
clusters <- read.csv("analysis/clustering/graphclust/clusters.csv")
# Merge by Barcode
data <- merge(umap, clusters, by = "Barcode")
#UMAP
library(ggplot2)
ggplot(data, aes(x = UMAP.1, y = UMAP.2, color = factor(Cluster))) +
  geom_point(size = 1.2, alpha = 0.9) +
  theme_minimal() +
  labs(
    title = "UMAP Projection of PBMC Clusters",
    x = "UMAP 1",
    y = "UMAP 2",
    color = "Cluster"
  ) +
  theme(plot.title = element_text(hjust = 0.5))
#differential expression
de <- read.csv("analysis/diffexp/graphclust/differential_expression.csv")
# Load necessary packages
library(dplyr)
# Show top 10 marker genes for Cluster 1 by adjusted p-value
#cluster1- monocytes
top_cluster1 <- de %>%
  select(Feature.Name, Cluster.1.Log2.fold.change, Cluster.1.Adjusted.p.value) %>%
  arrange(Cluster.1.Adjusted.p.value) %>%
  slice_head(n = 10)
top_cluster1
#top 10 genes of cluster 2- monocytes
top_cluster2 <- de %>%
  select(Feature.Name, Cluster.2.Log2.fold.change, Cluster.2.Adjusted.p.value) %>%
  arrange(Cluster.2.Adjusted.p.value) %>%
  slice_head(n = 10)
top_cluster2
#cluster 3-
top_cluster3 <- de %>%
  select(Feature.Name, Cluster.3.Log2.fold.change, Cluster.3.Adjusted.p.value) %>%
  arrange(Cluster.3.Adjusted.p.value) %>%
  slice_head(n = 10)
top_cluster3
#cluster 7- Bcells
top_cluster7 <- de %>%
  select(Feature.Name, Cluster.7.Log2.fold.change, Cluster.7.Adjusted.p.value) %>%
  arrange(Cluster.7.Adjusted.p.value) %>%
  slice_head(n = 10)
top_cluster7