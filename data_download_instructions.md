# Data Download Instructions
<br>

**33k PBMC  data from 10x Genomics**
<br><br>
These are based on the instructions in  http://github.com/berenslab/umi-normalization.  Modification was necessary due to changes made on the 10x Genomics website after the *berenslab* page was last updated.
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

**10k_heart data from 10x Genomics**
<br><br>
These instructions are similar to those for the 33kPBMC  data
- visit   https://support.10xgenomics.com/single-cell-gene-expression/datasets/
- provide contact details if necessary
- filter on Chemistry Version: select v3
- choose 10k Heart Cells from an E18 mouse (v3 chemistry)
- download  ' Feature/cell matrix(filtered)’ (71.3 MB); it contains 3 files
    - matrix.mtx
    - features.tsv   (for the 33kPBMC data, this is genes.tsv)
    - barcodes.tsv 
- extract these 3 files to the data subfolder
- download 'Clustering analysis' (36.3 MB)
- extract the folder ‘clustering’ to the data subfolder 
<br><br><br>

**10k_brain data from 10x Genomics**
<br><br>
These are almost identical to the instructions for the heart data
- visit   https://support.10xgenomics.com/single-cell-gene-expression/datasets/
- provide contact details if necessary
- filter on Chemistry Version: select v3
- choose 10k Brain  Cells from an E18 mouse
- download  ' Feature/cell matrix(filtered)’ (117 MB); it contains 3 files
    - matrix.mtx
    - features.tsv 
    - barcodes.tsv 
- extract these 3 files to the data subfolder
- download 'Clustering analysis' (32.7 MB)
- extract the folder ‘clustering’ to the data subfolder 
<br><br><br>

**Kang Lupus data**
<br><br>
Data are accessed with the Jupyter notebook **extract_Kang_Lupus_data_from_ExperimentHub** in the folder Kang_Lupus_notebooks
<br><br>
The code is excerpted from the vignette in https://github.com/HelenaLC/muscat.  The program creates 3 python pickle  files in the data subfolder:
- sce_counts_nz_GE_1.pkl
- sce_row_data_nz_GE_1.pkl
- sce_column_data_nz_GE_1.pkl
<br><br><br>

** retinal data**
<br><br>
These instructions are from  http://github.com/berenslab/umi-normalization 
<br><br>
Counts
- visit https://www.ncbi.nlm.nih.gov/geo/
- search for GSE63472
- download GSE63472_P14Retina_merged_digital_expression.txt.gz (50.7 MB)
- extract to GSE63472_P14Retina_merged_digital_expression.txt
- save this .txt file in the data subfolder
<br>

Cluster annotations
- download from http://mccarrolllab.org/wp-content/uploads/2015/05/retina_clusteridentities.txt
- save this .txt file in the data subfolder







