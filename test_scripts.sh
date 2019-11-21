#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle test_get_gene_counts.py
assert_no_stdout
run test_style pycodestyle get_gene_counts.py
assert_no_stdout

run test_style pycodestyle test_get_tissue_samples.py
assert_no_stdout
run test_style pycodestyle get_tissue_samples.py
assert_no_stdout

run test_style pycodestyle test_box.py
assert_no_stdout
run test_style pycodestyle box.py
assert_no_stdout

echo "...Get counts for ACTA2 gene..."
run test_acta2_counts python3 get_gene_counts.py -of out.txt -gn ACTA2 -gc GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true.gz
assert_exit_code 0
assert_no_stdout
rm out.txt

echo "...Get tissue samples for SMTS group type..."
run test_smts_samples python3 get_tissue_samples.py -of out.txt -gt SMTS -sa GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
assert_exit_code 0
assert_no_stdout
rm out.txt

echo "...Meta data does not exist..."
run test_bad_meta python3 box.py -t "Brain Heart Blood Skin" -g "SDHB MEN1 KCNH2 MSH2 MYL2 BRCA2" -of out.png -mf does_not_exist.txt
assert_exit_code 1
assert_stdout
