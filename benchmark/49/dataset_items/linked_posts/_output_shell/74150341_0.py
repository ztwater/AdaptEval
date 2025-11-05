import shlex
from subprocess import PIPE
from subprocess import Popen
def run(cmd, input=None):
    """Runs the given command locally and returns the output, err and exit_code."""
    if "|" in cmd:        
        cmd_parts = cmd.split('|')
    else:
        cmd_parts = []
        cmd_parts.append(cmd)
    i = 0
    p = {}
    for cmd_part in cmd_parts:
        cmd_part = cmd_part.strip()
        if i == 0:
            if input:
                p[i]=Popen(shlex.split(cmd_part),stdin=PIPE, stdout=PIPE, stderr=PIPE)
            else:
                p[i]=Popen(shlex.split(cmd_part),stdin=None, stdout=PIPE, stderr=PIPE)
        else:
            p[i]=Popen(shlex.split(cmd_part),stdin=p[i-1].stdout, stdout=PIPE, stderr=PIPE)
        i = i +1
    # close the stdin explicitly, otherwise, the following case will hang.
    if input:
        p[0].stdin.write(input)
        p[0].stdin.close()
    (output, err) = p[i-1].communicate()
    exit_code = p[0].wait()
    return str(output), str(err), exit_code

# test case below
inp = b'[  CMServer State   ]\n\nnode        node_ip         instance state\n--------------------------------------------\n1  linux172 10.90.56.172    1        Primary\n2  linux173 10.90.56.173    2        Standby\n3  linux174 10.90.56.174    3        Standby\n\n[    ETCD State     ]\n\nnode        node_ip         instance state\n--------------------------------------------------\n1  linux172 10.90.56.172    7001     StateFollower\n2  linux173 10.90.56.173    7002     StateLeader\n3  linux174 10.90.56.174    7003     StateFollower\n\n[   Cluster State   ]\n\ncluster_state   : Normal\nredistributing  : No\nbalanced        : No\ncurrent_az      : AZ_ALL\n\n[  Datanode State   ]\n\nnode        node_ip         instance state            | node        node_ip         instance state            | node        node_ip         instance state\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n1  linux172 10.90.56.172    6001     P Standby Normal | 2  linux173 10.90.56.173    6002     S Primary Normal | 3  linux174 10.90.56.174    6003     S Standby Normal'
cmd = "grep -E 'Primary' | tail -1 | awk '{print $3}'"

run(cmd, input=inp)
