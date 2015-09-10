import jinja2
import math
import os
import os.path

env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
template = env.get_template("job.template")

def create_job(nodes, tasks, tend):
    name = "{}_{}_{}".format(nodes, tasks, tend)
    if not os.path.exists(name):
        os.mkdir(name)
    var = dict()
    var["nodes"] = nodes
    var["tasks"] = tasks
    var["tasks_per_node"] = int(math.ceil(tasks/nodes))
    var["tend"] = tend
    with open(os.path.join(name, "run.job"), "w") as f:
        f.write(template.render(var))

create_job(1, 24, 0.96)
create_job(1, 48, 0.96)
create_job(2, 48, 0.96)
create_job(2, 96, 0.96)
create_job(4, 96, 0.96)
# create_job(1, 24, 2.56)
# create_job(1, 48, 2.56)
# create_job(2, 48, 2.56)
# create_job(2, 96, 2.56)
# create_job(4, 96, 2.56)
