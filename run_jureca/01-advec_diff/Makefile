JOBS:=$(shell find . -mindepth 1 -maxdepth 1 -type d)
TARGETS:=$(addsuffix /run.out, ${JOBS})

all: ${TARGETS}
%/run.out: %/run.job advec_diff_pfasst
	cd $(dir $@) && sbatch run.job

clean:
	rm -f *_*_*/*.{out,err}
	rm -f *_*_*/mpi-rank-*.log
