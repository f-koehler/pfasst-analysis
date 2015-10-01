OPTIONS=-s -f callgrind -w --show-samples --skew 0.01

all: eigen3.pdf naive.pdf std_transform_iterators.pdf
eigen3.pdf: eigen3.callgrind
	gprof2dot ${OPTIONS} $< | dot -Tpdf -o $@
	pdfcrop --hires $@ $@
naive.pdf: naive.callgrind
	gprof2dot ${OPTIONS} $< | dot -Tpdf -o $@
	pdfcrop --hires $@ $@
std_transform_iterators.pdf: std_transform_iterators.callgrind
	gprof2dot ${OPTIONS} $< | dot -x -Tpdf -o $@
	pdfcrop --hires $@ $@

.PHONY: clean
clean:
	rm *.pdf
