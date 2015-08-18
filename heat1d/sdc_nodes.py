import re
import numpy as np
from matplotlib import pyplot as plt
import heat1d

plt.xscale("log")
plt.yscale("log")

runner = heat1d.Heat1D_SDC()
def case(nodes):
    runner.num_nodes = nodes
    residuals = runner.absolute_residuals(runner.run())
    iters     = np.arange(1, len(residuals)+1)
    plt.plot(iters, residuals, ".-", label=str(nodes)+" Nodes")

def theory(order):
    x = np.linspace(1, 18, 100)
    plt.plot(x, x**(-order), "--")

plt.title(
    r"Heat1D with SDC\\"+
    r"$\mathrm{d}t="+str(runner.dt)+
    r"$, $t_\mathrm{end}="+str(runner.t_end)+
    r"$, $\mathrm{max\_iters}="+str(runner.num_iters)+
    r"$, $\mathrm{dof}="+str(runner.num_dofs)+
    r"$, $\mathrm{tol}=\num{"+str(runner.abs_res_tol)+"}$"
)

nodes = [3,5,7]
for n in nodes:
    case(n)

# orders = [2,4,6,8]
# for o in orders:
#     theory(o)

plt.xlabel("iteration")
plt.ylabel("absolute residuals")

plt.legend()
plt.show()
plt.savefig("plot/heat1d/sdc_nodes.pdf")
