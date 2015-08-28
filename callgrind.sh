#!/bin/bash

# pfasst options
BIN=bin/advec_diff_mlsdc
DT=0.001

# output options
EDGE_THRES=1.0
NODE_THRES=1.0



NAME=`date +%Y-%m-%d-%H-%M-%S`

valgrind --tool=callgrind --callgrind-out-file=${NAME}.callgrind ${BIN} --dt ${DT} --tend 0.5 --num_iters 30 --abs_res_tol 1e-10

cat ${NAME}.callgrind | gprof2dot -n ${NODE_THRES} -e ${EDGE_THRES} -s -f callgrind -w --show-samples --skew 0.01 | dot -Tpdf -o ${NAME}.pdf

# kcachegrind ${NAME}.callgrind
