PY=python3

SCRIPTS=advec_diff/coarse_factor.pdf advec_diff/nodes.py advec_diff/sdc_dt.py
PLOTS=$(addprefix plot/,$(patsubst %.py,%.pdf,${SCRIPTS}))

all: ${PLOTS}
plot/%.pdf: %.py matplotlibrc matplotlib.tex
	${PY} $<

.PHONY: clean
clean:
	rm -f ${PLOTS}
