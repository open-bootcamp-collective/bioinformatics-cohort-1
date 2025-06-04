#load libraries 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO

# RNA-seq dataset snippet
data = """
gene_id,log2FC,pvalue,tissue
BRCA1,1.5,0.004,breast
TP53,,0.02,lung
EGFR,0.8,0.2,liver
MYC,2.3,0.0001,colon
"""
#Load the data as if it's from a CSV
df = pd.read_csv(StringIO(data))

#Display original (messy) data
print("Original Data:")
print(df)

#  Data Cleaning: Remove rows with missing values
df_clean = df.dropna()

# Filter for log2FC > 1 and pvalue < 0.05 (e.g., significantly upregulated genes)
df_filtered = df_clean[(df_clean['log2FC'] > 1) & (df_clean['pvalue'] < 0.05)]

print("\nCleaned & Filtered Data:")
print(df_filtered)

# Visualize filtered results
sns.set(style="whitegrid")
plt.figure(figsize=(6, 4))
sns.barplot(data=df_filtered, x="gene_id", y="log2FC", palette="muted")
plt.title("Differentially Expressed Genes")
plt.ylabel("log2 Fold Change")
plt.xlabel("Gene")
plt.tight_layout()
plt.show()


#Visualizing relationships between two variables
sns.relplot(data=euk, x="Size (Mb)", y="Number of genes") 
plt.title("Genome size vs number of genes\n for all genomes")