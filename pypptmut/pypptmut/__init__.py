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
gencode_gtf = join(subdir, 'gencode', 'gencode.v14.annotation.gtf')


## Random stuff

def makedir(p):
    """Make a directory if it doesn't already exist"""
    try:
        os.makedirs(p)
    except OSError:
        pass
