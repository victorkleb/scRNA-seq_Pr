# scRNA-seq_Pr
<br><br>
This repository contains functions to implement the method described in xxx.
<br><br>
The Jupyter notebooks on this page reproduce results for the 33k PBMC data set discussed in the body of the paper.  Results for four other data sets are given in Supplement 1.   Jupyter notebooks with results for each are in the corresponding folders: 10k_heart, 10k_brain, Kang_Lupus, and Macosko_GEO.

Two functions in the file  **nru_DE.py** implement the method and calculate differential expression results for evaluation:
-	**nru** – normalize and rank UMI counts: return statistics, residuals, and intermediate results 
-	**DE_H_stats** – perform Kruskal-Wallis tests to analyze differential expression

These functions, with the others called by **nru**, are described in the file documentation.md
<br><br><br>



Before running the Jupyter notebooks, is necessary to create folders for programs and data.  For example, we use  D:/analyze_Pearson_residuals/ for programs, with a subfolder for each data set.
For the data sets discussed here, the subfolders are  
-	33k_PBMC
-	10k_heart
-	10k_brain
-	Kang_Lupus
-	Macosko_GEO

They are specified near the top of each notebook in the cell headed with the comment **#### user specified**. 

Instructions for downloading the data are given below.  For the 33k PBMC  data from 10x Genomics and the Macosko retinal data, these follow http://github.com/berenslab/umi-normalization  very closely.  The Kang Lupus data are extracted from Bioconductor’s  ExperimentHub with code in a Jupyter notebook. 
<br><br><br>
**Download Instructions**
<br><br>
**_33k PBMC  data from 10x Genomics_**
<br><br>
These instructions are based on  http://github.com/berenslab/umi-normalization.  Modification is necessary due to subsequent changes on the 10x Genomics website.
- visit   https://support.10xgenomics.com/single-cell-gene-expression/datasets/1.1.0/pbmc33k
- provide contact details if necessary
- download  'Gene / cell matrix (filtered)' (79.23 MB); it contains 3 files
    - matrix.mtx
    - genes.tsv
    - barcodes.tsv 
- extract these 3 files to the data subfolder
- download 'Clustering analysis' (23.81 MB) from the same website
- extract the folder ‘kmeans’ to the data subfolder 
<br><br><br>

**_10k_heart data from 10x Genomics_**
<br><br>
These instructions are similar to those for the 33kPBMC  data
- visit   https://support.10xgenomics.com/single-cell-gene-expression/datasets/
- provide contact details if necessary
- specify v3 chemistry
- choose Chromium Demonstration (v3 chemistry)
- choose 10k Heart  Cells from an E18 mouse
- download  ' Feature/cell matrix(filtered)’ (71.3 MB); it contains 3 files
    - matrix.mtx
    - features.tsv   (for the 33kPBMC data, this is genes.tsv)
    - barcodes.tsv 
- extract these 3 files to the data subfolder
- download 'Clustering analysis' (36.3 MB)
- extract the folder ‘clustering’ to the data subfolder 
<br><br><br>

**_10k_brain data from 10x Genomics_**
<br><br>
These are almost identical to the instructions for the heart data
- visit   https://support.10xgenomics.com/single-cell-gene-expression/datasets/
- provide contact details if necessary
- specify v3 chemistry
- choose Chromium Demonstration (v3 chemistry)
- choose 10k Brain  Cells from an E18 mouse
- download  ' Feature/cell matrix(filtered)’ (117 MB); it contains 3 files
    - matrix.mtx
    - features.tsv 
    - barcodes.tsv 
- extract these 3 files to the data subfolder
- download 'Clustering analysis' (32.7 MB)
- extract the folder ‘clustering’ to the data subfolder 
<br><br><br>

**_Kang Lupus data_**
<br><br>
Data are accessed with the Jupyter notebook **extract_Kang_Lupus_data_from_ExperimentHub**
<br><br>
The code is excerpted from the vignette in https://github.com/HelenaLC/muscat.  The program creates 3 python pickle  files in the data subfolder:
- sce_counts_nz_GE_1.pkl
- sce_row_data_nz_GE_1.pkl
- sce_column_data_nz_GE_1.pkl
<br><br><br>




