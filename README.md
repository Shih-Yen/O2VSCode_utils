# Scripts for automated VSCode-to-O2 connection

These scripts will allow you to connect to O2 with VSCode using a single command.

Essentially, it will request an O2 computing session, fetch the assigned node name, paste the hostname into VSCode configuration file, and open the VSCode window connecting to that node.

## Steps to set up the script:
### 1. Set up key-based authentication for O2
Follow the instructions here: https://harvardmed.atlassian.net/wiki/spaces/O2/pages/2051211265/VSCode+and+Code+Server+on+O2#SSH-Keys
### 2. Set up shell command for VSCode
Follow the instructions here: https://www.geeksforgeeks.org/how-to-open-vs-code-using-terminal/
### 3. Add VS-Code ssh configuration
Add the following config template to the `~/.ssh/config`, and change `User` to your user name.

(No need to modify the `HostName`. It will be assigned by the script automatically)
```
Host O2Server
  HostName XXXXXXXXXXXXXXX
  User [your_username]
  ProxyJump o2jump
  ForwardAgent yes
  
Host o2jump
  HostName o2.hms.harvard.edu
  User [your_username]
  ForwardAgent yes
  ForwardX11 yes
  ForwardX11Trusted yes

```
### 4. Copy `start_VSCode_job.sh` to your O2 home folder
You can also adjust the requested resources depending on your need:
```
PARTITION=priority
CPU_CORES=4
MEMORY=24G
TIME_HOURS=12
```
### 5. Copy `O2VSCode.py` to your local home folder
Remember to modify the following:
* `USERNAME`: your O2 account
* `SSH_CONFIG_PATH`: the path to your VSCode ssh config file
* default value of `--dir`: The default O2 directory to connect to initially

Once set up, running `python O2VSCode.py` will automatically request a new O2 session for you and connect VSCode to the requested session

### [Optional] Add an alias command

I also added the following line to `~/.bash_profile` on my local machine:
```alias harvardO2='python ~/O2VSCode.py'```

With this alias command you can simply type `harvardO2` on the terminal to create a new connection to O2