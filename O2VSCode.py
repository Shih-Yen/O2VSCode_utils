##
# run the coam
##
import os
import sys
import subprocess
import argparse

USERNAME = "shl968"
SSH_CONFIG_PATH = "/Users/ShihYenLin/.ssh/config"


def run_command(command):
    # run the command and get the output to the terminal

    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True, check=True)
    # get the second last line of the output
    lines = result.stdout.splitlines()
    output = lines[-1]
    return output


def modify_ssh_config(address):
    # modify the /Users/ShihYenLin/.ssh/config
    # change the HostName of Host O2Server to address
    new_lines = []
    with open(SSH_CONFIG_PATH, "r") as f:
        lines = f.readlines()
    found = False
    for line in lines:
        if "Host O2Server" in line:
            new_lines.append(line)
            found = True
        elif found and "HostName" in line:
            new_lines.append(f"  HostName {address}\n")
            found = False
        else:
            new_lines.append(line)
    # replace the old lines with the new lines
    with open(SSH_CONFIG_PATH, "w") as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run a command and get the second last line of the output")
    parser.add_argument("--dir", type=str, default="/n/data2/hms/dbmi/kyu/lab/shl968",
                        help="the O2 directory to connect to")
    args = parser.parse_args()

    # get the command from the command line arguments
    O2_command = f'CLUSTER_USER={USERNAME}; ssh $CLUSTER_USER@o2.hms.harvard.edu -t "sh start_VSCode_job.sh"'
    VSCode_command = f'code --remote ssh-remote+O2Server {args.dir} -n'
    # run the command and get the output
    address = run_command(O2_command)
    # address = 'compute-a-16-1sss70'
    print("the address is: ", address)
    modify_ssh_config(address)
    # os.system("code -n")
    os.system(VSCode_command)
