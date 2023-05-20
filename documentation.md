# User-called functions
<br>

**nru ( df_counts_sparse, chunksize**=1000**, nz_min**=50**, n_sample_pairs**=20**, n_genes**=2000 **)**
<br><br>
__parameters__
-	**df_counts_sparse**: sparse pandas data frame containing UMI counts; index contains gene identifiers (e.g. Ensembl IDs or gene symbols); column names are barcodes
-	**chunksize**: the mean sum of squares of Pearson residuals is calculated with dense numpy arrays of  UMI counts for at most **chunksize** genes
-	**nz_min*:  exclude genes with fewer nonzero cells
-	**n_sample_pairs**: number of pairs of complementary random samples of cells used to calculate the sampling-adjusted mean sum of squares of Pearson residuals
-	**n_genes**: number of genes for which Pearson residuals are calculated and returned;  these are the genes with the largest values of sampling-adjusted mean sum of squares of Pearson residuals

They are specified near the top of each notebook in the cell headed with the comment **#### user specified**. 
<br><br>
__value__: dictionary containing 3 items
-	df_gene_stats: pandas data frame with statistics for each gene in the input data frame with nonzero counts on  nz_min  cells or more.  These are
    - the number of nonzero cells
    - total count
    - the mean sum of squares of Pearson residuals calculated with all cells
    - the sampling-adjusted estimate of the mean sum of squares of Pearson residuals
    - a column for each sample of cells, containing the mean sum of squares of Pearson residuals
-	df_selected_cells:  pandas data frame containing one row for each cell and one column for each random sample; the Boolean True/False values identify the cells used in each sample
-	df_residuals: a dense pandas data frame containing n_genes rows – for genes with the largest sampling-adjusted mean sums of squares of Pearson residuals; the data frame has one column for each cell
<br><br><br>
