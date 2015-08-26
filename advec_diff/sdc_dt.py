import numpy as np
from matplotlib import pyplot as plt
import heat1d

runner = heat1d.Heat1DRunner()
runner.t_end = 0.5

def case(dt):
    runner.dt = dt
    t1, r1, rr1, e1, re1, t2, r2, rr2, e2, re2 = runner.run()
    uniq, inv = np.unique(t1, return_inverse=True)
    plt.plot(uniq, np.bincount(inv), ".-", label="dt="+str(dt))

plt.title(r"SDC@Heat1D, "
        +r"$t_{\mathrm{end}}="+str(runner.t_end)
        +r"$, $\mathrm{max\_iter}="+str(runner.num_iters)
        +r"$, $\mathrm{dof}="+str(runner.num_dofs)
        +r"$, $\mathrm{tol}=\num{"+str(runner.abs_res_tol)
        +r"}$, $"+str(runner.num_nodes)
        +r"$ Nodes"
)

plt.xlabel("needed iterations")
plt.ylabel("res")
plt.ylim(0, 8)

case(0.001)
case(0.005)
case(0.01)
case(0.025)

plt.legend()
plt.savefig("plot/heat1d/sdc_dt.pdf")
