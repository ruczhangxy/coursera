#!/usr/bin/env python
#encoding=utf8

import sys
from random import expovariate

def simulate():
    distance = 400.0
    v = 4.0
    miu = 1/25.5622
    time_needed = distance / v
    shot = 0

    while shot < 4:
        time_to_shot = expovariate(miu)
        if time_to_shot > time_needed:
            return True
        shot += 1
        passed = time_to_shot * v
        distance -= passed
        # Halve the velocity.
        v /= 2
        # Compute new time needed.
        time_needed = distance / v

    return False

def main():
    trial_num = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    ok = sum([simulate() for i in range(trial_num)])
    prob = ok * 1.0 / trial_num
    print 'Prob of succeed:', prob
    return

if __name__ == '__main__':
    main()
