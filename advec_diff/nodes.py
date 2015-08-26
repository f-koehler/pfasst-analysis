import numpy as np
from matplotlib import pyplot as plt
import advec_diff

plt.yscale("log")

runner = advec_diff.AdvecDiffRunner()


def case_sdc(nodes):
    runner.num_nodes = nodes
    runner.variant = "sdc"
    runner.coarse_factor = 1
    runner.run()
    t, r, rr, e, re = runner.results()
    i = np.arange(0, len(e))
    plt.plot(i, e, ".-", label="SDC,"+str(nodes)+" Nodes")


def case_mlsdc(nodes):
    runner.num_nodes = nodes
    runner.variant = "mlsdc"
    runner.coarse_factor = 2
    runner.run()
    t, r, rr, e, re = runner.results()
    i = np.arange(0, len(e))
    plt.plot(i, e, ".-", label="MLSDC,"+str(nodes)+" Nodes")


def theory(order):
    b = np.log(0.4)
    x = np.linspace(0, 18, 100)
    y = np.exp(-order*x+b)
    plt.plot(x, y, "--", label=r"$e^{-"+str(order)+"\cdot i+b}$")


plt.title(
    (
        "AdvecDiff, dt={}, t_end={}, max_iter={},\n"
        "dof={}, nu={}, vel={}, abs_res_tol={}\n"
    ).format(
        runner.dt, runner.t_end, runner.num_iters, runner.num_dofs,
        runner.nu, runner.vel, runner.abs_res_tol
    )
)

case_sdc(3)
case_sdc(5)
case_mlsdc(3)
case_mlsdc(5)
# theory(1)
# theory(2)
# theory(3)

plt.xlabel("iteration i")
plt.ylabel("absolute errors")

plt.legend()
plt.savefig("plot/advec_diff/nodes.pdf")
