from functools import reduce
from itertools import product
voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    ret_dict = {}
    for line in voting_data:
        tokens = line.strip().split(' ')
        names = tokens[:3]
        votes = tokens[3:]
        last_name = names[0]
        ret_dict[last_name] = list(map(int, votes))
    return ret_dict
    

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    votes_a = voting_dict[sen_a]
    votes_b = voting_dict[sen_b]
    simi = sum([a * b for a, b in zip(votes_a, votes_b)])
    return simi


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    
    return max([(other, policy_compare(sen, other, voting_dict)) for other in voting_dict.keys() if other != sen], key=lambda x:x[1])[0]
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    return min([(other, policy_compare(sen, other, voting_dict)) for other in voting_dict.keys()], key=lambda x:x[1])[0]
    
    

## Task 5

voting_dict = create_voting_dict()
most_like_chafee    = most_similar('Chafee', voting_dict)
least_like_santorum = least_similar('Santorum', voting_dict)



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    simi_list = [policy_compare(sen, other, voting_dict) for other in sen_set]
    return sum(simi_list) / len(simi_list)

party_sen_pairs = [line.strip().split()[:2] for line in voting_data]
democrat_sens = set([tokens[0] for tokens in party_sen_pairs if tokens[1] == 'D'])
all_sens = set([tokens[0] for tokens in party_sen_pairs])
most_average_Democrat = max([(name, find_average_similarity(name, democrat_sens, voting_dict)) for name in all_sens], key=lambda x:x[1])[0]


# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    votings_list = [voting_dict[sen] for sen in sen_set]
    total_votings = reduce(lambda a,b:[x+y for x, y in zip(a, b)],votings_list)
    size = len(votings_list)
    avg_votings = [x / size for x in total_votings]
    return avg_votings

average_Democrat_record = find_average_record(democrat_sens, voting_dict)


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    min_simi = 10000
    min_pair = None
    for sen_a, sen_b in product(voting_dict.keys(), voting_dict.keys()):
        simi = policy_compare(sen_a, sen_b, voting_dict)
        if simi < min_simi:
            min_simi = simi
            min_pair = (sen_a, sen_b)
    return min_pair

