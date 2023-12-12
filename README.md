# scRNA-seq_Pr
<br>

This repository includes
- Five folders, each containing  Jupyter notebooks that reproduce the results in the preprint "Normalization and gene selection for single-cell RNA-seq UMI data using 
sampling-adjusted sums of squares of Pearson residuals with a Poisson model" and its Supplement 1.   There is one folder for each data set.
- The file **nru_DE.py** of functions that implement the algorithms.  The examples in the notebooks call three functions:
	- **nru**: normalize and rank UMI counts: return statistics, residuals, and intermediate results 
	- **DE_H_stats**: perform Kruskal-Wallis tests to analyze differential expression
	- **mean_SSQ_Pearson_residuals** 
		- called by **nru** in the notebooks 01_compute_Mg_Ag_data_prep_for_Lg_Sg
		- called in the notebooks 02_Fig_1_and_Table to calculate the mean SSQ of Pearson residuals for all genes in the input count matrix. In the paper, these are plotted in Figure 1A and summarized in Table 2.
- The file **plot_tab_utilities.py** 
<br><br>
	
Functions in **nru_DE.py**  are described in **function_documentation.md**.
<br><br>
Before running the Jupyter notebooks, please create folders for programs and data.  For example, we use  D:/analyze_Pearson_residuals/ for programs, with a subfolder for each data set.

Then copy the files **nru_DE.py** and **plot_tab_utilities.py**  to the program folder.

For the data sets discussed here, the subfolders are  
-	33k_PBMC
-	10k_heart
-	10k_brain
-	lupus
-	retinal
<br><br>

Folders are specified near the top of each notebook in the cell headed with the comment **#### user specified**. 
<br><br>

Instructions for downloading the data are in  **data_download_instructions.md**.  For the  retinal data, they are taken directly from http://github.com/berenslab/umi-normalization.  For the 33k PBMC data set from 10x Genomics, they follow that web page very closely; modifications were necessary due to changes made on the 10x Genomics website after the *berenslab* page was last updated.
<br><br>

Each subfolder contains 11 notebooks
-	one is data-specific (e.g. prep_33k_PBMC); it prepares 2 pandas data frames
	- a sparse data frame containing UMI counts
    - a clustering (provided with the data)	
- the remaining 10 notebooks perform the reported analyses; there are two versions of notebooks 06 and 10, depending on whether or not genes are notated in the plots
	- 01_compute_Mg_Ag_data_prep_for_Lg_Sg
	- 02_Fig_1_and_Table
	- 03_compute_L_g
	- 04_compute_S_g
	- 05_Figs_3_5_and_Tables
	- 06_Fig_7_and_Table **or** 06_Fig_7_notated_and_Table
	- 07_compute_Ag_for_complementary_samples
	- 08_compute_Lg_for_complementary_samples
	- 09_compute_Sg_for_complementary_samples
	- 10_Figs_2_4_6_and_Tables **or** 10_Figs_2_notated_4_6_and_Tables
<br>

For the lupus data there is an additional notebook - extract_Kang_Lupus_data_from_ExperimentHub - as explained in **data_download_instructions.md**.

	
	