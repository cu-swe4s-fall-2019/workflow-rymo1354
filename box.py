import sys
import os
import argparse
import matplotlib.pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser(
        description='The right way to pass parameters.',
        prog='box.py')

    parser.add_argument('-of', '--output_file',
                        type=str,
                        help='Name of the output plot',
                        required=True)

    parser.add_argument('-g', '--genes',
                        type=str,
                        help='Target genes. e.g. SDHB MEN1',
                        required=True)

    parser.add_argument('-t', '--tissues',
                        type=str,
                        help='Target tissues. e.g. Brain Heart',
                        required=True)

    parser.add_argument('-mf', '--meta_file',
                        type=str,
                        help='Meta file',
                        required=True)

    return parser.parse_args()


def boxplot(data, meta, y_label, title, out_file):
    """ Arguments:
    _________
    data: (str) data from gene counts file
    meta: (str) file from which the meta data is pulled
    y_label: (str) y-label title
    title: (str) title of the graph
    out_file: (file) output file for graph, .png format """

    plt.subplots(nrows=len(title), figsize=(12, 10))

    for i in range(len(title)):
        plt.subplot(len(title), 1, i+1)
        plt.boxplot(data[i])
        plt.title(title[i])
        plt.ylabel(y_label)
        plt.xticks(range(1, len(meta) + 1), meta)

        if i == len(title) - 1:
            plt.xlabel('Gene')

    plt.savefig(out_file)


def main():
    args = parse_args()
    if not os.path.exists(args.meta_file):
        print('Invalid meta file')
        sys.exit(1)

    sample_dict = {}
    meta_file = open(args.meta_file)
    for l in meta_file:
        sample_id = l.split(':')[0]
        sample_genes = l.split(':')[1].split()
        sample_dict[sample_id] = sample_genes
    meta_file.close()

    tissues = args.tissues.split()
    genes = args.genes.split()

    final = []
    for tissue in tissues:
        par = []
        sample_ids = sample_dict[tissue]
        for gene in genes:
            gene_dict = {}
            if not os.path.exists(gene + '_counts.txt'):
                continue
            count_file = open(gene + '_counts.txt')
            for l in count_file:
                gene_dict[l.split(':')[0]] = int(l.split(':')[1])
            count_file.close()
            count_list = []
            for sample_id in sample_ids:
                if sample_id in gene_dict.keys():
                    count_list.append(gene_dict[sample_id])
            par.append(count_list)
        final.append(par)

    boxplot(final, genes, 'Count', tissues, args.output_file)

    sys.exit(0)


if __name__ == '__main__':
    main()
