import os
from os.path import join

# File locations
# Rather than specifying paths all over, I'll just put the paths to commonly
# used files and directories here and use the package to open them. 
def _get_project_dir():
    cwd = os.getcwd()
    upone = os.path.split(cwd)[0]
    return upone

root = _get_project_dir()

## external_data
subdir = join(root, 'external_data')
hg19 = join(subdir, 'hg19', 'hg19.fa')
gencode_gtf = join(subdir, 'gencode', 'gencode.v19.annotation.gtf')
gencode_db = join(subdir, 'gencode', 'gencode.db')
cancer_gene_census = join(subdir, 'cancer_gene_census.xls')

## output

### gencode_processing
subdir = join(root, 'output', 'gencode_processing')
gencode_gene_info = join(subdir, 'gene_info.tsv')
gencode_sj_info = join(subdir, 'sj_info.tsv')

### target_genes
subdir = join(root, 'output', 'target_genes')
target_genes = join(subdir, 'target_genes.tsv')
target_intervals = join(subdir, 'target_intervals.bed')

# Random stuff

def makedir(p):
    """Make a directory if it doesn't already exist"""
    try:
        os.makedirs(p)
    except OSError:
        pass
