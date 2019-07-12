workflow "run and plot pgbench performance" {
  resolves = "generate figures"
  on = "push"
}

action "install dependencies" {
  uses = "jefftriplett/python-actions@master"
  args = "pip install -r ./popper_demo/requirements.txt"
}

action "generate data" {
    needs = "install dependencies"
    uses = "jefftriplett/python-actions@master"
    args = "python ./popper_demo/scripts/generate_data.py"
}
action "generate figures" {
    needs = "generate data"
    uses = "jefftriplett/python-actions@master"
    args = "python ./popper_demo/scripts/generate_figures.py"
}
