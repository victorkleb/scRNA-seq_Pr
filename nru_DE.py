
########################
#                      #       
#  program:  nru_DE.py #
#                      #   
########################

import pandas as pd
import numpy  as np

from scipy import stats
 
########################################################################################        
  
def mean_SSQ_Pearson_residuals_array_block  ( block_csr_matrix, seq_depth_vector ):    

  dense_mat = block_csr_matrix.todense()
  n_cells = np.shape ( dense_mat )[1]
  
  total_count = np.sum ( seq_depth_vector )

  pi_hat_vector = np.sum ( dense_mat, axis=1 ) / total_count  
  mu_hat = pi_hat_vector @ seq_depth_vector 

  list_MSSQ_Pr =  list ( np.ravel ( np.sum ( ( np.square ( dense_mat - mu_hat ) ) / mu_hat , axis=1 ) / n_cells ) ) 
  
  return  list_MSSQ_Pr

	
	
	
	
def mean_SSQ_Pearson_residuals  ( counts_sparse_selected_csr, gene_list, chunksize ):    

  n_genes = np.shape ( counts_sparse_selected_csr )[0]   
      
  seq_depth_vector = np.sum ( counts_sparse_selected_csr, axis=0 )
  
  
  MSSQ_list = []    
 
  list_block_start_values = list ( chunksize * np.unique ( np.arange ( n_genes ) // chunksize ) )

  for block_start in list_block_start_values:
    block_end = min ( chunksize + block_start, n_genes )
    block_csr_matrix = counts_sparse_selected_csr[ block_start:block_end, : ]
    	

    list_MSSQ_Pr_block = mean_SSQ_Pearson_residuals_array_block ( block_csr_matrix, seq_depth_vector )
    MSSQ_list = MSSQ_list + list_MSSQ_Pr_block
  	
  ser_PR = pd.Series ( index=gene_list , data = MSSQ_list )  
    
  return  ser_PR
	
	
		  
  	
def   MSSQ_PR_samples  ( counts_sparse_selected_csr, gene_list, cell_list, chunksize, n_sample_pairs ):
  
  n_cells = counts_sparse_selected_csr.shape[1]


  df_selected_cells_list = []

  for sample_pair in range( n_sample_pairs ):
    arr_select =  np.array(np.random.randint(2, size=n_cells), dtype=bool)
    df_select = pd.DataFrame ( index = cell_list, data = arr_select, columns =[ 2* sample_pair ] )
    df_selected_cells_list.append ( df_select )
    df_select = pd.DataFrame ( index = cell_list, data = ~arr_select, columns =[ 2* sample_pair + 1 ] )
    df_selected_cells_list.append ( df_select )  
    
  df_selected_cells = pd.concat ( df_selected_cells_list, axis=1 )
 
 

  df_MSSQ_PR_samples = pd.DataFrame ( index = gene_list )

  for sample in  df_selected_cells.columns.values.tolist():
    print (  'calculating sum of squares of Pearson residuals using cell sample ', sample ) 
      
    arr_cell_select =  df_selected_cells[ sample ].values
    arr_count_sample = counts_sparse_selected_csr [ :, arr_cell_select ]		
		
    df_MSSQ_PR_samples[ sample ] = mean_SSQ_Pearson_residuals ( arr_count_sample, gene_list, chunksize )
	
  df_MSSQ_PR_samples.fillna(0, inplace=True )
  
  return_dict = { 'df_selected_cells':df_selected_cells, 'df_MSSQ_PR_samples':df_MSSQ_PR_samples }
  return return_dict
 
  
 
  
  
def compute_pearson_residuals  ( counts_sparse_selected_csr, gene_list, cell_list,  list_gene_subset ): 

  df_gene_totals = pd.DataFrame ( index = gene_list, data = counts_sparse_selected_csr.sum ( axis=1 ), columns=['gene_total'] )
  df_gene_totals['pi_hat'] = df_gene_totals['gene_total'] / df_gene_totals['gene_total'].sum()  
  df_gene_totals['select'] = df_gene_totals.index.isin ( list_gene_subset )  
  
  df_cell_totals = pd.DataFrame ( index = cell_list, data = counts_sparse_selected_csr.sum ( axis=0 ).transpose(), columns=['sequencing_depth'] )

  arr_counts = counts_sparse_selected_csr [ df_gene_totals['select'].values, : ]
  df_pi_hat_subset = df_gene_totals [ df_gene_totals['select'] ] [['pi_hat']]

  gene_index_list = df_pi_hat_subset.index.values.tolist()
 
   
  seq_depth_vector = ( df_cell_totals['sequencing_depth'].values )  [np.newaxis,:]    
  pi_hat_vector = ( df_pi_hat_subset['pi_hat'].values ) [:,np.newaxis]  
  mu_hat = pi_hat_vector @ seq_depth_vector 
  
  arr_denominator = np.sqrt ( mu_hat )

  arr_numerator = arr_counts - mu_hat
  del arr_counts
  del mu_hat  
 
  arr_residuals = arr_numerator / arr_denominator   
  del arr_numerator
  del arr_denominator  

  df_residuals = pd.DataFrame ( index=gene_index_list , data = arr_residuals, columns=cell_list )
  
  return   df_residuals 

  
  
  
  
def nru ( df_counts_sparse, chunksize=1000,  nz_min=50, n_sample_pairs=20, n_genes=2000 ): 

  df_genes = df_counts_sparse.sum ( axis=1 ).to_frame ( name='count' )
  df_cells = df_counts_sparse.sum ( axis=0 ).to_frame ( name='sequencing_depth' )
   
  counts_scipy_csr_mat = df_counts_sparse.sparse.to_coo().tocsr()

   
  counts_GT_0 = ( counts_scipy_csr_mat > 0 ).astype( int )  
  df_genes['nz_cells'] = np.ravel ( counts_GT_0.sum ( axis=1 ) )
  df_genes['select'] = ( df_genes['nz_cells'] >= nz_min )
  arr_gene_select = df_genes['select'].values  
  df_genes_select = df_genes[ df_genes['select' ] ].drop ( columns=['select'] )   
  counts_sparse_selected_genes = counts_scipy_csr_mat[ arr_gene_select, : ]
  print ( 'counts_sparse_selected_genes.shape: ', counts_sparse_selected_genes.shape )
  
  df_cells['sequencing_depth_gene_select'] = np.ravel ( counts_sparse_selected_genes.sum(axis=0) )   
  df_cells['retain'] = ( df_cells['sequencing_depth_gene_select'] > 0 )
  df_cells_retained = df_cells[ df_cells['retain'] ]
  arr_cells_retained = df_cells['retain'].values
  counts_sparse_selected_csr = counts_sparse_selected_genes[:, arr_cells_retained ]
  print ( 'counts_sparse_selected_csr.shape: ', counts_sparse_selected_csr.shape )   
 

  df_genes_select['M_g'] = mean_SSQ_Pearson_residuals ( counts_sparse_selected_csr, df_genes_select.index.values.tolist(), chunksize )
  print (  'calculating sum of squares of Pearson residuals using all cells' )

  
  s_MSSQ_PR_dict =  MSSQ_PR_samples  ( counts_sparse_selected_csr,  df_genes_select.index.values.tolist(), df_cells_retained.index.values.tolist(), chunksize, n_sample_pairs )
  df_selected_cells = s_MSSQ_PR_dict [ 'df_selected_cells' ]
  df_MSSQ_PR_samples = s_MSSQ_PR_dict [ 'df_MSSQ_PR_samples' ]

  df_sa_MSSQ_PR = df_MSSQ_PR_samples.min ( axis=1 ).to_frame ( name = 'A_g' )

  ##### replace small values obtained by randomization with the minimum  mean SSQ of Pearson residuals using all cells
  ##### this eliminates the risk of returning zero for sa_MSSQ_PR
  min_MSSQ_PR = df_genes_select['M_g'].min()
  df_sa_MSSQ_PR.loc [ df_sa_MSSQ_PR['A_g'] < min_MSSQ_PR ] = min_MSSQ_PR
  
  df_gene_stats = pd.concat ( [ df_genes_select, df_sa_MSSQ_PR, df_MSSQ_PR_samples ], axis=1 ) 
   
  
  df_sa_MSSQ_PR['rank'] = df_sa_MSSQ_PR['A_g'].rank ( ascending=False )
  ser_select_genes = ( df_sa_MSSQ_PR['rank'] <= n_genes )
  list_gene_subset = ser_select_genes[ ser_select_genes ].index.values.tolist()  
  df_residuals = compute_pearson_residuals  ( counts_sparse_selected_csr,  df_genes_select.index.values.tolist(), df_cells_retained.index.values.tolist(), list_gene_subset )  # NOT transpose
  

  return_dict = {'df_gene_stats':df_gene_stats, 'df_selected_cells':df_selected_cells, 'df_residuals':df_residuals}  
  return return_dict    
  	
########################################################################################

def DE_H_stats ( df_residuals, df_clusters ):

  df_cluster_residuals_tr = df_clusters[['Cluster']].merge ( df_residuals.transpose(), how='inner', left_index=True, right_index=True )

  cluster_list = df_clusters['Cluster'].unique().tolist()
  cluster_list.sort()

  df_stats_tuples_list = []

  for gene in df_residuals.index.values.tolist():
    df_cluster_residuals_column = df_cluster_residuals_tr[['Cluster', gene]] 
  
    stats_input_array_list  = []
    for cluster in cluster_list:
      df_res_cluster  = df_cluster_residuals_column [ df_cluster_residuals_column['Cluster'] == cluster ]
      stats_input_array_list.append ( df_res_cluster[gene].values )
  
    stat, p_value = stats.kruskal( *tuple ( stats_input_array_list ) )
    stats_tuple = ( gene, stat, p_value )  
    df_stats_tuples_list.append ( stats_tuple )

  df_stats = pd.DataFrame ( data = df_stats_tuples_list, columns = ['gene', 'H_stat', 'p_value'] ).set_index( ['gene'] )

  return df_stats    
    
########################################################################################




