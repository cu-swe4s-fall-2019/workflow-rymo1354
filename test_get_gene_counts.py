import unittest
import random
import os
import get_gene_counts


class TestGetGeneCounts(unittest.TestCase):
    def test_parser(self):
        gene = 'SDHB'
        get_gene_counts.parse_gene_counts(gene, 'test.txt',
                                          'GTEx_Analysis_2017-06-05'
                                          '_v8_RNASeQCv1.1.9_gene_reads'
                                          '.acmg_59.gct.gz?raw=true.gz')
        self.assertTrue(os.path.exists('test.txt'))
        os.remove('test.txt')

    def test_output(self):
        gene = 'ACTA2'
        get_gene_counts.parse_gene_counts(gene, 'test.txt',
                                          'GTEx_Analysis_2017-06-05'
                                          '_v8_RNASeQCv1.1.9_gene_reads'
                                          '.acmg_59.gct.gz?raw=true.gz')
        with open('test.txt') as f:
            first_line = f.readline().rstrip()
        self.assertEqual('GTEX-1117F-0226-SM-5GZZ7: 12528', first_line)
        os.remove('test.txt')

    def test_linear_search(self):
        L = [10, 20, 30, 40, 50, 60]

        r = get_gene_counts.linear_search(30, L)
        self.assertEqual(r, 2)
        r = get_gene_counts.linear_search(70, L)
        self.assertEqual(r, -1)


if __name__ == '__main__':
    unittest.main()
