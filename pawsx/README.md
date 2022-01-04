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

Note: As discussed [here](https://github.com/google-research-datasets/paws/issues/15), a small number of samples in the translated dev and tests contain the placeholder "NS". Please make sure you clean them up.

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


## Dataset Metadata
The following table is necessary for this dataset to be indexed by search
engines such as <a href="https://g.co/datasetsearch">Google Dataset Search</a>.
<div itemscope itemtype="http://schema.org/Dataset">
<table>
  <tr>
    <th>property</th>
    <th>value</th>
  </tr>
  <tr>
    <td>name</td>
    <td itemprop="name">PAWS-X</td>
  </tr>
  <tr>
    <td>alternateName</td>
    <td itemprop="alternateName">Paraphrase Adversaries from Word Scrambling</td>
  </tr>
  <tr>
    <td>description</td>
    <td itemprop="description">PAWS-X dataset contains 23,659 human translated PAWS evaluation pairs and 296,406 machine translated training pairs in six typologically distinct languages: French, Spanish, German, Chinese, Japanese, and Korean. All translated pairs are sourced from examples in <a href="https://github.com/google-research-datasets/paws#paws-wiki">PAWS-Wiki.</a>
   </td>
  </tr>
  <tr>
    <td>url</td>
    <td><code itemprop="url">https://github.com/google-research-datasets/paws/tree/master/pawsx</code></td>
  </tr>
  <tr>
      <td>provider</td>
    <td>
      <div itemscope itemtype="http://schema.org/Organization" itemprop="provider">
        <table>
          <tr>
            <th>property</th>
            <th>value</th>
          </tr>
          <tr>
            <td>name</td>
            <td itemprop="name">Google</td>
          </tr>
          <tr>
            <td>url</td>
            <td><code itemprop="url">https://en.wikipedia.org/wiki/Google</code></td>
          </tr>
        </table>
      </div>
    </td>
  </tr>
  <tr>
    <td>license</td>
    <td>
      <div itemscope itemtype="http://schema.org/CreativeWork" itemprop="license">
      <table>
          <tr>
            <th>property</th>
            <th>value</th>
          </tr>
          <tr>
            <td>name</td>
            <td  itemprop="name">
    The dataset may be freely used for any purpose, although acknowledgement of
Google LLC ("Google") as the data source would be appreciated. The dataset is
provided "AS IS" without any warranty, express or implied. Google disclaims all
liability for any damages, direct or indirect, resulting from the use of the
dataset. 
          </td>
        </tr>
        <tr>
          <td>url</td>
          <td>
            <code itemprop="url">https://github.com/google-research-datasets/paws/blob/master/LICENSE</code>
          </td>
        </tr>
        </table>
        </div>
      </td>
    </tr>
    <tr>
  <td>citation</td>
  <td itemprop="citation"> Yinfei Yang, Yuan Zhang, Chris Tar, Jason Baldridge "PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase Identification", Proceedings of EMNLP, 2019
  </td>
    </tr>
 </table>
</div>
  
