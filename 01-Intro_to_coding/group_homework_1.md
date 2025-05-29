# Group Homework 1: Set Up and Sequence Stats

## Overview

This homework is designed to reinforce key concepts from Session 1, including Conda environments, basic terminal usage, Git/GitHub, Python scripting, and basic sequence operations using Biopython.

Each group will work collaboratively to complete the tasks below and present their solution at the beginning of the next session. Presentations should be approximately 5 minutes long and demonstrate your understanding of the material.

## Assignment Tasks

### 1. Project Setup (Environment + Git)

As a group:

- Create a folder called `sequence_stats_project`
- Create and activate a new conda environment with Python 3.10
- Install Biopython using either `conda install biopython` or `pip install biopython`
- Initialize a Git repository in the folder using `git init`
- Create a GitHub repository (one per group)
- Link your local repository to GitHub and push your code

### 2. Write a Python Script

Create a file called `analyze_sequences.py` containing the following:

- A list of 5 DNA sequences stored as strings
- A function `gc_content(seq)` that computes the GC content of a sequence
- A function `is_valid(seq)` that checks whether a sequence only contains A, T, C, or G
- A loop that iterates through each sequence and prints:
  - The sequence
  - Its length
  - Its GC content
  - Whether it is valid

Bonus: Use `Bio.Seq.Seq` to create each sequence and print its reverse complement.

### 3. Run and Save Output

Run your script from the terminal and save the output to a file named `results.txt`:

```bash
python analyze_sequences.py > results.txt
```

### 4. Git Workflow

- Stage and commit your changes using `git add` and `git commit`
- Push your updates to the GitHub repository
- Your repository should contain the following files:
  - `run.sh` file containing the terminal commands used for setup
  - `analyze_sequences.py` python script
  - `results.txt` text file containing script output

## Presentation Instructions

During the next session, each group will:

- Present their GitHub repository
- Walk through their environment setup
- Explain their script and logic
- Show example output
- Briefly discuss any challenges or insights

Presentations should take about 5 minutes per group.

## Tools You Will Use

- Conda and pip
- Terminal commands: `cd`, `ls`, `mkdir`, `touch`
- Git commands: `git init`, `git add`, `git commit`, `git push`
- Python: variables, lists, functions, loops
- Biopython: `Bio.Seq.Seq`
- VSCode for writing and running code
- GitHub for version control and collaboration
