#!/usr/bin/env python
#encoding:utf8
import sys
import itertools
from collections import defaultdict

tag_count_dict = defaultdict(int)
pair_count_dict = defaultdict(int)
word_set = set()
def load_count(fname):
    for line in open(fname):
        line = line.strip()
        tokens = line.split(' ')
        count = int(tokens[0])
        tags = tuple(tokens[2:])
        if tokens[1] == 'WORDTAG':
            word_set.add(tags[1])
            pair_count_dict[tags] = count
        else:
            tag_count_dict[tags] = count
    return

def efunc(x, y):
    '''
    e(x|y)
    '''
    if x not in word_set:
        if any(c.isdigit() for c in x):
            x = '_NUMERIC_'
        elif x.isupper():
            x = '_ALL_CAP_'
        elif x[-1].isupper():
            x = '_LAST_CAP_'
        else:
            x = '_RARE_'
    return pair_count_dict[(y, x)] / float(tag_count_dict[(y,)])

def qfunc(v, w, u):
    '''
    q(v|w, u)
    '''
    return tag_count_dict[w, u, v] / float(tag_count_dict[w, u])

TAG_SET = ('O', 'I-GENE')
def viterbi(word_list):
    '''
    返回tag序列。
    '''
    word_list = ['*', '*'] + word_list
    pi_dict = {(1, '*', '*'):1}
    bp_dict = {}

    for k in range(2, len(word_list)):
        u_set = TAG_SET
        v_set = TAG_SET
        w_set = TAG_SET
        if k == 2:
            u_set = ('*', )
            w_set = ('*', )
        elif k == 3:
            w_set = ('*', )
        for u, v in itertools.product(u_set, v_set):
            e = efunc(word_list[k], v)
            candi_list = [((pi_dict[k - 1, w, u] * qfunc(v, w, u) * e), w) for w in w_set]
            pi, bp = max(candi_list, key=lambda x:x[0])
            pi_dict[k, u, v] = pi
            bp_dict[k, u, v] = bp
    # 确定最末尾的两个位置上的tag。
    # print word_list
    uv_list= [(pi_dict[len(word_list) - 1, u, v] * qfunc('STOP', u, v), (u, v)) \
            for (u, v) in itertools.product(TAG_SET, TAG_SET)]
    tagn_1, tagn = max(uv_list, key=lambda x:x[0])[1]
    tag_list = [0] * len(word_list)
    #print word_list
    tag_list[-2] = tagn_1
    tag_list[-1] = tagn
    for i in reversed(range(len(tag_list) - 2)):
        tag_list[i] = bp_dict[i + 2, tag_list[i + 1], tag_list[i + 2]]
    return tag_list[2:]

if __name__ == '__main__':
    count_fname = sys.argv[1]
    input_fname = sys.argv[2]
    load_count(count_fname)
    fout = open('gene_test.p3.out', 'w')
    word_list = []
    cnt = 0
    for line in open(input_fname):
        line = line.strip()
        if not line:
            tag_list = viterbi(word_list)
            for word, tag in zip(word_list, tag_list):
                fout.write('%s %s\n' % (word, tag))
            fout.write('\n')
            word_list = []
        else:
            word_list.append(line)
    fout.close()
