# scRNA-seq_Pr
<br>

This repository includes 
- five files, each containing  Jupyter noteooks that reproduce the results in xxx and its Supplement 1.   There is a file for each of the data sets that we studied (33k_PBMC, 	10k_heart, 10k_brain, Kang_Lupus, Macosko_GEO)
- the file **nru_DE.py** of functions that implement our algorithms.  The examples in the Jupyter notebooks call two functions:
	- **nru**: normalize and rank UMI counts: return statistics, residuals, and intermediate results 
	- **DE_H_stats**: perform Kruskal-Wallis tests to analyze differential expression
- the file **plot_tab_utilities.py**

The functions in **nru_DE.py**  are described in  **function_documentation.md**.
<br>

Before running the Jupyter notebooks, first create folders for programs and data.  For example, we use  D:/analyze_Pearson_residuals/ for programs, with a subfolder for each data set.  These are specified near the top of each notebook in the cell headed with the comment **#### user specified**. 
<br>

Instructions for downloading the data are in  **data_download_instructions.md**.  For the Macosko retinal data, they are taken directly from http://github.com/berenslab/umi-normalization.  For the 33k PBMC data set from 10x Genomics, they follow that web page very closely; modifications are necessary.

