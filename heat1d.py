import subprocess
import re
from matplotlib import pyplot

default_args = [
    "--tend",  "0.5",
    "--ndofs", "64",
    "--num_iters", "20",
    "--abs_res_tol", "1e-10",
    "--v=0",
]

regex_iter = re.compile(r"Advancing\s+to\s+next\s+iteration\s+\-\>\s+(?P<iter>\d+)")
regex_node = re.compile(r"t\[(?P<node>\d+)\]\=(?P<time>\d+\.\d+(e(\-|\+)\d+)?)\s+\|abs\s+residual\|\s+\=\s+(?P<abs_res>\d+\.\d+(e(\-|\+)\d+)?)")

def call(exe, extra_args):
    return subprocess.check_output(["bin/"+exe]+default_args+extra_args).decode().strip().splitlines()

def parse(output):
    for l in output:
        m = regex_iter.search(l)
        if m:
            print("{}".format(m.groupdict()["iter"]))
            continue
        m = regex_node.search(l)
        if m:
            print("{}\t{}\t{}".format(m.groupdict()["node"], m.groupdict()["time"], m.groupdict()["abs_res"]))

parse(call("heat1d_sdc", ["--num_nodes", "3"]))

# print(subprocess.check_output(["bin/heat1d_sdc", "--dt", "0.01", "--num-nodes", "3"] + default_args).decode().strip())
# print(subprocess.check_output(["bin/heat1d_mlsdc", "--dt", "0.01", "--num-nodes", "3", "--coarse_factor", "1"] + default_args).decode().strip())
