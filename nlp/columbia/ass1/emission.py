#!/usr/bin/env python
#encoding:utf8
import sys
from collections import defaultdict

tag_count_dict = {'O':345128, 'I-GENE':41072}
pair_count_dict = defaultdict(int)
word_set = set()

def load_count(fname):
    for line in open(fname):
        line = line.strip()
        tokens = line.split(' ')
        if tokens[1] != 'WORDTAG':
            continue
        count = int(tokens[0])
        tag = tokens[2]
        word = tokens[3]
        pair_count_dict[(word, tag)] = count
        word_set.add(word)
    return

def emission(x, y):
    if x not in word_set:
        x = '_RARE_'
    return pair_count_dict[(x, y)] / float(tag_count_dict[y])

def max_emission(x):
    e_list = [(y, emission(x, y)) for y in tag_count_dict]
    return max(e_list, key=lambda x:x[1])[0]

if __name__ == '__main__':
    load_count(sys.argv[1])
    fname = sys.argv[2]
    fout = open('gene_test.p1.out', 'w')
    for line in open(fname):
        line = line.strip()
        if not line:
            fout.write('\n')
            continue
        fout.write('%s %s\n' % (line, max_emission(line)))

    fout.close()
