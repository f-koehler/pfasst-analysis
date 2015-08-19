import numpy as np
from matplotlib import pyplot as plt
import heat1d

plt.yscale("log")

runner = heat1d.Heat1DRunner()

def case_sdc():
    runner.variant   = "sdc"
    runner.coarse_factor = 1
    t, r, _, _ = runner.run()
    i = np.arange(0, len(r))
    plt.plot(i, r, ".-", label="SDC")

def case_mlsdc(coarse_factor):
    runner.variant   = "mlsdc"
    runner.coarse_factor = coarse_factor
    t1, r1, t2, r2 = runner.run()
    i = np.arange(0, len(r1))
    plt.plot(i, r1, ".-", label="MLSDC, $\mathrm{coarse\_factor}="+str(coarse_factor)+"$")
    i = np.arange(0, len(r2))
    plt.plot(i, r2, ".-", label="MLSDC (Coarse), $\mathrm{coarse\_factor}="+str(coarse_factor)+"$")

case_sdc()
case_mlsdc(1)
case_mlsdc(2)

plt.title(r"Heat1D,"
        +r"$\mathrm{d}t="+str(runner.dt)
        +r"$, $t_{\mathrm{end}}="+str(runner.t_end)
        +r"$, $\mathrm{max\_iter}="+str(runner.num_iters)
        +r"$, $\mathrm{dof}="+str(runner.num_dofs)
        +r"$, $\mathrm{tol}=\num{"+str(runner.abs_res_tol)
        +r"}$, $"+str(runner.num_nodes)
        +r"$ Nodes"
)

plt.xlabel("iteration")
plt.ylabel("absolute residuals")

plt.legend()
plt.savefig("plot/heat1d/coarse_factor.pdf")
