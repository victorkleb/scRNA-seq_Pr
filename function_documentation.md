# Function Documentation
<br>

**compute_pearson_residuals  ( counts_sparse_selected_csr, gene_list, cell_list,  list_gene_subset )**
<br><br>
called by: **nru**
<br><br>

__description__

Compute Pearson residuals for the sparse array of counts, returning a dense pandas data frame.  Return values only for genes in the 4th parameter - **list_gene_subset**.

__arguments__
-	**counts_sparse_selected_csr**: a sparse scipy csr matrix of counts
-	**gene_list**: python list of gene identifiers; its length equals the number of rows of the input array **counts_sparse_selected_csr**
-	**cell_list**: python list of cell identifiers (typically barcodes); its length equals the number of columns of **counts_sparse_selected_csr**
-	**list_gene_subset**: genes for which Pearson residuals are to be computed – for example the 2,000 with the largest values of sampling-adjusted mean SSQ of Pearson residuals
<br><br>

__value__: pandas data frame
-	index: values in the input **list_gene_subset**
-	columns: values in the input **cell_list**
-	data: Pearson residuals 
<br><br><br>

**DE_H_stats ( df_residuals, df_clusters )**
<br><br>
__description__

Given a pandas data frame of Pearson residuals and a clustering of cells, perform Kruskal-Wallis tests for each gene.  Return H-statistics and p-values. 
<br><br>

__arguments__
-	**df_residuals**: dense pandas data frame containing (Pearson) residuals; for example as returned by **nru**
-	**df_clusters**:  pandas data frame:  index contains cell identifiers (typically barcodes), the one column contains cluster assignments
<br><br>

__value__: pandas data frame 
-	index contains gene identifiers; it is identical to the index of the input **df_residuals**
-	two columns:   H_stat,  p_value
<br><br><br>

**mean_SSQ_Pearson_residuals  ( counts_sparse_selected_csr, gene_list, chunksize )**
<br><br>
called by: **nru, MSSQ_PR_samples**
<br><br>

__description__

Given a sparse array of counts, calculate the sequencing depths as the column sums.
<br>

Segment rows into sub-matrices, each with at most **chunksize** rows, calculate the mean SSQ of Pearson residuals for the genes represented by each sub-matrix, and combine the results.
<br><br>

__arguments__
-	**counts_sparse_selected_csr**: a sparse scipy csr matrix of counts; this may be the count matrix containing all genes and cells of interest, or a submatrix containing a random sample of approximately half of the cells – and genes with at least one nonzero count for some cell
-	**gene_list**: python list of gene identifiers; its length equals the number of rows of the input array **counts_sparse_selected_csr**
-	**chunksize**: maximum number of rows used in calculation of mean SSQ of Pearson residuals with a dense submatrix of counts
<br><br>

__value__: pandas series
-	index: values in the input **gene_list**
-	data: mean SSQ of Pearson residuals for the input count matrix
<br><br><br>

**mean_SSQ_Pearson_residuals_array_block  ( block_csr_matrix, seq_depth_vector )**
<br><br>
called by: **mean_SSQ_Pearson_residuals**
<br><br>

__description__

Convert a sparse array of UMI counts to a dense numpy array, then calculate the mean SSQ of their Pearson residuals.   This requires the sequencing depths of all cells represented in the input array; these are specified by the function’s second parameter. <br><br>

__arguments__
-	**block_csr_matrix**: a sparse scipy csr matrix of counts; it contains a set of contiguous rows of the count matrix input to **mean_SSQ_Pearson_residuals** 
-	**seq_depth_vector**: a 1-dimensional numpy array with length equal to the number of columns of the input **block_csr_matrix**
<br><br>

__value__: python list containing the mean SSQ of Pearson residuals for the genes represented by the rows of the input matrix
<br><br><br>

**MSSQ_PR_samples  ( counts_sparse_selected_csr, gene_list, cell_list, chunksize, n_sample_pairs )**
<br><br>
called by: **nru**
<br><br>

__description__

Perform random sampling to define (complementary pairs of) subsets of cells. 
<br>

Each subset of cells defines a sub-matrix of UMI counts.  For each of these, calculate the mean SSQ of Pearson residuals.  The minima of these values are the sampling-adjusted mean SSQ of Pearson residuals.
<br><br>

