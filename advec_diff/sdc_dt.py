import numpy as np
from matplotlib import pyplot as plt
import advec_diff

runner = advec_diff.AdvecDiffRunner()
runner.t_end = 5.0

def case(dt):
    runner.dt = dt
    t1, r1, rr1, e1, re1, t2, r2, rr2, e2, re2 = runner.run()
    uniq, inv = np.unique(t1, return_inverse=True)
    plt.plot(uniq, np.bincount(inv), "-", label="dt={}".format(dt))

plt.title(
    (
        "SDC@AdvecDiff, t_end={}, max_iter={}, dof={},\n"
        "nu={}, vel={}, abs_res_tol={}, {} Nodes\n"
    ).format(
        runner.t_end, runner.num_iters, runner.num_dofs,
        runner.nu, runner.vel, runner.abs_res_tol, runner.num_nodes
    )
)

plt.xlabel("t")
plt.ylabel("required iterations")
plt.ylim(0, 10)

case(0.001)
case(0.005)
case(0.01)
case(0.025)

plt.legend()
plt.savefig("plot/advec_diff/sdc_dt.pdf")
