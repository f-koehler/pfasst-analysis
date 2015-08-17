PY=python3

PLOTS=$(addsuffix .pdf,sdc_heat1d_ndofs sdc_heat1d_nodes mlsdc_heat1d_ndofs mlsdc_heat1d_nodes)

all: ${PLOTS}
%.pdf: %.py
	${PY} $<

.PHONY: clean
clean:
	rm -f *.pdf
