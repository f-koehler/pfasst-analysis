import re
import numpy as np
from matplotlib import pyplot as plt
import heat1d

plt.yscale("log")

runner = heat1d.Heat1dRunner()
def case(dof):
    runner.num_dofs = dof
    residuals = runner.absolute_residuals(runner.run())
    iters     = np.arange(1, len(residuals)+1)
    plt.plot(iters, residuals, ".-", label=str(dof)+" dof")

plt.title(
    r"Heat1D with SDC\\"+
    r"$\mathrm{d}t="+str(runner.dt)+
    r"$, $t_\mathrm{end}="+str(runner.t_end)+
    r"$, $\mathrm{max\_iters}="+str(runner.num_iters)+
    r"$, $\mathrm{nodes}="+str(runner.num_nodes)+
    r"$, $\mathrm{tol}=\num{"+str(runner.abs_res_tol)+"}$"
)

case(16)
case(32)
case(64)
case(128)
case(256)
case(512)

plt.xlabel("iteration")
plt.ylabel("absolute residuals")

plt.legend()
plt.savefig("plot/heat1d/sdc_ndofs.pdf")
