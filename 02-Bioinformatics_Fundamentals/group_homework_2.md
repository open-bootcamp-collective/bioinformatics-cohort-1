# Group Homework 2: 

## Overview

This homework builds off of the key concepts from Session 2 including molecular biology fundamentals, Biopython usage, sequence data formats, pandas dataframes, and exploratory data analysis. 

Each group will work collaboratively to complete the tasks below and present their solution at the beginning of the next session. Presentations should be approximately 5 minutes long and demonstrate your understanding of the material.

## Assignment Tasks

### 1. Eukaryotic Genome Data Analysis 

Using the provided `eukaryotes.tsv` dataset 

- Create a script analyze_eukaryotes.py that:
    - Reads the file using pandas `(pd.read_csv(“eukaryotes.tsv”, sep=”\t”))`
    - Calculates descriptive statistics (`count`, `mean`, `std`, `min`, `quartiles`) for Size(Mb) column
    - Filters all rows where `Species == “Homo sapiens”` into a new DataFrame `humans`
    - Computes the correlation between Size (Mb) and Number of genes using the `dataframe.corr()` method
    - Creates a new DataFrame `small_genomes` where `Size (Mb)< 5000`
    - Plots `Number of genes` vs. `Size (Mb)` using Seaborn or matplotlib
    - Save your plot as `genome_plot.png`
 
- For some reference material for pandas and seaborn, please see the provided `bootcamp.py` and `mutation_case_study.py`, referenced in the lecture slides.

### 2. Open Reading Frames Finder with Biopython 

Using the provided file `test_dna_orf.txt`, identify all candidate proteins from potential open reading frames 

- Write a Python script `find_orfs.py` that:
    - Reads a DNA sequence from `test_dna_orf.txt`
    - Uses Bio.Seq and considers the 6 possible reading frames
    - Determines and prints (in any order) all unique, translated amino acid sequences that: 
        - Begin with a start codon (M/Methionine)
        - End with a stop codon (e.g., * in Biopython translation)
        - Do not contain intermediate stop codons
- Report how many unique ORFs you determined.

Hint: Consider using `.reverse_complement()` and `.translate(to_stop=False)` and filter translated results
Bonus: Save all unique protein sequences to a FASTA file using `Bio.SeqIO`

### 3. Run Your Script and Save the Output

Run both Python scripts from the terminal: 

```bash
python find_orfs.py > orf_results.txt
python analyze_eukaryotes.py > euk_stats.txt
```

Your output folder should include 
- `euk_stats.txt`: Descriptive stats and correlation information
- `orf_results.txt`: Unique ORF proteins
- `genome_plot.png`: Scatter plot of genes vs. genome size (<5000 Mb)

### 4. Save and Share Your Work with GitHub

- Stage and commit your changes using `git add` and `git commit`
- Push your updates to the GitHub repository
- Your GitHub repository should contain the following files:
  - `euk_stats.txt` - Stats and correlation from genome data
  - `genome_plot.png` - Plot of gene count vs genome size
  - `find_orfs.py`- Finds and translates ORFs from DNA
  - `analyze_eukaryotes.py` - Analyzes genome data with pandas
  - `orf_results.txt` - Output of translated ORF proteins
  - `run.sh` - Script of setup and run commands

## Presentation Instructions

During the session on 6/10/25, each group will: 

- Present their GitHub repository
- Walk through their setup
- Explain their script and logic
- Show example output
- Briefly discuss any challenges or insights

Presentations should take about 5 minutes per group

## Tools You Will Use

- Python and Biopython
- Pandas and Seaborn
- Terminal commands: `cat`,`cd`,`python`,`conda`,`git`
- VSCode for writing and running your script
- GitHub for version control and collaboration
