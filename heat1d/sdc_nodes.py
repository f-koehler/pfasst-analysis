import re
import numpy as np
from matplotlib import pyplot as plt
import heat1d

plt.yscale("log")

runner = heat1d.Heat1dRunner()
def case(nodes):
    runner.num_nodes = nodes
    residuals = runner.absolute_residuals(runner.run())
    iters     = np.arange(1, len(residuals)+1)
    plt.plot(iters, residuals, ".-", label=str(nodes)+" Nodes")

plt.title(
    r"Heat1D with SDC\\"+
    r"$\mathrm{d}t="+str(runner.dt)+
    r"$, $t_\mathrm{end}="+str(runner.t_end)+
    r"$, $\mathrm{max\_iters}="+str(runner.num_iters)+
    r"$, $\mathrm{dof}="+str(runner.num_dofs)+
    r"$, $\mathrm{tol}=\num{"+str(runner.abs_res_tol)+"}$"
)

case(3)
case(4)
case(5)
case(6)
case(7)
case(8)
case(9)
case(10)

plt.xlabel("iteration")
plt.ylabel("absolute residuals")

plt.legend()
plt.savefig("plot/heat1d/sdc_nodes.pdf")
