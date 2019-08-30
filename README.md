# PAWS: Paraphrase Adversaries from Word Scrambling

**\*\*\*\*\* New August 27th, 2019: Multilingual PAWS for six languages
\*\*\*\*\***

We released PAWS-X, a multilingual version of PAWS for six languages. See
[here](https://github.com/google-research-datasets/paws/tree/master/pawsx) for
more details.

**\*\*\*\*\* End new information \*\*\*\*\***

This dataset contains 108,463 human-labeled and 656k noisily labeled pairs that
feature the importance of modeling structure, context, and word order
information for the problem of paraphrase identification. The dataset has two
subsets, one based on Wikipedia and the other one based on the
[Quora Question Pairs](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs)
(QQP) dataset.

For further details, see the accompanying paper:
[PAWS: Paraphrase Adversaries from Word Scrambling](https://arxiv.org/abs/1904.01130)

## Motivation

Existing paraphrase identification datasets lack sentence pairs that have high
lexical overlap without being paraphrases. Models trained on such data fail to
distinguish pairs like *flights from New York to Florida* and *flights from
Florida to New York*.

Below are two examples from the dataset:

|     | Sentence 1                    | Sentence 2                    | Label |
| :-- | :---------------------------- | :---------------------------- | :---- |
| (1) | Although interchangeable, the body pieces on the 2 cars are not similar. | Although similar, the body parts are not interchangeable  on the 2 cars.  | 0     |
| (2) | Katz was born in Sweden in 1947 and moved to New York City at the age of 1.      | Katz was born in 1947 in Sweden and moved to New York at the age of one.   | 1     |

The first pair has different semantic meaning while the second pair is a
paraphrase. State-of-the-art models trained on existing datasets have dismal
performance on PAWS (<40% accuracy); however, including PAWS training data for
these models improves their accuracy to 85% while maintaining performance on
existing datasets such as the
[Quora Question Pairs](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs).

## PAWS-Wiki

This corpus contains pairs generated from Wikipedia pages, and can be downloaded
here:

*   [`PAWS-Wiki Labeled (Final)`](https://storage.googleapis.com/paws/english/paws_wiki_labeled_final.tar.gz):
    containing pairs that are generated from both word swapping and back
    translation methods. All pairs have human judgements on both paraphrasing
    and fluency and they are split into Train/Dev/Test sections.
*   [`PAWS-Wiki Labeled (Swap-only)`](https://storage.googleapis.com/paws/english/paws_wiki_labeled_swap.tar.gz):
    containing pairs that have no back translation counterparts and therefore
    they are not included in the first set. Nevertheless, they are high-quality
    pairs with human judgements on both paraphrasing and fluency, and they can
    be included as an auxiliary training set.
*   [`PAWS-Wiki Unlabeled (Final)`](https://storage.googleapis.com/paws/english/paws_wiki_unlabeled_final.tar.gz):
    Pairs in this set have noisy labels without human judgments and can also be
    used as an auxiliary training set. They are generated from both word
    swapping and back translation methods.

All files are in the tsv format with four columns:

Column Name   | Data
:------------ | :--------------------------
id            | A unique id for each pair
sentence1     | The first sentence
sentence2     | The second sentence
(noisy_)label | (Noisy) label for each pair

Each label has two possible values: `0` indicates the pair has different
meaning, while `1` indicates the pair is a paraphrase.

The number of examples and the proportion of paraphrase (Yes%) pairs are shown
below:

Data                | Train   | Dev    | Test  | Yes%
:------------------ | ------: | -----: | ----: | ----:
Labeled (Final)     | 49,401  | 8,000  | 8,000 | 44.2%
Labeled (Swap-only) | 30,397  | --     | --    | 9.6%
Unlabeled (Final)   | 645,652 | 10,000 | --    | 50.0%

We also release source sentences that are used to generate this dataset and
their mappings. Please see
[here](https://github.com/google-research-datasets/paws/tree/master/wiki_raw_and_mapping#raw-sentences-and-mappings-for-paws-wiki)
for more details.

## PAWS-QQP

This corpus contains pairs generated from the
[Quora Question Pairs](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs)
corpus. We cannot directly distribute the raw `PAWS-QQP` data due to the license
of QQP, so the examples must be reconstructed by downloading the original data
and then running our scripts to produce the data and attach the labels.

To reconstruct the `PAWS-QQP` corpus, first download the original
[Quora Question Pairs dataset](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs)
and save the tsv file to some location `/path/to/original_qqp/data.tsv`. Then
download the `PAWS-QQP` index file from the following link:

*   [`PAWS-QQP Index (Final)`](https://storage.googleapis.com/paws/english/paws_qqp.tar.gz)

Unpack it to some directory `/path/to/paws_qqp/`. Run the following commands to
generate the corpus.

```shell
export ORIGINAL_QQP_FILE="/path/to/original_qqp/data.tsv"
export PAWS_QQP_DIR="/path/to/paws_qqp/"
export PAWS_QQP_OUTPUT_DIR="/path/to/paws_qqp/output/"

python qqp_generate_data.py \
  --original_qqp_input="${ORIGINAL_QQP_FILE}" \
  --paws_input="${PAWS_QQP_DIR}/train.tsv" \
  --paws_output="${PAWS_QQP_OUTPUT_DIR}/train.tsv"

python qqp_generate_data.py \
  --original_qqp_input="${ORIGINAL_QQP_FILE}" \
  --paws_input="${PAWS_QQP_DIR}/dev_and_test.tsv" \
  --paws_output="${PAWS_QQP_OUTPUT_DIR}/dev_and_test.tsv"
```

Note: this script requires NLTK and was tested on version 3.2.5.

The generated tsv files have the same format as `PAWS-Wiki`. All pairs are
manually labeled, and the number of examples and the proportion of paraphrase
(Yes%) pairs are shown below:

Data     | Train  | Dev and Test | Yes%
:------- | -----: | -----------: | ----:
PAWS-QQP | 11,988 | 677          | 31.3%

For the experiments in our paper, we used the train/dev/test split of the
original QQP from [Wang et al, 2017](https://arxiv.org/abs/1702.03814).

## PAWS-X

This corpus contains translations of the PAWS examples in six typologically
distinct languages: French, Spanish, German, Chinese, Japanese, and Korean.
Please see
[here](https://github.com/google-research-datasets/paws/tree/master/pawsx) for
more details.

Note: for multilingual experiments, please use `dev_2k.tsv` provided in the
PAWS-X repo as the development sets for all languages, including English.

## Reference

If you use or discuss this dataset in your work, please cite the following
papers correspondingly:

```
@InProceedings{paws2019naacl,
  title = {{PAWS: Paraphrase Adversaries from Word Scrambling}},
  author = {Zhang, Yuan and Baldridge, Jason and He, Luheng},
  booktitle = {Proc. of NAACL},
  year = {2019}
}

@InProceedings{pawsx2019emnlp,
  title = {{PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase Identification}},
  author = {Yang, Yinfei and Zhang, Yuan and Tar, Chris and Baldridge, Jason},
  booktitle = {Proc. of EMNLP},
  year = {2019}
}
```

## Contact

If you have a technical question regarding the dataset or publication, please
create an issue in this repository.
