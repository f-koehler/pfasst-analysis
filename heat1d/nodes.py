import numpy as np
from matplotlib import pyplot as plt
import heat1d

plt.yscale("log")

runner = heat1d.Heat1DRunner()

def case_sdc(nodes):
    runner.num_nodes = nodes
    runner.variant   = "sdc"
    runner.coarse_factor = 1
    t, r, _, _ = runner.run()
    i = np.arange(0, len(r))
    plt.plot(i, r, ".-", label="SDC,"+str(nodes)+" Nodes")

def case_mlsdc(nodes):
    runner.num_nodes = nodes
    runner.variant   = "mlsdc"
    runner.coarse_factor = 2
    t1, r1, t2, r2 = runner.run()
    i = np.arange(0, len(r1))
    plt.plot(i, r1, ".-", label="MLSDC,"+str(nodes)+" Nodes")

plt.title(r"Heat1D,"
        +r"$\mathrm{d}t="+str(runner.dt)
        +r"$, $t_{\mathrm{end}}="+str(runner.t_end)
        +r"$, $\mathrm{max\_iter}="+str(runner.num_iters)
        +r"$, $\mathrm{dof}="+str(runner.num_dofs)
        +r"$, $\mathrm{tol}=\num{"+str(runner.abs_res_tol)
        +r"}$"
)

case_sdc(3)
case_sdc(5)
case_mlsdc(3)
case_mlsdc(5)

plt.xlabel("iteration")
plt.ylabel("absolute residuals")

plt.legend()
plt.savefig("plot/heat1d/nodes.pdf")
