# scRNA-seq_Pr
<br>
This repository contains functions to implement the method described in xxx.
<br><br>
The files on this page contain Jupyter notebooks that reproduce results for the 33k PBMC data set studed in the body of the paper and for the four data sets discussed in Supplement 1  (10k_heart, 10k_brain, Kang_Lupus, Macosko_GEO).
<br><br>

Two functions in the file  **nru_DE.py** implement the method and calculate differential expression statistics for evaluation:
-	**nru** – normalize and rank UMI counts: return statistics, residuals, and intermediate results 
-	**DE_H_stats** – perform Kruskal-Wallis tests to analyze differential expression

These functions, with the others called by **nru**, are described in the file **function_documentation.md**.
<br><br>

Before running the Jupyter notebooks, is necessary to create folders for programs and data -- and to download the data.  For example, we use  D:/analyze_Pearson_residuals/ for programs, with a subfolder for each data set.
For the data sets discussed here, the subfolders are  
-	33k_PBMC
-	10k_heart
-	10k_brain
-	Kang_Lupus
-	Macosko_GEO

They are specified near the top of each notebook in the cell headed with the comment **#### user specified**. 
<br><br>

Instructions for downloading the data are in the file **data_download_instructions.md**.  For the 33k PBMC  data from 10x Genomics, these follow http://github.com/berenslab/umi-normalization  very closely.   For the Macosko retinal data, they are taken directly from that web page. 

