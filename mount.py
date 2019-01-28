#!/usr/bin/python3
import subprocess
def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print (proc_stdout)
print('Starting mount shortcut app')
subprocess_cmd('sudo fdisk -l')
print('Which device should I mount (example: /dev/sdb1)')
myMount = input()
subprocess_cmd('sudo mount ' + myMount + ' /mnt/')
print('Sucessfully mounted')
