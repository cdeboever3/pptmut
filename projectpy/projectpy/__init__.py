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

cghub_manifest = ('https://cghub.ucsc.edu/reports/'
                  'SUMMARY_STATS/2014-08-29T12:00:01-0700_data_manifest.tsv')

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

### branchpoint_analysis
subdir = join(root, 'output', 'branchpoint_analysis')
cosmic_intervals01_fasta = join(subdir, 'cosmic_intervals01.fa')
cosmic_intervals01_bps = join(subdir, 'cosmic_intervals01_branchpoints.tsv')
cosmic_intervals01_bps_single = join(
    subdir, 'cosmic_intervals01_branchpoints_single.tsv')

## private_data
subdir = join(root, 'private_data')
cosmic_variants01 = join(subdir, 'cosmic_variants01')

## software
subdir = join(root, 'software')
bedtools = join(subdir, 'bedtools2-2.20.1/bin/bedtools')
mutect = join(subdir, 'muTect', 'muTect-1.1.4.jar')
picard = join(subdir, 'picard-tools-1.118')
R = join(subdir, 'R-3.1.1', 'bin', 'R')
samtools = join(subdir, 'samtools-bcftools-htslib-1.0_x64-linux', 'bin',
                'samtools')

## submodules
subdir = join(root, 'submodules')
svm_bp = join('svm-bpfinder', 'svm_bpfinder.py')


# Random stuff

java = '/usr/lib64/jvm/java-1.6.0/bin/java'

def makedir(p):
    """Make a directory if it doesn't already exist"""
    try:
        os.makedirs(p)
    except OSError:
        pass
