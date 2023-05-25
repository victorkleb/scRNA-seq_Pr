# scRNA-seq_Pr
<br>
This repository includes 
-	Five files, each containing  Jupyter noteooks that reproduce the results in xxx and its Supplement 1.   There is one file for each of the data sets that we studied.
-	The file **nru_DE.py** of functions that implement our algorithms.  The examples in the Jupyter notebooks call two functions:
	- **nru**: normalize and rank UMI counts: return statistics, residuals, and intermediate results 
	- **DE_H_stats**: perform Kruskal-Wallis tests to analyze differential expression
-	The file **plot_tab_utilities.py**: functions used in plotting
<br><br>
	
The functions in **nru_DE.py*  are described in the file **function_documentation.md**.
<br><br>

Before running the Jupyter notebooks, first create folders for programs and data.  For example, we use  D:/analyze_Pearson_residuals/ for programs, with a subfolder for each data set.
For the data sets discussed here, the subfolders are  
-	33k_PBMC
-	10k_heart
-	10k_brain
-	Kang_Lupus
-	Macosko_GEO
<br><br>

Subfolders are specified near the top of each notebook in the cell headed with the comment **#### user specified**. 
<br><br>

Instructions for downloading the data are in the file **data_download_instructions.md**.  For the Macosko retinal data, they are taken directly from http://github.com/berenslab/umi-normalization.  For the 33k PBMC data set from 10x Genomics, they follow that web page very closely; modifications are necessary.

