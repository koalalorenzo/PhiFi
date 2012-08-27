#!/usr/bin/python
# -*- coding=utf-8 -*-

import sys
from phifi.manager import Manager
    
if "--version" in sys.argv or "-v" in sys.argv:
    print phifi.__version__
    sys.exit(0)

if  len(sys.argv) == 0 or "--help" in sys.argv or "-h" in sys.argv:
        print help
        sys.exit(0)

def get_targhet(manager):
    sys.stdout.write("Targhets availables:\n")
    answers = list()
    for targhet in manager.targets:
        answers.append(targhet)
        sys.stdout.write("  %s => %s\n" % (len(answers), targhet))
    return answers[int(raw_input("Insert the targhet number: "))]

manager = Manager()
sys.stdout.write("Downloading databases: ")
manager.get_databases()
sys.stdout.write("done\n")

while 1:
    try:
        targhet = get_targhet(manager)
        break
    except:
        sys.stdout.write("Do not do it again\n")

while 1:
    print manager.nuke_one_time_random_by_target(targhet)


