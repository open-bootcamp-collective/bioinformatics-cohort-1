# Overview

This assignment extends the concepts from Session 3 by demonstrating how to use Biopython for programmatic retrieval of sequencing data. It also covers how to access and explore biological databases like NCBI and Ensembl using simple code-based methods

Each group will work collaboratively to complete the tasks below and present their solution at the beginning of the next session. Presentations should be approximately 5 minutes long and demonstrate your understanding of the material.

# Assignment questions:

1) Using biopython Entrez.esearch(), fetch nucleotide sequences of the Homo sapiens gene TP53 from NCBI in FASTA format and save it in the working directory , and save the sequence information in a separate output table using pandas (pd.DataFrame()).
   
2) Find the protein-coding and non-coding regions in the TP53 human gene using Ensembl. Approximately, what is the length of TP53?
   
3) Identify the genes associated with the following Gene IDs from the NCBI and Ensembl databases, and give a brief description of their biological function:
-    672 / ENSG00000012048
-    1080 / ENSG00000001626
-    440121 / ENSG00000268388
-    79645 / ENSG00000163360
-    348 / ENSG00000130203

  Bonus: Use the Ensembl-REST API to obtain the sequences for the genes above using ensembl_rest.sequence_id()

4) How do Genebank and Ensemble differ in their structure, purpose, and use?
   
5) What are the potential downstream consequences of choosing Ensembl versus NCBI as a 
reference database in transcriptomic and genomic analyses?

6) Optional: Use biopython to BLAST search NCBI for homologous TP53 sequences.

## Presentation Instructions:
During the session on 6/12/2025, each group will:
-   Explain biopython script 
-   Walkthrough saved files
-   Answer short answer questions
  
## Tools You Will Use:
- Python and pandas
- Biopython: https://biopython.org/docs/1.76/api/Bio.Entrez.html
- NCBI: https://www.ncbi.nlm.nih.gov/
- Ensembl: https://www.ensembl.org/index.html
- Ensembl API: https://ensemblrest.readthedocs.io/en/latest/

