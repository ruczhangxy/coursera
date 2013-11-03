#!/usr/bin/env python
#encoding:utf8
import sys
from collections import defaultdict

def transform_word(word):
    '''
    将低频词转为四种形式之一。
    '''
    if any(c.isdigit() for c in word):
        return '_NUMERIC_'
    if word.isupper():
        return '_ALL_CAP_'
    if word[-1].isupper():
        return '_LAST_CAP_'
    return '_RARE_'
def sub_rare(fname, out_name):
    count_dict = defaultdict(int)
    # 先统计词频。
    with open(fname) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            word = line.partition(' ')[0]
            count_dict[word] += 1
    # 然后替换低频词。
    fout = open(out_name, 'w')
    with open(fname) as f:
        for line in f:
            line = line.strip()
            if not line:
                fout.write('\n')
                continue
            word, sep, tag = line.partition(' ')
            if count_dict[word] < 5:
                # word = '_RARE_'
                word = transform_word(word)
            fout.write('%s %s\n' % (word, tag))
    fout.close()
    return

if __name__ == '__main__':
    fname = sys.argv[1]
    sub_rare(fname, fname + '.sub_rare')
