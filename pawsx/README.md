# PAWS-X

This dataset contains 23,659 **human** translated PAWS evaluation pairs and
296,406 **machine** translated training pairs in six typologically distinct
languages: French, Spanish, German, Chinese, Japanese, and Korean. All
translated pairs are sourced from examples in
[PAWS-Wiki](https://github.com/google-research-datasets/paws#paws-wiki).

The dataset can be downloaded here:

*   [`PAWS-X for six languages`](https://storage.googleapis.com/paws/pawsx/x-final.tar.gz)

For further details, see the accompanying paper:
[PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase
Identification](https://arxiv.org/abs/1908.11828)

Note: for multilingual experiments, please use `dev_2k.tsv` provided in the
PAWS-X repo as the development sets for all languages, including English.

## Data Format and Statistics

All files are in tsv format with four columns:

Column Name | Data
:---------- | :--------------------------------------------------------
id          | An ID that matches the ID of the source pair in PAWS-Wiki
sentence1   | The first sentence
sentence2   | The second sentence
label       | Label for each pair

The source text of each translation can be retrieved by looking up the ID in the
corresponding file in PAWS-Wiki.

The numbers of examples for each of the six languages are shown below:

Language | Train   | Dev    | Test
:------- | ------: | -----: | -----:
fr       | 49,401  | 1,992  | 1,985
es       | 49,401  | 1,962  | 1,999
de       | 49,401  | 1,932  | 1,967
zh       | 49,401  | 1,984  | 1,975
ja       | 49,401  | 1,980  | 1,946
ko       | 49,401  | 1,965  | 1,972
Total    | 296,406 | 11,815 | 11,844

> **Caveat**: please note that the dev and test sets of PAWS-X are both sourced
> from the dev set of PAWS-Wiki. As a consequence, the same `sentence 1` may
> appear in both the dev and test sets. Nevertheless our data split guarantees
> that there is no overlap on sentence pairs (`sentence 1` + `sentence 2`)
> between dev and test.

## Reference

If you use or discuss this dataset in your work, please cite our paper:

```
@InProceedings{pawsx2019emnlp,
  title = {{PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase Identification}},
  author = {Yang, Yinfei and Zhang, Yuan and Tar, Chris and Baldridge, Jason},
  booktitle = {Proc. of EMNLP},
  year = {2019}
}
```
