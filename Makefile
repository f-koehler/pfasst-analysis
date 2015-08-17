PY=python3

SCRIPTS=heat1d/sdc_nodes.py heat1d/mlsdc_nodes.py heat1d/sdc_ndofs.py heat1d/mlsdc_ndofs.py
PLOTS=$(addprefix plot/,$(patsubst %.py,%.pdf,${SCRIPTS}))

all: ${PLOTS}
plot/%.pdf: %.py matplotlibrc matplotlib.tex
	${PY} $<

.PHONY: clean
clean:
	rm -f ${PLOTS}
