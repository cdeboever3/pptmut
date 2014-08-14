pptmut
======

Research project.

## Dependencies

### Python

A working IPython notebook environment is needed along with some of the common
scientific python packages that you likely already have as part of a working
IPython notebook environment. I recommend using 
[Anaconda python](https://store.continuum.io/cshop/anaconda/) since it includes
most of the needed packages. Besides the default Anaconda packages, you will 
need

* pybedtools
* cdpybio

You can download cdpybio from it's [github
repo](https://github.com/cdeboever3/cdpybio) and install using 
`python setup.py install`.

You will also need to install the project specific python package from this
repository. If you are using Anaconda, I'd recommend making a new environment.
From the `pptmut` directory, you can change into `pypptmut` and install using
`python setup.py install` or `python setup.py develop` if you think you may want
to make changes to the pypptmut package and have these changes instantly 
propagated.

## R

You will need an R installation linked with rpy2 that is installed for the
python installation that you will run the notebooks with. You will need to
install Bioconductor and Gviz.
