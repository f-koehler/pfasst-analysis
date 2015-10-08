import subprocess
import time
import numpy as np
from uncertainties import ufloat

repetitions = range(0, 1000)
cmd = ["--dt", "0.05", "--tend", "1", "-c", "--abs_res_tol", "1e-15", "--num_iters", "30", "--num_dofs", "6144"]


def time_naive():
    t1 = time.perf_counter()
    subprocess.call(["./heat1d_sdc_naive"]+cmd)
    t2 = time.perf_counter()
    return (t2-t1)


def time_transform():
    t1 = time.perf_counter()
    subprocess.call(["./heat1d_sdc_transform"]+cmd)
    t2 = time.perf_counter()
    return (t2-t1)


def time_eigen():
    t1 = time.perf_counter()
    subprocess.call(["./heat1d_sdc_eigen"]+cmd)
    t2 = time.perf_counter()
    return (t2-t1)


with open("results.txt", "w") as f:
    print("Config: "+" ".join(cmd))
    times_naive = []
    times_transform = []
    times_eigen = []
    for r in repetitions:
        times_naive.append(time_naive())
        times_transform.append(time_transform())
        times_eigen.append(time_eigen())
        times = "%d\t%.10f\t%.10f\t%.10f" % (r, times_naive[-1], times_transform[-1], times_eigen[-1])
        f.write(times+"\n")
        f.flush()
        print(times)
