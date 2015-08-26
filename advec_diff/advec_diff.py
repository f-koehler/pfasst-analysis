import hashlib
import logging
import numpy as np
import os
import os.path
import re
import subprocess
import shlex


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

    def cmd(self):
        file_name = self.parameter_hash()
        cmd = (
            "./advec_diff_{}"
            " --dt {}"
            " --tend {}"
            " --num_iters {}"
            " --num_dofs {}"
            " --coarse_factor {}"
            " --num_nodes {}"
            " --abs_res_tol {}"
            " --nu {}"
            " --vel {}"
            " --out_file {}"
            " --nocolor"
        ).format(
            self.variant,
            self.dt, self.t_end,
            self.num_iters, self.num_dofs,
            self.coarse_factor, self.num_nodes,
            self.abs_res_tol, self.nu,
            self.vel, file_name
        )
        return shlex.split(cmd)

    def run(self):
        cmd = self.cmd()

        logging.debug("Execute: "+" ".join(cmd))
        subprocess.check_output(cmd, cwd="bin")

    def callgrind(self):
        pass

    def results(self):
        file_name = "bin/"+self.parameter_hash()
        if not os.path.exists(file_name):
            raise RuntimeError("File \"{}\" does not exist!".format(file_name))
        return np.loadtxt(file_name, unpack=True)

    def results_coarse(self):
        file_name = "bin/"+self.parameter_hash()+"_coarse"
        if not os.path.exists(file_name):
            raise RuntimeError("File \"{}\" does not exist!".format(file_name))
        return np.loadtxt(file_name, unpack=True)

    def remove_files(self):
        file_name = "bin/"+self.parameter_hash()
        logging.debug("Remove: "+file_name)
        if os.path.exists(file_name):
            os.remove(file_name)

        file_name += "_coarse"
        logging.debug("Remove: "+file_name)
        if os.path.exists(file_name):
            os.remove(file_name)

        # entries = ["bin/"+e for e in os.listdir("bin") if os.path.isfile("bin/"+e)]
        # for e in entries:
        #     if re.match("^"+e+"\.\d+$", e):
        #         os.remove(e)
