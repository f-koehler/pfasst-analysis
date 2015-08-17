import numpy as np
from matplotlib import pyplot as plt
import heat1d

runner = heat1d.Heat1D_SDC()

def case(dt):
    runner.dt = dt
    t, r = runner.convergence(runner.run())
    plt.plot(t,r, ".-")

dts = [ 0.01, 0.05, 0.1 ]
for dt in dts:
    case(dt)

plt.xlabel("$t$")
plt.ylabel("absolute residuals")
plt.savefig("plot/heat1d/sdc_dt.pdf")