__arguments__
-	**counts_sparse_selected_csr**: a sparse scipy csr matrix of counts
-	**gene_list**: python list of gene identifiers; its length equals the number of rows of the input array **counts_sparse_selected_csr**
-	**cell_list**: python list of cell identifiers (typically barcodes); its length equals the number of columns of **counts_sparse_selected_csr**
-	**chunksize**: maximum number of rows used in calculation of mean SSQ of Pearson residuals with a dense submatrix of counts
-	**n_sample_pairs**: number of pairs of complementary random samples of cells used to calculate the sampling-adjusted mean SSQ of Pearson residuals 
<br><br>

__value__: dictionary containing 2 pandas data frames
-	df_selected_cells:  pandas data frame containing one row for each cell in **cell_list**  and one column for each random sample; the Boolean True/False values identify the cells used in each sample
-	df_MSSQ_PR_samples: a pandas data frame containing  one row for each gene in **gene_list** and a total of  2* **n_sample_pairs**  columns – one for each sample of cells.   The values in each column are the mean SSQ of Pearson residuals calculated using the sample of cells identified with TRUE values in the corresponding column of the output data frame df_selected_cells
<br><br><br>

**nru ( df_counts_sparse, chunksize**=1000, **nz_min**=50, **n_sample_pairs**=20, **n_genes**=2000 **)**
<br><br>
__description__

For the input UMI count matrix, provided as a sparse pandas data frame
-	count the number of cells with nonzero counts for each gene
-	restrict to genes for which this count exceeds a specified minimum
-	for each of these genes, calculate
	- the mean SSQ of Pearson residuals – using all cells in the count matrix
	- the mean SSQ of Pearson residuals – for multiple pairs of random samples (complementary samples of approximately half of the cells)
	- the sampling-adjusted mean SSQ of Pearson residuals 
-	for genes with the **n_genes** largest values of the sampling-adjusted mean SSQ of Pearson residuals, calculate a dense matrix of residuals

Returns
-	a data frame containing – for each gene with sufficient nonzero cells – the number of nonzero cells, its total count, the mean SSQ of Pearson residuals calculated with all cells, the sampling-adjusted mean SSQ of Pearson residuals, and a column for each sample of cells, containing the mean SSQ of Pearson residuals calculated with that sample
-	a data frame identifying the cells in each sample
-	the matrix of Pearson residuals as a dense pandas data frame

Calculating the sums of squares of Pearson residuals is faster with dense matrices but requires more storage.  To balance these requirements, calculations are performed with dense sub-matrices for subsets of genes.   

Note that excluding some genes from analysis may leave some cells without UMI counts.  These cells are excluded.  As a result, the output data frame of Pearson residuals may have fewer columns than the input data frame of UMI counts.
<br><br>

__arguments__
-	**df_counts_sparse**: sparse pandas data frame containing UMI counts; index contains gene identifiers (e.g. Ensembl IDs or gene symbols); column names are cell identifiers (typically barcodes)
-	**chunksize**: the mean SSQ of Pearson residuals is calculated with dense numpy arrays of  UMI counts for at most **chunksize** genes
-	**nz_min**:  exclude genes with fewer nonzero cells
-	**n_sample_pairs**: number of pairs of complementary random samples of cells used to calculate the sampling-adjusted mean SSQ of Pearson residuals
-	**n_genes**: number of genes for which Pearson residuals are calculated and returned;  these are the genes with the largest values of sampling-adjusted mean SSQ of Pearson residuals
<br><br>

__value__: dictionary containing 3 pandas data frames
-	df_gene_stats: pandas data frame with statistics for each gene in the input data frame with nonzero counts on  **nz_min**  cells or more.  Its columns are
    - the number of nonzero cells
    - total count
    - the mean SSQ of Pearson residuals calculated with all cells
    - the sampling-adjusted mean SSQ of Pearson residuals
    - a column for each sample of cells, containing the mean SSQ of Pearson residuals
-	df_selected_cells:  pandas data frame containing one row for each cell and one column for each random sample; the Boolean True/False values identify the cells used in each sample
-	df_residuals: a dense pandas data frame containing **n_genes** rows – for genes with the largest sampling-adjusted mean SSQ of Pearson residuals; the data frame has one column for each cell
<br><br><br>






























