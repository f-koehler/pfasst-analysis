import numpy as np
from matplotlib import pyplot as plt
import advec_diff

plt.yscale("log")

runner = advec_diff.AdvecDiffRunner()


def case_sdc():
    runner.variant = "sdc"
    runner.coarse_factor = 1
    runner.run()
    t, r, rr, e, re = runner.results()
    i = np.arange(0, len(r))
    plt.plot(i, r, "^-", label="SDC")
    runner.remove_files()


def case_mlsdc(coarse_factor):
    runner.variant = "mlsdc"
    runner.coarse_factor = coarse_factor
    runner.run()
    t, r, rr, e, re = runner.results()
    i = np.arange(0, len(r))
    plt.plot(i, r, "v-", label="MLSDC, coarse_factor={}".format(coarse_factor))
    runner.remove_files()


def case_mlsdc2(coarse_factor):
    runner.variant = "mlsdc"
    runner.coarse_factor = coarse_factor
    runner.run()
    t, r, rr, e, re = runner.results()
    i = np.arange(0, len(r))
    plt.plot(i, r, "^-", label="MLSDC, coarse_factor={}".format(coarse_factor))
    runner.remove_files()


case_sdc()
case_mlsdc(1)
case_mlsdc2(2)

plt.title(
    (
        "AdvecDiff, dt={}, t_end={}, max_iter={}, dof={},\n"
        "nu={}, vel={}, abs_res_tol={}, {} Nodes\n"
    ).format(
        runner.dt, runner.t_end, runner.num_iters, runner.num_dofs,
        runner.nu, runner.vel, runner.abs_res_tol, runner.num_nodes
    )
)

plt.xlabel("iteration")
plt.ylabel("absolute residuals")

plt.legend()
plt.savefig("plot/advec_diff/coarse_factor.pdf")
