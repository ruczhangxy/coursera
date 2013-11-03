#!/usr/bin/env python
#encoding:utf8
import sys
import json
from collections import defaultdict

def get_words(tree):
    if len(tree) == 2:
        return [tree[1]]
    return get_words(tree[1]) + get_words(tree[2])

def sub_rare_tree(tree, count_dict):
    if len(tree) == 2:
        if count_dict[tree[1]] < 5:
            tree[1] = '_RARE_'
        return
    sub_rare_tree(tree[1], count_dict)
    sub_rare_tree(tree[2], count_dict)
    return

def sub_rare_file(fname, out_name):
    count_dict = defaultdict(int)
    # 先统计词频。
    with open(fname) as f:
        for line in f:
            tree = json.loads(line.strip())
            words = get_words(tree)
            for w in words:
                count_dict[w] += 1

    fout = open(out_name, 'w')
    with open(fname) as f:
        for line in f:
            tree = json.loads(line.strip())
            # subed_tree = sub_rare_tree(tree, count_dict)
            sub_rare_tree(tree, count_dict)
            fout.write('%s\n' % json.dumps(tree))
    fout.close()

if __name__ == '__main__':
    in_name = sys.argv[1]
    sub_rare_file(in_name, in_name + '.sub_rare')
