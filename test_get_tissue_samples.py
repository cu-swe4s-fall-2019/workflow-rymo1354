import unittest
import random
import os
import get_tissue_samples


class TestGetTissueSamples(unittest.TestCase):
    def test_parser(self):
        sample = 'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
        group_type = 'SMTS'
        gene_dict, tissue = get_tissue_samples.parse_meta(group_type, sample)
        self.assertNotEqual(tissue, None)
        tissue.sort()
        self.assertEqual(tissue[0], 'Adipose Tissue')
        self.assertEqual(tissue[30], 'Vagina')

    def test_linear_search(self):
        L = [10, 20, 30, 40, 50, 60]

        r = get_tissue_samples.linear_search(30, L)
        self.assertEqual(r, 2)
        r = get_tissue_samples.linear_search(70, L)
        self.assertEqual(r, -1)


if __name__ == '__main__':
    unittest.main()
