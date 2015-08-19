import numpy as np
from matplotlib import pyplot as plt
import heat1d

plt.yscale("log")

runner = heat1d.Heat1DRunner()
runner.t_end = 0.5

def case(dt):
    runner.dt = dt
    t, r, _, _ = runner.run()
    last_t = t[0]
    x = [t[0]]
    y = [r[0]]

    for i in range(0, len(t)):
        if t[i] != last_t:
            last_t = t[i]
            x.append(t[i])
            y.append(r[i])
        else:
            y[-1] = r[i]

    plt.plot(x, y, ".-", label="dt="+str(dt))

plt.title(r"SDC@Heat1D, "
        +r"$t_{\mathrm{end}}="+str(runner.t_end)
        +r"$, $\mathrm{max\_iter}="+str(runner.num_iters)
        +r"$, $\mathrm{dof}="+str(runner.num_dofs)
        +r"$, $\mathrm{tol}=\num{"+str(runner.abs_res_tol)
        +r"}$, $"+str(runner.num_nodes)
        +r"$ Nodes"
)

plt.xlabel(r"$\mathrm{d}t$")
plt.ylabel("res")

case(0.001)
case(0.005)
case(0.01)
case(0.025)

plt.legend()
plt.savefig("plot/heat1d/sdc_dt.pdf")
