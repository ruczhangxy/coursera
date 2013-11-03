#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
'''
Solve the knapsack prblem by branch and bouding.
When searching the best solution, use Depth-First search.
'''

def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    values = []
    weights = []

    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    items = len(values)
    zipped = list(enumerate(zip(values, weights)))
    # Sort items to accelerate computation of optimal estimate and heuristic search.
    zipped.sort(key=lambda x:(x[1][0] * 1.0/x[1][1], x[1][1]), reverse=True)
    index_list, pair_list = zip(*zipped)
    values, weights = zip(*pair_list)

    # branch and bound approach.
    value, taken = iterative_branch_bound(values, weights, capacity)
    if len(taken) < len(weights):
        taken += [0] * (len(weights) - len(taken))
    sorted_taken = [0] * items
    for i, n in enumerate(index_list):
        sorted_taken[n] = taken[i]
    taken = sorted_taken

    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(1) + '\n'
    outputData += ' '.join(map(str, taken))
    return outputData

def estimate_optimal_value(values, weights, index, capacity_left):
    '''
    假设可以取某个东西的一部分，计算最大可能取到的value。
    '''
    return capacity_left * values[index] * 1.0 / weights[index]

def recursive_branch_bound(values, weights, taken, \
        current_value, current_weight, capacity_left, best_value):
    if len(taken) == len(values):
        return current_value, taken
    next_index = len(taken)
    next_value = values[next_index]
    next_weight = weights[next_index]

    if min(weights[next_index:]) > capacity_left or \
            current_value + estimate_optimal_value(values, weights, \
            next_index, capacity_left) <= best_value:
        # Prune this branch.
        return current_value, taken

    value1, taken1 = recursive_branch_bound(values, weights, taken + [0], \
            current_value, current_weight, capacity_left, best_value)
    if value1 > best_value:
        best_value = value1

    if next_weight > capacity_left:
        return value1, taken1
    else:
        value2 , taken2 = recursive_branch_bound(values, weights, taken + [1], \
                current_value + next_value, current_weight + next_weight, \
                capacity_left - next_weight, best_value)
        if value2 > value1:
            return value2, taken2
        else:
            return value1, taken1

def iterative_branch_bound(values, weights, capacity):
    best_value = 0
    best_taken = []
    item_count = len(values)
    # Status tuple:(current_value, capacity_left, taken)
    stack = [(0, capacity, [])] 
    estimate_cache = {}
    while stack:
        current_value, capacity_left, taken = stack.pop()
        #print current_value, capacity_left, taken
        if len(taken) == item_count:
            continue
        if current_value > best_value:
            best_value = current_value
            best_taken = taken
        next_index = len(taken)
        next_value = values[next_index]
        next_weight = weights[next_index]

        optimal = estimate_cache.get((next_index, capacity_left), -1)
        if optimal == -1:
            optimal = estimate_optimal_value(values, weights, \
                next_index, capacity_left)
            estimate_cache[(next_index, capacity_left)] = optimal
        if current_value + optimal <= best_value:
            # Prune this branch.
            continue

        new_node = (current_value, capacity_left, taken + [0])
        stack.append(new_node)

        if next_weight <= capacity_left:
            new_node = (current_value + next_value, capacity_left - next_weight, taken + [1])
            stack.append(new_node)

    return best_value, best_taken

import sys
import cProfile
import pstats

def main():
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        t1 = time.time()
        print solveIt(inputData)
        t2 = time.time()
        #print 'Time', t2 - t1
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

if __name__ == '__main__':
    main()
    '''
    fname = 'bb_df.profile'
    cProfile.run('main()', fname)
    stats = pstats.Stats(fname)
    stats.sort_stats('time')
    stats.print_stats(20)
    '''
