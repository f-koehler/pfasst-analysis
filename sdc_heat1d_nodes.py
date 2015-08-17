import subprocess
import re
from matplotlib import pyplot as plt
import numpy as np

dt = 0.05
tend  = 0.05
ndofs = 64
num_iters = 20
abs_res_tol = 1e-10

regex_abs_res = re.compile(r"t\[3\]\=\d+\.\d+(e(\-|\+)\d+)?\s+\|abs\s+residual\|\s+\=\s+(?P<abs_res>\d+\.\d+(e(\-|\+)\d+)?)")

def call(exe, extra_args):
    return subprocess.check_output(["bin/"+exe, "--tend", str(tend), "--ndofs", str(ndofs), "--num_iters", str(num_iters), "--abs_res_tol", str(abs_res_tol)]+extra_args).decode().strip().splitlines()

def abs_res(output):
    abs_res = []
    for l in output:
        m = regex_abs_res.search(l)
        if m:
            abs_res.append(float(m.groupdict()["abs_res"]))
    return abs_res

output = call("heat1d_sdc", ["--dt", str(dt), "--num-nodes", "3"])
ar_3 = abs_res(output)
output = call("heat1d_sdc", ["--dt", str(dt), "--num-nodes", "4"])
ar_4 = abs_res(output)
output = call("heat1d_sdc", ["--dt", str(dt), "--num-nodes", "5"])
ar_5 = abs_res(output)
plt.plot(np.arange(0, len(ar_3)), ar_3, "<", label="3 Nodes")
plt.plot(np.arange(0, len(ar_4)), ar_4, ">", label="4 Nodes")
plt.plot(np.arange(0, len(ar_5)), ar_5, "^", label="5 Nodes")
plt.yscale("log")
plt.xlabel("Iteration")
plt.ylabel("abs res")
plt.legend()
plt.title(r"SDC@Heat1D, dt={}, Tend={}, dof={}, max\_iter={}, tol={}$".format(dt, tend, ndofs, num_iters, abs_res_tol))
plt.savefig("sdc_heat1d_nodes.pdf")
