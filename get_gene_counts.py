import gzip
import sys
import os
import argparse


def parse_args():

    parser = argparse.ArgumentParser(description='The right way to \
                                     pass parameters.',
                                     prog='get_gene_counts.py')

    parser.add_argument('-of', '--output_file',
                        type=str,
                        help='Output file name',
                        required=True)
    parser.add_argument('-gn', '--gene',
                        type=str,
                        help='Target gene, such as ACTA2',
                        required=True)
    parser.add_argument('-gc', '--gene_counts_file',
                        type=str,
                        help='Database of genes',
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


def parse_gene_counts(target_gene_name, output_file, data):
    """
    Writes the gene_counts file to the current directory
    Arguments
    ________
    target_gene_name: (str) gene to search for
    output_file: (str) name of the gene_counts output file
    data: (str) name of the file to read data from
    """

    output = open(output_file, 'w')
    version = None
    dim = None
    rna_header = None

    for l in gzip.open(data, 'rt'):

        if version is None:
            version = l
            continue

        if dim is None:
            dim = l
            continue

        if rna_header is None:
            rna_header = l.rstrip().split('\t')
            description_idx = linear_search("Description", rna_header)
            continue

        rna_counts = l.rstrip().split('\t')

        if description_idx == -1:
            print('Gene not found in header')
            sys.exit(1)

        if rna_counts[description_idx] == target_gene_name:
            for i in range(description_idx + 1, len(rna_header)):
                output.write(rna_header[i] + ': ' + rna_counts[i])
                if i != len(rna_header) - 1:
                    output.write('\n')

            output.close()


def main():
    args = parse_args()
    if (not os.path.exists(args.gene_counts_file)):
        print('Cannot find meta file')
        sys.exit(1)
    parse_gene_counts(args.gene, args.output_file, args.gene_counts_file)
    sys.exit(0)


if __name__ == '__main__':
    main()
