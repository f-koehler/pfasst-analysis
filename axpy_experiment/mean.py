#!/bin/env python3
import numpy as np
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        exit(1)
    i, n, t, e = np.loadtxt(sys.argv[1], unpack=True)
    print("    naive         transform        Eigen3")
    print("%.4f±%.4f\t%.4f±%.4f\t%.4f±%.4f\n" % (
        np.mean(n), np.std(n),
        np.mean(t), np.std(t),
        np.mean(e), np.std(e)
    ))
