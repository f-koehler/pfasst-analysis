import advec_diff

runner = advec_diff.AdvecDiffRunner()
runner.tend = 5.

def case_sdc(dt):
    runner.dt = dt
    runner.coarse_factor = 1
    runner.variant = "sdc"
    result = runner.run_callgrind()
    with open("profiles/advec_diff/sdc_{}.callgrind".format(dt), "w") as f:
        f.write(result.raw)
    runner.remove_files()

def case_mlsdc(dt):
    runner.dt = dt
    runner.coarse_factor = 1
    runner.variant = "mlsdc"
    result = runner.run_callgrind()
    with open("profiles/advec_diff/mlsdc_{}.callgrind".format(dt), "w") as f:
        f.write(result.raw)
    runner.remove_files()

case_sdc(0.001)
case_sdc(0.01)
case_mlsdc(0.001)
case_mlsdc(0.01)
