import subprocess
import re
from matplotlib import pyplot as plt
import numpy as np

dt = 0.05
tend = 0.05
num_nodes = 4
num_iters = 20
abs_res_tol = 1e-10

regex_abs_res = re.compile(r"t\[3\]\=\d+\.\d+(e(\-|\+)\d+)?\s+\|abs\s+residual\|\s+\=\s+(?P<abs_res>\d+\.\d+(e(\-|\+)\d+)?)")

def call(exe, extra_args):
    return subprocess.check_output(["bin/"+exe, "--tend", str(tend), "--num_nodes", str(num_nodes), "--num_iters", str(num_iters), "--abs_res_tol", str(abs_res_tol)]+extra_args).decode().strip().splitlines()

def abs_res(output):
    abs_res = []
    for l in output:
        m = regex_abs_res.search(l)
        if m:
            abs_res.append(float(m.groupdict()["abs_res"]))
    return abs_res

output = call("heat1d_mlsdc", ["--dt", "0.05", "--ndofs", "16"])
ar_16 = abs_res(output)
output = call("heat1d_mlsdc", ["--dt", "0.05", "--ndofs", "64"])
ar_64 = abs_res(output)
output = call("heat1d_mlsdc", ["--dt", "0.05", "--ndofs", "128"])
ar_128 = abs_res(output)
output = call("heat1d_mlsdc", ["--dt", "0.05", "--ndofs", "512"])
ar_512 = abs_res(output)
plt.plot(np.arange(0, len(ar_16)), ar_16, "<", label="16 DOF")
plt.plot(np.arange(0, len(ar_64)), ar_64, ">", label="64 DOF")
plt.plot(np.arange(0, len(ar_128)), ar_128, "^", label="128 DOF")
plt.plot(np.arange(0, len(ar_512)), ar_512, "v", label="512 DOF")
plt.yscale("log")
plt.xlabel("Iteration")
plt.ylabel("abs res")
plt.legend()
plt.title(r"MLSDC@Heat1D, dt={}, Tend={}, nodes={}, max\_iter={}, tol={}$".format(dt, tend, num_nodes, num_iters, abs_res_tol))
plt.savefig("mlsdc_heat1d_ndofs.pdf")
