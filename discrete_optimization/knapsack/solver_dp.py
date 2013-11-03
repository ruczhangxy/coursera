#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
'''
Solve the knapsack problem by dynamic programming.
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

    # dynamic programming approach.
    dp_matrix = compute_dp_matrix(capacity, values, weights)
    value = dp_matrix[items][capacity]
    taken = trace_back(dp_matrix, weights)

    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(1) + '\n'
    outputData += ' '.join(map(str, taken))
    return outputData

def compute_dp_matrix(capacity, values, weights):
    matrix = [[0] * (capacity + 1)]
    for i in range(1, len(values) + 1):
        vector = [0] * (capacity + 1)
        value = values[i - 1]
        weight = weights[i - 1]
        for cap in range(capacity + 1):
            if weight > cap:
                    vector[cap] = matrix[i - 1][cap]
            else:
                vector[cap] = max(value + matrix[i - 1][cap - weight],
                                matrix[i - 1][cap])
        matrix.append(vector)
    return matrix

def trace_back(dp_matrix, weights):
    capacity = len(dp_matrix[0]) - 1
    taken = [0] * len(dp_matrix)
    for n_item in range(len(dp_matrix) - 1, 0, -1):
        if dp_matrix[n_item][capacity] == dp_matrix[n_item - 1][capacity]:
            taken[n_item] = 0
        else:
            taken[n_item] = 1
            capacity -= weights[n_item - 1]

    return taken[1:]

import sys

if __name__ == '__main__':
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

