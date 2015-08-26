import numpy as np
from matplotlib import pyplot as plt
import advec_diff

plt.yscale("log")

runner = advec_diff.AdvecDiffRunner()


def case_sdc(nodes):
    runner.num_nodes = nodes
    runner.variant = "sdc"
    runner.coarse_factor = 1
    t1, r1, rr1, e1, re1, t2, r2, rr2, e2, re2 = runner.run()
    i = np.arange(0, len(e1))
    plt.plot(i, e1, ".-", label="SDC,"+str(nodes)+" Nodes")


def case_mlsdc(nodes):
    runner.num_nodes = nodes
    runner.variant = "mlsdc"
    runner.coarse_factor = 2
    t1, r1, rr1, e1, re1, t2, r2, rr2, e2, re2 = runner.run()
    i = np.arange(0, len(e1))
    plt.plot(i, e1, ".-", label="MLSDC,"+str(nodes)+" Nodes")


def theory(order):
    b = np.log(0.4)
    x = np.linspace(0, 18, 100)
    y = np.exp(-order*x+b)
    plt.plot(x, y, "--", label=r"$e^{-"+str(order)+"\cdot i+b}$")


plt.title(r"AdvecDiff, " +
          r"$\mathrm{d}t=" + str(runner.dt) +
          r"$, $t_{\mathrm{end}}=" + str(runner.t_end) +
          r"$, $\mathrm{max\_iter}=" + str(runner.num_iters) +
          r"$, $\mathrm{dof}=" + str(runner.num_dofs) +
          r"$, $\mathrm{tol}=\num{" + str(runner.abs_res_tol) +
          r"}$")

case_sdc(3)
case_sdc(5)
case_mlsdc(3)
case_mlsdc(5)
# theory(1)
# theory(2)
# theory(3)

plt.xlabel("iteration $i$")
plt.ylabel("absolute errors")

plt.legend()
plt.savefig("plot/advec_diff/nodes.pdf")
