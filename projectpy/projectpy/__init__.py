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

## data
subdir = join(root, 'data')
cghub_manifest = join(subdir, 'cghub', 'LATEST_MANIFEST.tsv')

## external_data
subdir = join(root, 'external_data')
GRCh37_lite = join(subdir, 'GRCh37', 'GRCh37-lite.fa')
gencode_gtf = join(subdir, 'gencode', 'gencode.v19.annotation.gtf')
gencode_db = join(subdir, 'gencode', 'gencode.db')
cancer_gene_census = join(subdir, 'cancer_gene_census.xls')
dbsnp = join(subdir, 'dbsnp', 'All.vcf')
cosmic_all = join(subdir, 'cosmic', 'cosmic_all.vcf')

## output

### gencode_processing
subdir = join(root, 'output', 'gencode_processing')
gencode_gene_info = join(subdir, 'gene_info.tsv')
gencode_sj_info = join(subdir, 'sj_info.tsv')

### target_genes
subdir = join(root, 'output', 'target_genes')
cosmic_genes01 = join(subdir, 'cosmic_genes01.tsv')
cosmic_intervals01 = join(subdir, 'cosmic_intervals01.bed')
cosmic_intervals_merged01 = join(subdir, 'cosmic_intervals_merged01.bed')

### target_samples
subdir = join(root, 'output', 'target_samples')
target_samples = join(subdir, 'target_samples.tsv')

## private_data
subdir = join(root, 'private_data')
cosmic_variants01 = join(subdir, 'cosmic_variants01')

## software
subdir = join(root, 'software')
mutect = join(subdir, 'muTect/muTect-1.1.4.jar')
picard = join(subdir, 'picard-tools-1.118')

# Random stuff

java = '/usr/lib64/jvm/java-1.6.0/bin/java'

def makedir(p):
    """Make a directory if it doesn't already exist"""
    try:
        os.makedirs(p)
    except OSError:
        pass
