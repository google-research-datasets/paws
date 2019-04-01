#!/usr/bin/python
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Script to build PAWS-QQP data from the original QQP corpus.

Link to the original QQP:
  https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs
"""

from __future__ import print_function

import argparse
import ast
import csv
import nltk


def _tokenize(x):
  """Tokenizes input using NLTK."""
  return nltk.word_tokenize(x)


def _update_qqp_data(question, qid, qid_to_tokens):
  """Tokenizes input and add tokens to dictionaries."""
  tokens = _tokenize(question)
  if qid not in qid_to_tokens:
    qid_to_tokens[qid] = tokens


def _read_original_qqp(filename):
  """Loads and tokenizes original QQP corpus."""
  fieldnames = ["id", "qid1", "qid2", "question1", "question2", "is_duplicate"]
  csvin = open(filename, "r")
  reader = csv.DictReader(csvin, fieldnames=fieldnames, delimiter="\t")
  qid_to_tokens = {}
  count = 0
  for row in reader:
    count += 1
    if count == 1:
      continue
    q1 = row["question1"].decode("utf-8")
    q2 = row["question2"].decode("utf-8")
    _update_qqp_data(q1, int(row["qid1"]), qid_to_tokens)
    _update_qqp_data(q2, int(row["qid2"]), qid_to_tokens)
  return qid_to_tokens


def _get_token(qid, index, qid_to_tokens):
  """Convert index to token string."""
  if qid not in qid_to_tokens:
    print("Question ID {} not found, perhaps due to a change of QQP. "
          "Failed to build this example.".format(qid))
    return ""
  tokens = qid_to_tokens[qid]
  if index >= len(tokens):
    print("Token index out of array, perhaps due to a change of QQP or "
          "the NLTK version not being 3.2.5. Failed to build this example.")
    return ""
  else:
    return tokens[index]


def _build_sentence(indices_str, qid, qid_to_tokens):
  """Build sentence from index string."""
  indices = indices_str.split("/")
  tokens = []
  for index in indices:
    if index[0] != "(":
      token = _get_token(qid, int(index), qid_to_tokens)
      if not token:
        return ""
      tokens.append(token)
    else:
      token = ""
      for sub_index in index.split(":"):
        sub_index_tuple = ast.literal_eval(sub_index)
        sub_token = _get_token(sub_index_tuple[0], sub_index_tuple[1],
                               qid_to_tokens)
        if not sub_token:
          return ""
        token += sub_token
      tokens.append(token)
  return " ".join(tokens).encode("utf-8")


def _build_and_write_row(row, writer, qid_to_words):
  """Build an example and write it to output."""
  sentence1 = _build_sentence(row["sentence1"], int(row["qid1"]), qid_to_words)
  if not sentence1:
    return False
  sentence2 = _build_sentence(row["sentence2"], int(row["qid2"]), qid_to_words)
  if not sentence2:
    return False
  else:
    writer.writerow([str(row["id"]), sentence1, sentence2, row["label"]])
    return True


def main(args):
  """Generate PAWS-QQP data from the original QQP corpus.

  Args:
    args: argparse contining paths to input and output files.
  """
  print("Reading the original QQP corpus. This may take a while.")
  qid_to_tokens = _read_original_qqp(args.original_qqp_input)

  paws_qqp_output_csv = open(args.paws_output, "w")
  fieldnames = ["id", "sentence1", "sentence2", "label"]
  writer = csv.writer(paws_qqp_output_csv, delimiter="\t", quotechar=None)
  writer.writerow(fieldnames)

  paws_qqp_input_csv = open(args.paws_input, "r")
  fieldnames = ["id", "qid1", "sentence1", "qid2", "sentence2", "label"]
  reader = csv.DictReader(
      paws_qqp_input_csv, fieldnames=fieldnames, delimiter="\t")
  print("Generating the PAWS-QQP corpus.")
  success = 0
  fail = 0
  for i, row in enumerate(reader):
    # Skip first row.
    if i == 0:
      continue
    if _build_and_write_row(row, writer, qid_to_tokens):
      success += 1
    else:
      fail += 1
  paws_qqp_input_csv.close()
  paws_qqp_output_csv.close()
  print("******Final Results********")
  print("  Success: {}".format(success))
  print("  Fail:    {}".format(fail))
  print("  Total:   {}".format(success + fail))


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument(
      "--original_qqp_input",
      dest="original_qqp_input",
      required=True,
      help="Path to the original QQP corpus.")
  parser.add_argument(
      "--paws_input",
      dest="paws_input",
      required=True,
      help="Path to the PAWS-QQP input file.")
  parser.add_argument(
      "--paws_output",
      dest="paws_output",
      required=True,
      help="Final PAWS-QQP data in the TSV format.")
  main(parser.parse_args())
