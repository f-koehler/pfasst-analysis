import os
import os.path
import subprocess
import hashlib
import numpy as np
import logging


logging.basicConfig(level=logging.DEBUG)


class AdvecDiffRunner:
    variant = "sdc"
    dt = 0.01
    t_end = 0.01
    num_iters = 30
    num_dofs = 64
    coarse_factor = 1
    num_nodes = 3
    abs_res_tol = 1e-10
    nu = 0.02
    vel = 1

    def parameter_hash(self):
        s = "{};{};{};{};{};{};{};{};{};{}".format(
            self.variant,
            self.dt,
            self.t_end,
            self.num_iters,
            self.num_dofs,
            self.coarse_factor,
            self.num_nodes,
            self.abs_res_tol,
            self.nu,
            self.vel
        )
        h = hashlib.sha1(s.encode())
        return h.hexdigest()

    def run(self):
        name = self.parameter_hash()

        cmd = [
            "--dt", str(self.dt),
            "--tend", str(self.t_end),
            "--num_iters", str(self.num_iters),
            "--num_dofs", str(self.num_dofs),
            "--coarse_factor", str(self.coarse_factor),
            "--num_nodes", str(self.num_nodes),
            "--abs_res_tol", str(self.abs_res_tol),
            "--nu", str(self.nu),
            "--vel", str(self.vel),
            "--out_file", name,
            "--nocolor",
        ]
        cmd = ["bin/advec_diff_"+self.variant]+cmd
        logging.debug("Execute: "+" ".join(cmd))
        subprocess.check_output(cmd)

        t, r, rr, e, re = np.loadtxt(name, unpack=True)
        os.remove(name)

        t_coarse = []
        r_coarse = []
        rr_coarse = []
        e_coarse = []
        re_coarse = []
        if os.path.exists(name+"_coarse"):
            t_coarse, r_coarse, rr_coarse, e_coarse, re_coarse = np.loadtxt(name+"_coarse", unpack=True)
            os.remove(name+"_coarse")
        return (t, r, rr, e, re, t_coarse, r_coarse, rr_coarse, e_coarse, re_coarse)
