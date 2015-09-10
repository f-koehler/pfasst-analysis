pfasst-analysis
===============

Warning
-------
I know this repository is quite unstructured and even contains binaries (normally you should never do that). This is due to the many different small tasks I had to deal with. Maybe you can still find something of interest. I look at this repo as a collection of all the little helpers that I use to do analyses of PFASST.


About
-----
During the Guest Student Programme at [FZ Jülich](http://www.fz-juelich.de/portal/DE/Home/home_node.html) I worked with @torbjoernk at his reimplementation of [PFASST++](https://github.com/torbjoernk/PFASST). The old version of this library can be found [here](https://github.com/Parallel-in-Time/PFASST).

To describe PFASST I cite the project page:

> The PFASST project is a C++ implementation of the parallel full approximation scheme in space and time (PFASST) algorithm, which in turn is a time-parallel algorithm for solving ODEs and PDEs. It also contains basic implementations of the spectral deferred correction (SDC) and multi-level spectral deferred correction (MLSDC) algorithms.

This repository contains a collection of tools that I created to create convergence plots and to do serial profiling as well as many configuration files (super computer modules, jobs and configurations). To create the plots you have to use the `feature/example-output` branch from [my fork](https://github.com/f-koehler/PFASST). I think from the symlinks in `./bin` you can guess where to put pfasst and where the binaries should be.

Here is a list of tools I used:

- [valgrind](http://valgrind.org/) 3.10.1 (mostly callgrind)
- [perf](https://perf.wiki.kernel.org/index.php/Main_Page) 4.2.0 (I think I do not have any scripts in the repo as I used it manually)
- [gprof2dot](https://github.com/jrfonseca/gprof2dot.git) 2015.02.03 (awesome tool to visualize traces from different serial profilers, not only C++)
- [Score-P](http://www.vi-hps.org/projects/score-p/) and [Vampir](https://www.vampir.eu/) (different versions on the supercomputers to do MPI profiling and to reproduce the PFASST algorithm image in the [M. Emmett and M. L. Minion paper](http://dx.doi.org/10.2140/camcos.2012.7.105))
- [jinja2](http://jinja.pocoo.org/) 2.8 ((for templating)
- [matplotlib](http://matplotlib.org/) 1.4.3 and [numpy](http://www.numpy.org/) 1.9.2 (to create rudimentary plots)
