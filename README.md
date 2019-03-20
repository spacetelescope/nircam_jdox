# nircam_jdox

[![PyPI - License](https://img.shields.io/pypi/l/Django.svg)](https://github.com/spacetelescope/jwql/blob/master/LICENSE)
[![STScI](https://img.shields.io/badge/powered%20by-STScI-blue.svg?colorA=707170&colorB=3e8ddd&style=flat)](http://www.stsci.edu)


The nircam_jdox repository is meant to act as a simple collection of code and ancillary data files that have been used to create tables and figures on the [NIRCam JDox webpages](https://jwst-docs.stsci.edu/display/JTI/Near+Infrared+Camera).

## Installation

Getting `nircam_jdox` up and running on your own computer requires four steps, detailed below:
1. Cloning the GitHub repository
1. Installing the `conda`environment
1. Installing the python package

### Prerequisites

It is highly suggested that contributors have a working installation of `anaconda` or `miniconda` for Python 3.6.  Downloads and installation instructions are  available here:

- [Miniconda](https://conda.io/miniconda.html)
- [Anaconda](https://www.continuum.io/downloads)

Requirements for contributing to the `nircam_jdox` package will be included in the `nircam_jdox` `conda` environment, which is included in our installation instructions below.

### Clone the `nircam_jdox` repo

You first need to clone the current version of `nircam_jdox`. The simplest way to do this is to go to the directory you want your copy of the repository to be in and clone the repository there. Once you are in the directory you can do the following:

```
git clone https://github.com/spacetelescope/nircam_jdox.git
cd nircam_jdox
```

or, if you would rather use `SSH` instead of `https`, type
```
git clone git@github.com:spacetelescope/nircam_jdox.git
cd nircam_jdox
```
instead, and then proceed as stated.

### Environment Installation

Following the download of the `nircam_jdox` repository, contributors can then install the `nircam_jdox` `conda` environment via the `environment.yml` file, which contains all of the dependencies for the project.  First, one should ensure that their version of `conda` is up to date:

```
conda update conda
```

Next, one should activate the `base` environment:

```
source activate base
```

Lastly, one can create the `nircam_jdox` environment via the `environment.yml` file:

```
conda env create -f environment.yml
```

### Package Installation

Next, you need to install the `nircam_jdox` package. While still in the `nircam_jdox/` directory, run the following command to set up the package:

```
python setup.py develop
```
The package should now appear if you run `conda list nircam_jdox`.


## Software Contributions

Before you begin contributing to the `nircam_jdox` development please review our [suggested git workflow page](https://github.com/spacetelescope/nircam_jdox/wiki/git-&-GitHub-workflow-for-contributing), which contains an in-depth explanation of the workflow.

The following is a bare-bones example of a best work flow for contributing to the project:

1. Create a fork off of the `spacetelescope` `nircam_jdox` repository.
2. Make a local clone of your fork.
3. Ensure your personal fork is pointing `upstream` properly.
4. Create a branch on that personal fork.
5. Make your software changes.
6. Push that branch to your personal GitHub repository (i.e. `origin`).
7. On the `spacetelescope` `nircam_jdox` repository, create a pull request that merges the branch into `spacetelescope:master`.
8. Assign a reviewer from the team for the pull request.
9. Iterate with the reviewer over any needed changes until the reviewer accepts and merges your branch.
10. Delete your local copy of your branch.


## Issue Reporting / Feature Requests

Users who wish to report an issue or request a new feature may do so by submitting a new issue on GitHub: https://github.com/spacetelescope/nircam_jdox/issues


## Code of Conduct

Users and contributors to the `nircam_jdox` repository should adhere to the [Code of Conduct](https://github.com/spacetelescope/nircam_jdox/blob/master/CODE_OF_CONDUCT.md).  Any issues or violations pertaining to the Code of Conduct should be brought to the attention of a `nircam_jdox` team member.
