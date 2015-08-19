PY=python3

SCRIPTS=heat1d/coarse_factor.pdf heat1d/nodes.py heat1d/sdc_dt.py
PLOTS=$(addprefix plot/,$(patsubst %.py,%.pdf,${SCRIPTS}))

all: ${PLOTS}
plot/%.pdf: %.py matplotlibrc matplotlib.tex
	${PY} $<

.PHONY: clean
clean:
	rm -f ${PLOTS}
