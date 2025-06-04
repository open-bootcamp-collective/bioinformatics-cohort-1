
# Mutation Frequency Analysis Across Tissues

## Step 1: Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## Step 2: Create Simulated Mutation Data
mutation_data = pd.DataFrame({
    'Sample': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6'],
    'Tissue': ['Lung', 'Lung', 'Lung', 'Liver', 'Liver', 'Liver'],
    'TP53': [3, 5, 4, 10, 8, 12],
    'KRAS': [7, 6, 5, 3, 2, 1],
    'PIK3CA': [1, 0, 1, 4, 5, 3]
})
#Gene columns: Number of mutations found for each gene

## Step 3: Reshape Data using melt
mutation_long = mutation_data.melt(id_vars=['Sample', 'Tissue'],var_name='Gene',value_name='Mutation_Count')


#id_vars: Columns to keep fixed (Sample, Tissue)
#var_name: The new column name to hold the gene names (TP53, etc.)
#value_name: New column to hold their corresponding mutation counts



## Step 4: Summarize Mutation Counts:  we are using groupby
mutation_summary = mutation_long.groupby(['Tissue', 'Gene'])['Mutation_Count'].mean().reset_index()


#Groups data by both Tissue and Gene
#Calculates the average mutation count per gene per tissue type
#reset_index() flattens the grouped data back into a DataFrame

pivot_mut = mutation_summary.pivot(index='Gene', columns='Tissue', values='Mutation_Count')
# it converts long format to a matrix 

## Step 5: Heatmap Visualization
plt.figure(figsize=(8, 5)) # sets the plot size
sns.heatmap(pivot_mut, annot=True, fmt=".1f", cmap="magma") # using the above matrix draws the map
plt.title("Average Mutation Count per Gene by Tissue Type") 
plt.tight_layout() #Adjusts layout to avoid clipping
plt.show()
