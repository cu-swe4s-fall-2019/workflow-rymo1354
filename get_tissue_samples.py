import sys
import os
import argparse
import time


def parse_args():
    parser = argparse.ArgumentParser(
        description='The right way to pass parameters.',
        prog='get_tissue_samples.py')

    parser.add_argument('-of', '--output_file',
                        type=str,
                        help='Name of the output plot',
                        required=True)
    parser.add_argument('-gt', '--group_type',
                        type=str,
                        help='The group type, such as SMTS',
                        required=True)
    parser.add_argument('-sa', '--sample_attributes',
                        type=str,
                        help='A txt file with sample attribs',
                        required=True)

    return parser.parse_args()


def linear_search(key, L):
    """
    Linear search for first index in list equivalent to key
    Arguments
    ________
    key: datatype being searched for
    L: list being searched
    Returns
    _______
    i: if key is in the list
    -1: if key is not in the list
    """
    for i in range(len(L)):
        if key == L[i]:
            return i
    return -1


def parse_meta(group, file):
    """
    Splits meta data into the gene and target groups
    Arguments
    ________
    group: (str) the group type, like SMTS
    file: (str) name of the file to read data from
    Returns
    ________
    dic: (dict) a meta data map of the group type
    target_group: (list) the target group
    """

    metadata_header = None
    target_group = []
    dic = {}
    f = open(file)
    for l in f:
        sample_info = l.rstrip().split('\t')

        if metadata_header is None:
            metadata_header = sample_info
            continue

        sample_idx = linear_search('SAMPID', metadata_header)
        target_idx = linear_search(group, metadata_header)

        if target_idx == -1:
            return None, target_group

        key = sample_info[target_idx]
        value = sample_info[sample_idx]
        search = None

        if key in dic.keys():
            search = dic[key]

        if search is None:
            dic[key] = [value]
            target_group.append(key)
        else:
            search.append(value)

    f.close()

    return dic, target_group


def main():
    args = parse_args()
    if not os.path.exists(args.sample_attributes):
        print('Cannot find meta file')
        sys.exit(1)

    meta_map, target_group = parse_meta(args.group_type,
                                        args.sample_attributes)
    target_group.sort()

    if meta_map is None:
        print('Cannot find group_type')
        sys.exit(1)
    else:
        output = open(args.output_file, 'w')
        for i in range(len(target_group)):
            output.write(target_group[i] + ': ')
            for j in range(len(meta_map[target_group[i]])):
                output.write(meta_map[target_group[i]][j])
                if j != len(meta_map[target_group[i]]) - 1:
                    output.write(' ')
            if i != len(target_group) - 1:
                output.write('\n')
        output.close()

    sys.exit(0)


if __name__ == '__main__':
    main()
