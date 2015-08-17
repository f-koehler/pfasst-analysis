import re
import subprocess

regex_abs_res = re.compile(r"t\[3\]\=\d+\.\d+(e(\-|\+)\d+)?\s+\|abs\s+residual\|\s+\=\s+(?P<abs_res>\d+\.\d+(e(\-|\+)\d+)?)")

class Heat1D_SDC:
    dt            = 0.5
    t_end         = 0.5
    num_iters     = 20
    num_dofs      = 64
    coarse_factor = 1
    num_nodes     = 3
    abs_res_tol   = 1e-10
    variant       = "sdc"

    def run(self):
        cmd = [
            "--dt", str(self.dt),
            "--tend", str(self.t_end),
            "--num_iters", str(self.num_iters),
            "--num_dofs", str(self.num_dofs),
            "--coarse_factor", str(self.coarse_factor),
            "--num_nodes", str(self.num_nodes),
            "--abs_res_tol", str(self.abs_res_tol),
            "--nocolor",
        ]
        cmd = ["bin/heat1d_"+self.variant]+cmd
        output = subprocess.check_output(cmd).decode().strip().splitlines()
        return output

    def absolute_residuals(self, output):
        abs_res  = []
        for l in output:
            m = regex_abs_res.search(l)
            if m:
                abs_res.append(float(m.groupdict()["abs_res"]))
        return abs_res

class Heat1D_MLSDC:
    dt            = 0.5
    t_end         = 0.5
    num_iters     = 20
    num_dofs      = 64
    coarse_factor = 1
    num_nodes     = 3
    abs_res_tol   = 1e-10
    variant       = "mlsdc"

    def run(self):
        cmd = [
            "--dt", str(self.dt),
            "--tend", str(self.t_end),
            "--num_iters", str(self.num_iters),
            "--num_dofs", str(self.num_dofs),
            "--coarse_factor", str(self.coarse_factor),
            "--num_nodes", str(self.num_nodes),
            "--abs_res_tol", str(self.abs_res_tol),
            "--nocolor",
        ]
        cmd = ["bin/heat1d_"+self.variant]+cmd
        output = subprocess.check_output(cmd).decode().strip().splitlines()
        return output
    
    def absolute_residuals(self, output):
        abs_res_coarse = []
        abs_res_fine   = []

        for l in output:
            m = regex_abs_res.search(l)
            if m:
                if l.find("LVL_COARSE") >= 0:
                    abs_res_coarse.append(float(m.groupdict()["abs_res"]))
                else:
                    abs_res_fine.append(float(m.groupdict()["abs_res"]))
        return (abs_res_coarse, abs_res_fine)
