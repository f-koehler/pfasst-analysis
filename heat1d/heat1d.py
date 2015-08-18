import re
import os
import os.path
import subprocess
import hashlib
import numpy as np

regex_abs_res = re.compile(r"t\[3\]\=\d+\.\d+(e(\-|\+)\d+)?\s+\|abs\s+residual\|\s+\=\s+(?P<abs_res>\d+\.\d+(e(\-|\+)\d+)?)")
regex_next = re.compile(r"Advancing 1 time step with dt=\d+\.\d+(e(\-|\+)\d+)? to t=(?P<t>\d+\.\d+(e(\-|\+)\d+)?)")

class Heat1DRunner:
    variant       = "sdc"
    dt            = 0.5
    t_end         = 0.5
    num_iters     = 20
    num_dofs      = 64
    coarse_factor = 1
    num_nodes     = 3
    abs_res_tol   = 1e-10

    def parameter_hash(self):
        s = "{};{};{};{};{};{};{};{}".format(
            self.variant,
            self.dt,
            self.t_end,
            self.num_iters,
            self.num_dofs,
            self.coarse_factor,
            self.num_nodes,
            self.abs_res_tol
        )
        data = (None, None, None, None)
        h = hashlib.sha1(s.encode())
        return h.hexdigest()

    def run(self):
        name = self.parameter_hash()
        name_coarse = name+"_coarse"
        
        cmd = [
            "--dt", str(self.dt),
            "--tend", str(self.t_end),
            "--num_iters", str(self.num_iters),
            "--num_dofs", str(self.num_dofs),
            "--coarse_factor", str(self.coarse_factor),
            "--num_nodes", str(self.num_nodes),
            "--abs_res_tol", str(self.abs_res_tol),
            "--out_file", name,
            "--nocolor",
        ]
        cmd = ["bin/heat1d_"+self.variant]+cmd
        subprocess.check_output(cmd)

        t, r = np.loadtxt(name, unpack=True)
        os.remove(name)
        
        t_coarse = []
        r_coarse = []
        if os.path.exists(name+"_coarse"):
            t, r = np.loadtxt(name+"_coarse", unpack=True)
            os.remove(name+"_coarse")
        return (t, r, t_coarse, r_coarse) 
