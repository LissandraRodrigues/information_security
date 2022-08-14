import os
import time

with open('hosts.txt') as file:
    content = file.read()
    hosts = content.split('\n')

    for host in hosts:
        print("\n")
        print("-" * 60)
        os.system('ping -n 3 {}'.format(host))
        time.sleep(5)



