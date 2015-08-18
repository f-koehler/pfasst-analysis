import numpy as np
from matplotlib import pyplot as plt
import heat1d

runner_sdc   = heat1d.Heat1D_SDC()
runner_mlsdc = heat1d.Heat1D_MLSDC()

plt.yscale("log")

def case_mlsdc(coarse_factor):
    runner_mlsdc.coarse_factor = coarse_factor
    coarse, fine = runner_mlsdc.absolute_residuals(runner_mlsdc.run())
    line1 = plt.plot(np.arange(0, len(coarse)), coarse, ".-", label="MLSDC (coarse), coarse factor=$"+str(coarse_factor)+"$")[0]
    plt.plot(np.arange(0, len(fine)), fine, "x-", label="MLSDC (fine), coarse factor=$"+str(coarse_factor)+"$", color=line1.get_color())

res = runner_sdc.absolute_residuals(runner_sdc.run())
plt.plot(np.arange(0, len(res)), res, "v-", label="SDC")

case_mlsdc(1)
case_mlsdc(2)

plt.xlabel("iteration")
plt.ylabel("absolute residuals")

plt.legend()

plt.savefig("plot/heat1d/mlsdc_coarse_factor.pdf")
