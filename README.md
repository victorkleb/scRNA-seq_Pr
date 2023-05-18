# scRNA-seq_Pr

<br />
<br />
The approach uses
- binomial deviance to rank genes for filtering
- random forest classification to produce proximities to cluster genes and cells
- spectral consensus clustering using the random forest proximities
- distributions of adjusted Rand index or Misclassification Error distance to determine an appropriate number of clusters
- Laplacian scores computed with random forest cell proximities to confirm the gene ranks and provide additional - validation of the methodology.
<br />