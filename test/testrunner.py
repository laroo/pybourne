#!/usr/bin/env python3
import sys
import time


def error(msg):
    print('[ERROR] ', file=sys.stderr, end='')
    print(msg, file=sys.stderr, flush=True)


def info(msg):
    print('[INFO ] ', file=sys.stdout, end='')
    print(msg, file=sys.stdout, flush=True)


info("booting...")
time.sleep(1)

for x in range(1, 10):
    if x % 2:
        info('running {}'.format(x))
    else:
        error('running {}'.format(x))
    time.sleep(1)

info("done!")
