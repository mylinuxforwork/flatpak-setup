import json
import os
import pathlib

home_folder = os.path.expanduser('~') + "/"
project_folder = home_folder + "Projects/"
json_arr = json.load(open("apps.json"))

with open("template.sh", 'r') as file:
    tpl = file.read()

for app in json_arr:
    f = tpl.replace("[RUNTIME]", app["runtime"])
    f = f.replace("[APP]", app["app"])
    f = f.replace("[PROJECT]", app["project"])
    print("Writing -> " +  project_folder + app["project"] + "/setup.sh")
    with open(project_folder + app["project"] + "/setup.sh", "w") as setup_file:
        setup_file.write(f)

print("DONE")