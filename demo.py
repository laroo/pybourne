#!/usr/bin/env python3

from pybourne.shell import ShellCommand

# cmd = './test/testrunner.py'
cmd = './test/multitest.sh'

# x = ShellCommand(cmd)
# rc = x.run()
rc = ShellCommand(cmd).run()

print('Return code:', rc)
