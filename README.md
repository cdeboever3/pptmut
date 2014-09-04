pptmut
======

Research project.

## Dependencies

### Python

A working IPython notebook environment is needed along with some of the common
scientific python packages that you likely already have as part of a working
IPython notebook environment. I recommend using 
[Anaconda python](https://store.continuum.io/cshop/anaconda/) since it includes
most of the needed packages. If you are using Anaconda, I'd recommend making a
new environment. Besides the default Anaconda packages, you will need
`pybedtools` which you can install using `pip install pybedtools`.

You'll also need `cdpybio` which is included in this repository as a submodule.
After cloning this repository from Github, change into the repo directory and
run:

	git submodule init
	git submodule update

You will also need to install the project specific python package from this
repository. From the `projectpy` directory, you can change into `projectpy` and
install using `python setup.py install` or `python setup.py develop` if you
think you may want to make changes to the projectpy package and have these
changes instantly propagated.

### SVM-BPfinder

You'll need SVM-BPfinder as well. It's included here as a submodule, but after
initializing and updating the submodules you'll need to download
[http://svmlight.joachims.org/](SVMlight) and place it in 
`submodules/svm-bpfinder/SCRIPTS`. See the `submodules/svm-bpfinder/README` for
more info.

### External software notebook

Running the "External Software" notebook will download and install most of the
necessary external software in this project's directory. However, There are a
few pieces of software that must be installed manually.

### Software to be installed manually

You must install [igvtools](http://www.broadinstitute.org/software/igv/log-in)
and [muTect](http://www.broadinstitute.org/cancer/cga/mutect) manually as these
are available from the Broad but require registration/login. After downloading
these tools, place the unzipped directories in the `tcga/software` directory.
If you do this correctly, you should have would expect `tcga/software/IGVTools`
and `tcga/software/muTect`.

### Variant calling and GTFuse

If you want to do the variant calling with GTFuse, you'll need a working
version of GTFuse in your path. 
