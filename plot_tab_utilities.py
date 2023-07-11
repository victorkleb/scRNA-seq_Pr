  

###################################
#                                 #       
#  program: plot_tab_utilities.py #
#                                 #   
###################################  



import pandas as pd
import numpy  as np 


        
######################################################################################## 

def pv_table_noprint_margins (  df, col1,   col2 ):
  df_copy = df.copy() 
  df_copy ['count'] = 1
  pt = pd.pivot_table( df_copy, values='count',  index=[ col1 ], columns=[ col2 ], fill_value=0, aggfunc=np.sum, margins=True, margins_name='Total' ).fillna(0)
  pti = pt.astype(int)  
  return pti
   
########################################################################################     

def plot_ax ( df, ax, subplot_label, x, y, xlabel, ylabel, yscale_log=True, line_slope='diagonal' ):

  ax.scatter ( df[x], df [ y ], marker='o', color='k',  s=0.1)
  
  if ( line_slope == 'diagonal' ): 
    x_min = min ( df[x].min(), df [ y ].min() )
    x_max = max ( df[x].max(), df [ y ].max() )
    ax.plot ( [ x_min, x_max ], [x_min, x_max],  linewidth=1, color='orange')
	
  if ( line_slope == 'horizontal' ): 
    ax.axhline( y=1, linewidth=1, color='orange') 	
	
	
  ax.set_xscale('log')
  
  if ( yscale_log ):  
    ax.set_yscale('log') 

  ax.set_xlabel ( xlabel, fontsize=5.5 )	
  ax.set_ylabel ( ylabel , fontsize=5.5 )	
  ax.tick_params(labelsize=4.5, which='major' )    
  ax.minorticks_off()
	
  right = ax.spines["right"]	
  right.set_visible(False)
  top = ax.spines["top"]	
  top.set_visible(False)

  ax.text(-0.05, 1.05, subplot_label, fontsize=5.5, fontweight='bold', va='top', ha='right', transform=ax.transAxes,)

########################################################################################    
   
def comma_fmt (x):
  return  f"{ x:,.0f}"
  
def dec_2_fmt (x):
  return '%1.2f' % x
    
########################################################################################
