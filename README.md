# Workflow
A workflow to plot gene counts in different tissue types using snakemake.

# Continuous Integration Status
![](https://travis-ci.com/cu-swe4s-fall-2019/workflow-rymo1354.svg?branch=master)

# Installation
To use this package, install `python3`. Necessary packages include:

## Used Packages
- pycodestyle
- numpy
- matplotlib
- graphviz
- snakemake

Install snakemake and graphviz with the following command: 
`conda install -c bioconda snakemake graphviz`

Other packages installed using `conda` installer.

# Usage
The `snakemake` package used the Snakemake file to generate a boxplot of the count of gene expression in different tissue types. It steps through the following:
1. Makes gene_counts files
2. Makes tissue_samples files
3. Makes a boxplot of gene counts in tissue from the above files

To run snakemake, just execute `snakemake` in the repository. To generate a plot of the snakemake workflow, perform `snakemake --dag | dot -Tpng > dag.png` in the repository. This creates a graphviz-based png file of the workflow. To do a dry run, execute `snakemake --dryrun --printshellcmds` 
